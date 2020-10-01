# coding: utf-8

"""
    Trend Micro Deep Security API

    Copyright 2018 - 2020 Trend Micro Incorporated.<br/>Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 20.0.186
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from deepsecurity.models.daily_schedule_parameters import DailyScheduleParameters  # noqa: F401,E501
from deepsecurity.models.hourly_schedule_parameters import HourlyScheduleParameters  # noqa: F401,E501
from deepsecurity.models.monthly_schedule_parameters import MonthlyScheduleParameters  # noqa: F401,E501
from deepsecurity.models.once_only_schedule_parameters import OnceOnlyScheduleParameters  # noqa: F401,E501
from deepsecurity.models.weekly_schedule_parameters import WeeklyScheduleParameters  # noqa: F401,E501


class ScheduleDetails(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'time_zone': 'str',
        'recurrence_type': 'str',
        'recurrence_count': 'int',
        'hourly_schedule_parameters': 'HourlyScheduleParameters',
        'daily_schedule_parameters': 'DailyScheduleParameters',
        'weekly_schedule_parameters': 'WeeklyScheduleParameters',
        'monthly_schedule_parameters': 'MonthlyScheduleParameters',
        'once_only_schedule_parameters': 'OnceOnlyScheduleParameters'
    }

    attribute_map = {
        'time_zone': 'timeZone',
        'recurrence_type': 'recurrenceType',
        'recurrence_count': 'recurrenceCount',
        'hourly_schedule_parameters': 'hourlyScheduleParameters',
        'daily_schedule_parameters': 'dailyScheduleParameters',
        'weekly_schedule_parameters': 'weeklyScheduleParameters',
        'monthly_schedule_parameters': 'monthlyScheduleParameters',
        'once_only_schedule_parameters': 'onceOnlyScheduleParameters'
    }

    def __init__(self, time_zone=None, recurrence_type=None, recurrence_count=None, hourly_schedule_parameters=None, daily_schedule_parameters=None, weekly_schedule_parameters=None, monthly_schedule_parameters=None, once_only_schedule_parameters=None):  # noqa: E501
        """ScheduleDetails - a model defined in Swagger"""  # noqa: E501

        self._time_zone = None
        self._recurrence_type = None
        self._recurrence_count = None
        self._hourly_schedule_parameters = None
        self._daily_schedule_parameters = None
        self._weekly_schedule_parameters = None
        self._monthly_schedule_parameters = None
        self._once_only_schedule_parameters = None
        self.discriminator = None

        if time_zone is not None:
            self.time_zone = time_zone
        if recurrence_type is not None:
            self.recurrence_type = recurrence_type
        if recurrence_count is not None:
            self.recurrence_count = recurrence_count
        if hourly_schedule_parameters is not None:
            self.hourly_schedule_parameters = hourly_schedule_parameters
        if daily_schedule_parameters is not None:
            self.daily_schedule_parameters = daily_schedule_parameters
        if weekly_schedule_parameters is not None:
            self.weekly_schedule_parameters = weekly_schedule_parameters
        if monthly_schedule_parameters is not None:
            self.monthly_schedule_parameters = monthly_schedule_parameters
        if once_only_schedule_parameters is not None:
            self.once_only_schedule_parameters = once_only_schedule_parameters

    @property
    def time_zone(self):
        """Gets the time_zone of this ScheduleDetails.  # noqa: E501

        The timezone used to interpret the scheduled task schedule.  # noqa: E501

        :return: The time_zone of this ScheduleDetails.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this ScheduleDetails.

        The timezone used to interpret the scheduled task schedule.  # noqa: E501

        :param time_zone: The time_zone of this ScheduleDetails.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def recurrence_type(self):
        """Gets the recurrence_type of this ScheduleDetails.  # noqa: E501

        Recurrence type.  # noqa: E501

        :return: The recurrence_type of this ScheduleDetails.  # noqa: E501
        :rtype: str
        """
        return self._recurrence_type

    @recurrence_type.setter
    def recurrence_type(self, recurrence_type):
        """Sets the recurrence_type of this ScheduleDetails.

        Recurrence type.  # noqa: E501

        :param recurrence_type: The recurrence_type of this ScheduleDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "hourly", "daily", "weekly", "monthly"]  # noqa: E501
        if recurrence_type not in allowed_values:
            raise ValueError(
                "Invalid value for `recurrence_type` ({0}), must be one of {1}"  # noqa: E501
                .format(recurrence_type, allowed_values)
            )

        self._recurrence_type = recurrence_type

    @property
    def recurrence_count(self):
        """Gets the recurrence_count of this ScheduleDetails.  # noqa: E501

        Number of times the task should execute.  # noqa: E501

        :return: The recurrence_count of this ScheduleDetails.  # noqa: E501
        :rtype: int
        """
        return self._recurrence_count

    @recurrence_count.setter
    def recurrence_count(self, recurrence_count):
        """Sets the recurrence_count of this ScheduleDetails.

        Number of times the task should execute.  # noqa: E501

        :param recurrence_count: The recurrence_count of this ScheduleDetails.  # noqa: E501
        :type: int
        """

        self._recurrence_count = recurrence_count

    @property
    def hourly_schedule_parameters(self):
        """Gets the hourly_schedule_parameters of this ScheduleDetails.  # noqa: E501

        Details for an hourly schedule.  # noqa: E501

        :return: The hourly_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :rtype: HourlyScheduleParameters
        """
        return self._hourly_schedule_parameters

    @hourly_schedule_parameters.setter
    def hourly_schedule_parameters(self, hourly_schedule_parameters):
        """Sets the hourly_schedule_parameters of this ScheduleDetails.

        Details for an hourly schedule.  # noqa: E501

        :param hourly_schedule_parameters: The hourly_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :type: HourlyScheduleParameters
        """

        self._hourly_schedule_parameters = hourly_schedule_parameters

    @property
    def daily_schedule_parameters(self):
        """Gets the daily_schedule_parameters of this ScheduleDetails.  # noqa: E501

        Details for a daily schedule.  # noqa: E501

        :return: The daily_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :rtype: DailyScheduleParameters
        """
        return self._daily_schedule_parameters

    @daily_schedule_parameters.setter
    def daily_schedule_parameters(self, daily_schedule_parameters):
        """Sets the daily_schedule_parameters of this ScheduleDetails.

        Details for a daily schedule.  # noqa: E501

        :param daily_schedule_parameters: The daily_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :type: DailyScheduleParameters
        """

        self._daily_schedule_parameters = daily_schedule_parameters

    @property
    def weekly_schedule_parameters(self):
        """Gets the weekly_schedule_parameters of this ScheduleDetails.  # noqa: E501

        Details for a weekly schedule.  # noqa: E501

        :return: The weekly_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :rtype: WeeklyScheduleParameters
        """
        return self._weekly_schedule_parameters

    @weekly_schedule_parameters.setter
    def weekly_schedule_parameters(self, weekly_schedule_parameters):
        """Sets the weekly_schedule_parameters of this ScheduleDetails.

        Details for a weekly schedule.  # noqa: E501

        :param weekly_schedule_parameters: The weekly_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :type: WeeklyScheduleParameters
        """

        self._weekly_schedule_parameters = weekly_schedule_parameters

    @property
    def monthly_schedule_parameters(self):
        """Gets the monthly_schedule_parameters of this ScheduleDetails.  # noqa: E501

        Details for a monthly schedule.  # noqa: E501

        :return: The monthly_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :rtype: MonthlyScheduleParameters
        """
        return self._monthly_schedule_parameters

    @monthly_schedule_parameters.setter
    def monthly_schedule_parameters(self, monthly_schedule_parameters):
        """Sets the monthly_schedule_parameters of this ScheduleDetails.

        Details for a monthly schedule.  # noqa: E501

        :param monthly_schedule_parameters: The monthly_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :type: MonthlyScheduleParameters
        """

        self._monthly_schedule_parameters = monthly_schedule_parameters

    @property
    def once_only_schedule_parameters(self):
        """Gets the once_only_schedule_parameters of this ScheduleDetails.  # noqa: E501

        Details for a once only schedule.  # noqa: E501

        :return: The once_only_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :rtype: OnceOnlyScheduleParameters
        """
        return self._once_only_schedule_parameters

    @once_only_schedule_parameters.setter
    def once_only_schedule_parameters(self, once_only_schedule_parameters):
        """Sets the once_only_schedule_parameters of this ScheduleDetails.

        Details for a once only schedule.  # noqa: E501

        :param once_only_schedule_parameters: The once_only_schedule_parameters of this ScheduleDetails.  # noqa: E501
        :type: OnceOnlyScheduleParameters
        """

        self._once_only_schedule_parameters = once_only_schedule_parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ScheduleDetails, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduleDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

