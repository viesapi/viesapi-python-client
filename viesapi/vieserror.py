#
# -*- coding: utf-8 -*-
#
# Copyright 2022-2025 NETCAT (www.netcat.pl)
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
# @copyright 2022-2025 NETCAT (www.netcat.pl)
# @license https://www.apache.org/licenses/LICENSE-2.0
#


class VIESError:
    """
    VIES error
    """

    def __init__(self):
        self.uid = None
        self.country_code = None
        self.vat_number = None
        self.error = None
        self.date = None
        self.source = None

    def __str__(self):
        return 'VIESError: [uid = ' + str(self.uid) \
            + ', country_code = ' + str(self.country_code) \
            + ', vat_number = ' + str(self.vat_number) \
            + ', error = ' + str(self.error) \
            + ', date = ' + str(self.date) \
            + ', source = ' + str(self.source) \
            + ']'
