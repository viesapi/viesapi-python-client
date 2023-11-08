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


class VIESData:
    """
    VIES data
    """

    def __init__(self):
        self.uid = None
        self.country_code = None
        self.vat_number = None
        self.valid = None
        self.trader_name = None
        self.trader_company_type = None
        self.trader_address = None
        self.id = None
        self.date = None
        self.source = None

    def __str__(self):
        return 'VIESData: [uid = ' + str(self.uid) \
            + ', country_code = ' + str(self.country_code) \
            + ', vat_number = ' + str(self.vat_number) \
            + ', valid = ' + str(self.valid) \
            + ', trader_name = ' + str(self.trader_name) \
            + ', trader_company_type = ' + str(self.trader_company_type) \
            + ', trader_address = ' + str(self.trader_address) \
            + ', id = ' + str(self.id) \
            + ', date = ' + str(self.date) \
            + ', source = ' + str(self.source) \
            + ']'
