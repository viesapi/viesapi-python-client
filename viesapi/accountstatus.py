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


class AccountStatus:
    """
    Account status
    """

    def __init__(self):
        self.uid = None

        self.type = None
        self.valid_to = None
        self.billing_plan_name = None

        self.subscription_price = None
        self.item_price = None
        self.item_price_status = None

        self.limit = None
        self.request_delay = None
        self.domain_limit = None
        self.over_plan_allowed = None
        self.excel_addin = None

        self.app = None
        self.cli = None
        self.stats = None
        self.monitor = None

        self.func_get_vies_data = None

        self.vies_data_count = None
        self.total_count = None

    def __str__(self):
        return 'AccountStatus: [uid = ' + str(self.uid) \
            + ', type = ' + str(self.type) \
            + ', valid_to = ' + str(self.valid_to) \
            + ', billing_plan_name = ' + str(self.billing_plan_name) \
            + ', subscription_price = ' + str(self.subscription_price) \
            + ', item_price = ' + str(self.item_price) \
            + ', item_price_status = ' + str(self.item_price_status) \
            + ', limit = ' + str(self.limit) \
            + ', request_delay = ' + str(self.request_delay) \
            + ', domain_limit = ' + str(self.domain_limit) \
            + ', over_plan_allowed = ' + str(self.over_plan_allowed) \
            + ', excel_addin = ' + str(self.excel_addin) \
            + ', app = ' + str(self.app) \
            + ', cli = ' + str(self.cli) \
            + ', stats = ' + str(self.stats) \
            + ', monitor = ' + str(self.monitor) \
            + ', func_get_vies_data = ' + str(self.func_get_vies_data) \
            + ', vies_data_count = ' + str(self.vies_data_count) \
            + ', total_count = ' + str(self.total_count) \
            + ']'
