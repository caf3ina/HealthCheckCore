# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.186
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class EventBasedTasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_event_based_task(self, event_based_task, api_version, **kwargs):  # noqa: E501
        """Create an Event Based Task  # noqa: E501

        Create a new event based task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_event_based_task(event_based_task, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EventBasedTask event_based_task: The settings of the new event based task. (required)
        :param str api_version: The version of the api being called. (required)
        :return: EventBasedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_event_based_task_with_http_info(event_based_task, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_event_based_task_with_http_info(event_based_task, api_version, **kwargs)  # noqa: E501
            return data

    def create_event_based_task_with_http_info(self, event_based_task, api_version, **kwargs):  # noqa: E501
        """Create an Event Based Task  # noqa: E501

        Create a new event based task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_event_based_task_with_http_info(event_based_task, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EventBasedTask event_based_task: The settings of the new event based task. (required)
        :param str api_version: The version of the api being called. (required)
        :return: EventBasedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_based_task', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_event_based_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_based_task' is set
        if ('event_based_task' not in params or
                params['event_based_task'] is None):
            raise ValueError("Missing the required parameter `event_based_task` when calling `create_event_based_task`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_event_based_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'event_based_task' in params:
            body_params = params['event_based_task']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/eventbasedtasks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventBasedTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_event_based_task(self, event_based_task_id, api_version, **kwargs):  # noqa: E501
        """Delete an Event Based Task  # noqa: E501

        Delete an event based task by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_event_based_task(event_based_task_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int event_based_task_id: The ID number of the event based task to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_event_based_task_with_http_info(event_based_task_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_event_based_task_with_http_info(event_based_task_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_event_based_task_with_http_info(self, event_based_task_id, api_version, **kwargs):  # noqa: E501
        """Delete an Event Based Task  # noqa: E501

        Delete an event based task by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_event_based_task_with_http_info(event_based_task_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int event_based_task_id: The ID number of the event based task to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_based_task_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_event_based_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_based_task_id' is set
        if ('event_based_task_id' not in params or
                params['event_based_task_id'] is None):
            raise ValueError("Missing the required parameter `event_based_task_id` when calling `delete_event_based_task`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_event_based_task`")  # noqa: E501

        if 'event_based_task_id' in params and not re.search('\\d+', str(params['event_based_task_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `event_based_task_id` when calling `delete_event_based_task`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'event_based_task_id' in params:
            path_params['eventBasedTaskID'] = params['event_based_task_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/eventbasedtasks/{eventBasedTaskID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_event_based_task(self, event_based_task_id, api_version, **kwargs):  # noqa: E501
        """Describe an Event Based Task  # noqa: E501

        Describe an event based task by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_event_based_task(event_based_task_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int event_based_task_id: The ID number of the event based task to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: EventBasedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_event_based_task_with_http_info(event_based_task_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_event_based_task_with_http_info(event_based_task_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_event_based_task_with_http_info(self, event_based_task_id, api_version, **kwargs):  # noqa: E501
        """Describe an Event Based Task  # noqa: E501

        Describe an event based task by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_event_based_task_with_http_info(event_based_task_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int event_based_task_id: The ID number of the event based task to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :return: EventBasedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_based_task_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_event_based_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_based_task_id' is set
        if ('event_based_task_id' not in params or
                params['event_based_task_id'] is None):
            raise ValueError("Missing the required parameter `event_based_task_id` when calling `describe_event_based_task`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_event_based_task`")  # noqa: E501

        if 'event_based_task_id' in params and not re.search('\\d+', str(params['event_based_task_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `event_based_task_id` when calling `describe_event_based_task`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'event_based_task_id' in params:
            path_params['eventBasedTaskID'] = params['event_based_task_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/eventbasedtasks/{eventBasedTaskID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventBasedTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_event_based_tasks(self, api_version, **kwargs):  # noqa: E501
        """List Event Based Tasks  # noqa: E501

        Lists all event based tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_event_based_tasks(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: EventBasedTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_event_based_tasks_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_event_based_tasks_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_event_based_tasks_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List Event Based Tasks  # noqa: E501

        Lists all event based tasks.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_event_based_tasks_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :return: EventBasedTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_event_based_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_event_based_tasks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/eventbasedtasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventBasedTasks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_event_based_task(self, event_based_task_id, event_based_task, api_version, **kwargs):  # noqa: E501
        """Modify an Event Based Task  # noqa: E501

        Modify an event based task by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_event_based_task(event_based_task_id, event_based_task, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int event_based_task_id: The ID number of the event based task to modify. (required)
        :param EventBasedTask event_based_task: The settings of the event based task to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: EventBasedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_event_based_task_with_http_info(event_based_task_id, event_based_task, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_event_based_task_with_http_info(event_based_task_id, event_based_task, api_version, **kwargs)  # noqa: E501
            return data

    def modify_event_based_task_with_http_info(self, event_based_task_id, event_based_task, api_version, **kwargs):  # noqa: E501
        """Modify an Event Based Task  # noqa: E501

        Modify an event based task by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_event_based_task_with_http_info(event_based_task_id, event_based_task, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int event_based_task_id: The ID number of the event based task to modify. (required)
        :param EventBasedTask event_based_task: The settings of the event based task to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :return: EventBasedTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['event_based_task_id', 'event_based_task', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_event_based_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'event_based_task_id' is set
        if ('event_based_task_id' not in params or
                params['event_based_task_id'] is None):
            raise ValueError("Missing the required parameter `event_based_task_id` when calling `modify_event_based_task`")  # noqa: E501
        # verify the required parameter 'event_based_task' is set
        if ('event_based_task' not in params or
                params['event_based_task'] is None):
            raise ValueError("Missing the required parameter `event_based_task` when calling `modify_event_based_task`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_event_based_task`")  # noqa: E501

        if 'event_based_task_id' in params and not re.search('\\d+', str(params['event_based_task_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `event_based_task_id` when calling `modify_event_based_task`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'event_based_task_id' in params:
            path_params['eventBasedTaskID'] = params['event_based_task_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'event_based_task' in params:
            body_params = params['event_based_task']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/eventbasedtasks/{eventBasedTaskID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventBasedTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_event_based_tasks(self, api_version, **kwargs):  # noqa: E501
        """Search Event Based Tasks  # noqa: E501

        Search for event based tasks using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_event_based_tasks(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: EventBasedTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_event_based_tasks_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_event_based_tasks_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_event_based_tasks_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search Event Based Tasks  # noqa: E501

        Search for event based tasks using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_event_based_tasks_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :return: EventBasedTasks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'search_filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_event_based_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_event_based_tasks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_filter' in params:
            body_params = params['search_filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/eventbasedtasks/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventBasedTasks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
