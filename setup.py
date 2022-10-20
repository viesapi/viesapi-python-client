#
# -*- coding: utf-8 -*-
#
# Copyright 2022 NETCAT (www.netcat.pl)
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
# @copyright 2022 NETCAT (www.netcat.pl)
# @license https://www.apache.org/licenses/LICENSE-2.0
#

from setuptools import setup

setup(name='viesapi',
      version='1.2.3',
      description='VIES API Client for Python',
      url='https://viesapi.eu',
      author='NETCAT',
      author_email='firma@netcat.pl',
      license='https://www.apache.org/licenses/LICENSE-2.0',
      packages=['viesapi'],
      zip_safe=False,
      install_requires=['lxml', 'python-dateutil'])