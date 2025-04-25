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


class NameComponents:
    """
    Name components
    """

    def __init__(self):
        self.name = None
        self.legal_form = None
        self.legal_form_canonical_id = None
        self.legal_form_canonical_name = None

    def __str__(self):
        return 'NameComponents: [name = ' + str(self.name) \
            + ', legal_form = ' + str(self.legal_form) \
            + ', legal_form_canonical_id = ' + str(self.legal_form_canonical_id) \
            + ', legal_form_canonical_name = ' + str(self.legal_form_canonical_name) \
            + ']'
