# Copyright (c) 2017 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

import setuptools

setuptools.setup(
    name='cloudify-fortigate-plugin',
    version='0.0.1',
    author='Nicolas Thomas',
    author_email='nthomas@fortinet.com',
    description='Generic plugin for fortigate VMs or Physical',
    packages=setuptools.find_packages(),
#    packages=['fortigate_plugin',
#              'fortigate_sdk',
#              'fortigate_sdk.pyfmg',
#              'fortigate_sdk.pyfmg.pyFMG'],
    license='LICENSE',
    install_requires=[
        'fortiosapi',
        'cloudify-plugins-common>=3.4.2',
        'cloudify-rest-client>=4.0',
        'Jinja2>=2.7.2',  # for template support
        'pycrypto',
        'pyyaml',
        'xmltodict']
)
