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
from time import sleep

from viesapi import *

# Create client object and establish connection to the production system
# id – API identifier
# key – API key (keep it secret)
# viesapi = VIESAPIClient('id', 'key')

# Create client object and establish connection to the test system
viesapi = VIESAPIClient()

euvat = 'PL7171642051'

# SGet current account status
account = viesapi.get_account_status()

if account:
    print(account)
else:
    print('Error: ' + viesapi.get_last_error() + ' (code: ' + str(viesapi.get_last_error_code()) + ')')

# Get VIES data from VIES system
vies = viesapi.get_vies_data(euvat)

if vies:
    print(vies)
else:
    print('Error: ' + viesapi.get_last_error() + ' (code: ' + str(viesapi.get_last_error_code()) + ')')

# Get VIES data returning parsed trader name and address from VIES system
vies_parsed = viesapi.get_vies_data_parsed(euvat)

if vies_parsed:
    print(vies_parsed)
else:
    print('Error: ' + viesapi.get_last_error() + ' (code: ' + str(viesapi.get_last_error_code()) + ')')

# Upload batch of VAT numbers and get their current VAT statuses and traders data
numbers = [
    euvat,
    'DK56314210',
    'CZ7710043187'
]

token = viesapi.get_vies_data_async(numbers)

if token:
    print('Batch token: ' + token)
else:
    print('Error: ' + viesapi.get_last_error() + ' (code: ' + str(viesapi.get_last_error_code()) + ')')

# Check batch result and download data (at production it usually takes 2-3 min for result to be ready)
while True:
    result = viesapi.get_vies_data_async_result(token)
    if result:
        break

    if viesapi.get_last_error_code() != Error.BATCH_PROCESSING:
        print('Error: ' + viesapi.get_last_error() + ' (code: ' + str(viesapi.get_last_error_code()) + ')')
        break

    print('Batch is still processing, waiting...')
    sleep(10)

# Batch result is ready
print(result)
