########
# Copyright (c) 2019 Fortinet
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

import traceback

from cloudify import ctx
from cloudify.exceptions import NonRecoverableError, RecoverableError

from fortigate_sdk import utility, exceptions


def execute(params, template_file, **kwargs):
    if not params:
        params = {}

    if not template_file:
        ctx.logger.info(
            'Processing finished. No template file provided.')
        return

    ctx.logger.info(
        'Execute:\n'
        'params: {}\n'
        'template_file: {}'.format(params, template_file))

    runtime_properties = ctx.instance.runtime_properties.copy()

    ctx.logger.info(
        'Runtime properties get_all: {}'.format(runtime_properties))
    for ctxrel in ctx.instance.relationships:
        ctx.logger.info(
            'ctx instance: {}'.format(ctxrel.type))
        ctx.logger.info(
            'ctx instance: {}'.format(ctxrel.target.instance.runtime_properties))
        ctx.logger.info(
            'ctx instance: {}'.format(ctxrel.target.node.properties))

    # Replace host config with runtime propertie (instead of rearchitect the plugin)
    params['host'] = ctx.instance.host_ip
    runtime_properties.update(params)

    ctx.logger.debug(
        'Runtime properties: {}'.format(runtime_properties))

    template = ctx.get_resource(template_file)
    request_props = ctx.node.properties.copy()

    ctx.logger.debug(
        'request_props: {}'.format(request_props))

    try:
        ctx.instance.runtime_properties.update(
            utility.process(
                params,
                template,
                request_props))

    except exceptions.NonRecoverableResponseException as e:
        ctx.logger.debug(
            '--sss--> Nonrecoverable: {}'.format(e))
        raise NonRecoverableError(e)

    except (exceptions.RecoverableResponseException,
            exceptions.RecoverableStatusCodeCodeException)as e:
        ctx.logger.debug(
            '--sss--> Recoverable: {}'.format(e))
        raise RecoverableError(e)

    except Exception as e:
        ctx.logger.info(
            'Exception traceback : {}'.format(traceback.format_exc()))
        raise NonRecoverableError(e)


def execute_relation(params, template_file, **kwargs):
    if not params:
        params = {}

    if not template_file:
        ctx.logger.info(
            'Processing finished. No template file provided.')
        return

    ctx.logger.debug(
        'Execute:\n'
        'params: {}\n'
        'template_file: {}'.format(params, template_file))

    runtime_properties = ctx.source.node.properties.copy()
    runtime_properties.update(params)

    ctx.logger.debug(
        'Runtime properties: {}'.format(runtime_properties))

    template = ctx.get_resource(template_file)
    request_props = ctx.source.node.properties.copy()

    ctx.logger.debug(
        'request_props: {}'.format(request_props))
    ctx.logger.debug(
        'params: {}'.format(params))
    ctx.logger.debug(
        'template_file: {}'.format(template_file))

    try:
        ctx.target.instance.runtime_properties.update(
            utility.process(
                params,
                template,
                request_props))

    except exceptions.NonRecoverableResponseException as e:
        ctx.logger.debug(
            '--sss--> Nonrecoverable: {}'.format(e))
        raise NonRecoverableError(e)

    except (exceptions.RecoverableResponseException,
            exceptions.RecoverableStatusCodeCodeException)as e:
        ctx.logger.debug(
            '--sss--> Recoverable: {}'.format(e))
        raise RecoverableError(e)

    except Exception as e:
        ctx.logger.info(
            'Exception traceback : {}'.format(traceback.format_exc()))
        raise NonRecoverableError(e)
