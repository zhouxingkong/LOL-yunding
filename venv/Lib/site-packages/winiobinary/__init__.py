# -*- coding: utf-8 -*-

#
# Copyright 2018, Hong-She Liang <starofrainnight@gmail.com>.  All rights
# reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Top-level package for winio-binary."""

import os.path

__author__ = """Hong-She Liang"""
__email__ = 'starofrainnight@gmail.com'
__version__ = '0.0.6'


def get_data_dir(version='3.0'):
    return os.path.join(os.path.dirname(__file__), 'data', version)
