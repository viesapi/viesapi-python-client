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


class AddressComponents:
    """
    Address components
    """

    def __init__(self):
        self.country = None
        self.postal_code = None
        self.city = None
        self.street = None
        self.street_number = None
        self.house_number = None

    def __str__(self):
        return 'AddressComponents: [country = ' + str(self.country) \
            + ', postal_code = ' + str(self.postal_code) \
            + ', city = ' + str(self.city) \
            + ', street = ' + str(self.street) \
            + ', street_number = ' + str(self.street_number) \
            + ', house_number = ' + str(self.house_number) \
            + ']'
