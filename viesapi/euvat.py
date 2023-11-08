#
# -*- coding: utf-8 -*-
#
# Copyright 2022-2023 NETCAT (www.netcat.pl)
#
# Licensed under the Apache License, Version 2.0 (the "License"),
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

import re

from viesapi import NIP


class EUVAT:
    """
    EU VAT number verificator
    """

    @staticmethod
    def normalize(number):
        """
        Normalizes form of the VAT number
        :param number: input string
        :type number: str
        :returns: normalized string or False
        :rtype: str or False
        """

        if not number:
            return False

        number = re.sub('[ -]', '', number).upper()

        if not re.match('[A-Z]{2}[A-Z0-9+*]{2,12}', number):
            return False

        return number

    @staticmethod
    def is_valid(number):
        """
        Checks if specified NIP is valid
        :param number: input string
        :type number: str
        :returns: True if NIP is valid
        :rtype: bool
        """

        number = EUVAT.normalize(number)

        if not number:
            return False

        cmap = {
            'AT': 'ATU\\d{8}',
            'BE': 'BE[0-1]{1}\\d{9}',
            'BG': 'BG\\d{9,10}',
            'CY': 'CY\\d{8}[A-Z]{1}',
            'CZ': 'CZ\\d{8,10}',
            'DE': 'DE\\d{9}',
            'DK': 'DK\\d{8}',
            'EE': 'EE\\d{9}',
            'EL': 'EL\\d{9}',
            'ES': 'ES[A-Z0-9]{1}\\d{7}[A-Z0-9]{1}',
            'FI': 'FI\\d{8}',
            'FR': 'FR[A-Z0-9]{2}\\d{9}',
            'HR': 'HR\\d{11}',
            'HU': 'HU\\d{8}',
            'IE': 'IE[A-Z0-9+*]{8,9}',
            'IT': 'IT\\d{11}',
            'LT': 'LT\\d{9,12}',
            'LU': 'LU\\d{8}',
            'LV': 'LV\\d{11}',
            'MT': 'MT\\d{8}',
            'NL': 'NL[A-Z0-9+*]{12}',
            'PL': 'PL\\d{10}',
            'PT': 'PT\\d{9}',
            'RO': 'RO\\d{2,10}',
            'SE': 'SE\\d{12}',
            'SI': 'SI\\d{8}',
            'SK': 'SK\\d{10}',
            'XI': 'XI[A-Z0-9]{5,12}'
        }

        cc = number[0:2].upper()
        num = number[2:].upper()

        if cc not in cmap:
            return False

        if not re.match(cmap[cc], number):
            return False

        if cc == 'PL':
            return NIP.is_valid(num)

        return True
