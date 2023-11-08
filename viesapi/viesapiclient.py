#
# -*- coding: utf-8 -*-
#
# Copyright 2022-2023 NETCAT (www.netcat.pl)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author NETCAT <firma@netcat.pl>
# @copyright 2022-2023 NETCAT (www.netcat.pl)
# @license https://www.apache.org/licenses/LICENSE-2.0
#

import base64
import datetime
import hashlib
import hmac
import os
import sys
import time
import urllib.request
import urllib.parse
import urllib.error

from viesapi import Error, Number, NIP, EUVAT, VIESData, AccountStatus
from io import BytesIO
from lxml import etree
from dateutil.parser import parse


class VIESAPIClient:
    """
    VIESAPI service client
    """

    VERSION = '1.2.6'

    PRODUCTION_URL = 'https://viesapi.eu/api'
    TEST_URL = 'https://viesapi.eu/api-test'

    TEST_ID = 'test_id'
    TEST_KEY = 'test_key'

    HMAC_ALG = hashlib.sha256

    def __init__(self, id=None, key=None):
        """
        Construct new service client object
        :param id: VIES API key identifier
        :type id: str
        :param key: VIES API key
        :type key: str
        """
        self.__url__ = self.TEST_URL
        self.__id__ = self.TEST_ID
        self.__key__ = self.TEST_KEY

        if id is not None and key is not None:
            self.__url__ = self.PRODUCTION_URL
            self.__id__ = id
            self.__key__ = key

        self.__clear()

    def set_url(self, url):
        """
        Set non default service URL
        :param url: service URL
        :type url: str
        """

        self.__url__ = url

    def get_vies_data(self, euvat):
        """
        Get VIES data for specified number
        :param euvat: EU VAT number with 2-letter country prefix
        :type euvat: str
        :return: VIESData object or False
        :rtype: VIESData or False
        """

        # clear error
        self.__clear()

        # validate number and construct path
        suffix = self.__get_path_suffix(Number.EUVAT, euvat)

        if not suffix:
            return False

        # prepare url
        url = self.__url__ + '/get/vies/' + suffix

        # send request
        doc = self.__get(url)

        if not doc:
            return False

        # parse response
        vies = VIESData()

        vies.uid = self.__get_text(doc, '/result/vies/uid/text()')

        vies.country_code = self.__get_text(doc, '/result/vies/countryCode/text()')
        vies.vat_number = self.__get_text(doc, '/result/vies/vatNumber/text()')

        vies.valid = True if self.__get_text(doc, '/result/vies/valid/text()') == 'true' else False

        vies.trader_name = self.__get_text(doc, '/result/vies/traderName/text()')
        vies.trader_company_type = self.__get_text(doc, '/result/vies/traderCompanyType/text()')
        vies.trader_address = self.__get_text(doc, '/result/vies/traderAddress/text()')

        vies.id = self.__get_text(doc, '/result/vies/id/text()')
        vies.date = self.__get_date(doc, '/result/vies/date/text()')
        vies.source = self.__get_text(doc, '/result/vies/source/text()')

        return vies

    def get_account_status(self):
        """
        Get user account's status
        :return: AccountStatus object or False
        :rtype: AccountStatus or False
        """

        # clear error
        self.__clear()

        # prepare url
        url = self.__url__ + '/check/account/status'

        # send request
        doc = self.__get(url)

        if not doc:
            return False

        # parse response
        status = AccountStatus()

        status.uid = self.__get_text(doc, '/result/account/uid/text()')
        status.type = self.__get_text(doc, '/result/account/type/text()')
        status.valid_to = self.__get_date_time(doc, '/result/account/validTo/text()')
        status.billing_plan_name = self.__get_text(doc, '/result/account/billingPlan/name/text()')

        status.subscription_price = float(
            '0' + self.__get_text(doc, '/result/account/billingPlan/subscriptionPrice/text()'))
        status.item_price = float('0' + self.__get_text(doc, '/result/account/billingPlan/itemPrice/text()'))
        status.item_price_status = float(
            '0' + self.__get_text(doc, '/result/account/billingPlan/itemPriceCheckStatus/text()'))

        status.limit = int(self.__get_text(doc, '/result/account/billingPlan/limit/text()'))
        status.request_delay = int(self.__get_text(doc, '/result/account/billingPlan/requestDelay/text()'))
        status.domain_limit = int(self.__get_text(doc, '/result/account/billingPlan/domainLimit/text()'))
        status.over_plan_allowed = True if self.__get_text(doc,
                                                         '/result/account/billingPlan/overplanAllowed/text()') == 'true' else False
        status.excel_addin = True if self.__get_text(doc,
                                                    '/result/account/billingPlan/excelAddin/text()') == 'true' else False

        status.app = True if self.__get_text(doc, '/result/account/billingPlan/app/text()') == 'true' else False
        status.cli = True if self.__get_text(doc, '/result/account/billingPlan/cli/text()') == 'true' else False
        status.stats = True if self.__get_text(doc, '/result/account/billingPlan/stats/text()') == 'true' else False
        status.monitor = True if self.__get_text(doc, '/result/account/billingPlan/monitor/text()') == 'true' else False

        status.func_get_vies_data = True if self.__get_text(doc,
                                                         '/result/account/billingPlan/funcGetVIESData/text()') == 'true' else False

        status.vies_data_count = int(self.__get_text(doc, '/result/account/requests/viesData/text()'))
        status.total_count = int(self.__get_text(doc, '/result/account/requests/total/text()'))

        return status

    def get_last_error_code(self):
        """
        Get last error code
        :return: error code
        :rtype: int
        """

        return self.__errcode__

    def get_last_error(self):
        """
        Get last error message
        :return: unicode string
        :rtype: str
        """

        return self.__err__

    def __clear(self):
        """
        Clear error info
        """

        self.__errcode__ = 0
        self.__err__ = ''

    def __set(self, code, err=None):
        """
        Set error info
        :param code: error code
        :type code: int
        :param err: error message
        :type err: str
        """

        self.__errcode__ = code
        self.__err__ = err if err else Error.message(code)

    def __auth(self, method, url):
        """
        Prepare authorization header content
        :param method: HTTP method
        :type method: str
        :param url: target URL
        :type url: str
        :returns: authorization header content or False
        :rtype: str or False
        """

        # parse url
        u = urllib.parse.urlparse(url)
        ls = u.netloc.split(':')

        host = ls[0]
        port = 443 if u.scheme == 'https' else 80

        if len(ls) > 1:
            port = ls[1]

        # prepare auth header value
        nonce = os.urandom(4).hex()
        ts = int(time.time())

        s = '' + str(ts) + '\n' \
            + nonce + '\n' \
            + method + '\n' \
            + u.path + '\n' \
            + host + '\n' \
            + str(port) + '\n' \
            + '\n'

        mac = base64.b64encode(hmac.new(self.__key__.encode(), s.encode(), self.HMAC_ALG).digest()).decode()

        return 'MAC id="' + self.__id__ + '", ts="' + str(ts) + '", nonce="' + nonce + '", mac="' + mac + '"'

    def __user_agent(self):
        """
        Prepare user agent information header content
        :return: user agent header content
        :rtype: str
        """

        return 'VIESAPIClient/' + self.VERSION + ' Python/' + str(sys.version_info[0]) \
            + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2])

    def __parse(self, data):
        """
        Parse HTTP response
        :param data: response data
        :type data: Any
        :returns: XML document or False
        :rtype: ElementTree or False
        """
        try:
            doc = etree.parse(BytesIO(data))

            if not doc:
                self.__set(Error.CLI_RESPONSE)
                return False

            code = self.__get_text(doc, '/result/error/code/text()')

            if len(code) > 0:
                self.__set(int(code), self.__get_text(doc, '/result/error/description/text()'))
                return False

            return doc
        except Exception as e:
            self.__set(Error.CLI_EXCEPTION, str(e))
        return False

    def __get(self, url):
        """
        Get result of HTTP GET request
        :param url: target URL
        :type url: str
        :returns: result as XML document
        :rtype: ElementTree or False
        """

        # auth
        auth = self.__auth('GET', url)

        if not auth:
            return False

        # send request
        try:
            req = urllib.request.Request(url)
            req.add_header('Accept', 'text/xml')
            req.add_header('Authorization', auth)
            req.add_header('User-Agent', self.__user_agent())

            res = urllib.request.urlopen(req)

            return self.__parse(res.read())
        except urllib.error.HTTPError as he:
            if self.__parse(he.read()):
                self.__set(Error.CLI_EXCEPTION, he.reason)
        except urllib.error.URLError as ue:
            self.__set(Error.CLI_EXCEPTION, ue.reason)
        return False

    def __get_text(self, doc, xpath):
        """
        Get XML element as text
        :param doc: etree document
        :type doc: tree
        :param xpath: xpath string
        :type xpath: string
        :return: string
        :rtype: str
        """

        s = doc.xpath(xpath)

        if not s:
            return ''

        if len(s) != 1:
            return ''

        return str(s[0].strip())

    def __get_date_time(self, doc, xpath):
        """
        Get XML element as date time object
        :param doc: etree document
        :type doc: tree
        :param xpath: xpath string
        :type xpath: string
        :return: datetime
        :rtype: datetime or None
        """

        s = self.__get_text(doc, xpath)

        if len(s) == 0:
            return None

        return parse(s)

    def __get_date(self, doc, xpath):
        """
        Get XML element as date object
        :param doc: etree document
        :type doc: tree
        :param xpath: xpath string
        :type xpath: string
        :return: datetime
        :rtype: datetime or None
        """

        s = self.__get_text(doc, xpath)

        sl = len(s)

        if sl == 0:
            return None
        elif sl == 11:
            # dateutil does not support xsd:date type in form YYYY-MM-DDZ
            s = s[0:10] + 'T00:00:00Z'
        elif sl == 16:
            # dateutil does not support xsd:date type in form YYYY-MM-DD+00:00
            s = s[0:10] + 'T00:00:00' + s[10:]

        return parse(s)

    def __get_path_suffix(self, type, number):
        """
        Get path suffix
        :param type: search number type as Number.xxx value
        :type type: Number
        :param number: search number value
        :type number: str
        :return: path suffix
        :rtype: string or False
        """

        if type == Number.NIP:
            if not NIP.is_valid(number):
                self.__set(Error.CLI_NIP)
                return False

            path = 'nip/' + NIP.normalize(number)
        elif type == Number.EUVAT:
            if not EUVAT.is_valid(number):
                self.__set(Error.CLI_EUVAT)
                return False

            path = 'euvat/' + EUVAT.normalize(number)
        else:
            self.__set(Error.CLI_NUMBER)
            return False

        return path
