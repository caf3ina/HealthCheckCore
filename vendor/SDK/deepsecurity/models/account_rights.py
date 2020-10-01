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


class AccountRights(object):
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
        'can_delete_accounts': 'bool',
        'can_update_accounts': 'bool',
        'can_view_account_billing': 'bool'
    }

    attribute_map = {
        'can_delete_accounts': 'canDeleteAccounts',
        'can_update_accounts': 'canUpdateAccounts',
        'can_view_account_billing': 'canViewAccountBilling'
    }

    def __init__(self, can_delete_accounts=None, can_update_accounts=None, can_view_account_billing=None):  # noqa: E501
        """AccountRights - a model defined in Swagger"""  # noqa: E501

        self._can_delete_accounts = None
        self._can_update_accounts = None
        self._can_view_account_billing = None
        self.discriminator = None

        if can_delete_accounts is not None:
            self.can_delete_accounts = can_delete_accounts
        if can_update_accounts is not None:
            self.can_update_accounts = can_update_accounts
        if can_view_account_billing is not None:
            self.can_view_account_billing = can_view_account_billing

    @property
    def can_delete_accounts(self):
        """Gets the can_delete_accounts of this AccountRights.  # noqa: E501

        Right to delete accounts.  # noqa: E501

        :return: The can_delete_accounts of this AccountRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_accounts

    @can_delete_accounts.setter
    def can_delete_accounts(self, can_delete_accounts):
        """Sets the can_delete_accounts of this AccountRights.

        Right to delete accounts.  # noqa: E501

        :param can_delete_accounts: The can_delete_accounts of this AccountRights.  # noqa: E501
        :type: bool
        """

        self._can_delete_accounts = can_delete_accounts

    @property
    def can_update_accounts(self):
        """Gets the can_update_accounts of this AccountRights.  # noqa: E501

        Right to update accounts.  # noqa: E501

        :return: The can_update_accounts of this AccountRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_update_accounts

    @can_update_accounts.setter
    def can_update_accounts(self, can_update_accounts):
        """Sets the can_update_accounts of this AccountRights.

        Right to update accounts.  # noqa: E501

        :param can_update_accounts: The can_update_accounts of this AccountRights.  # noqa: E501
        :type: bool
        """

        self._can_update_accounts = can_update_accounts

    @property
    def can_view_account_billing(self):
        """Gets the can_view_account_billing of this AccountRights.  # noqa: E501

        Right to view account billing.  # noqa: E501

        :return: The can_view_account_billing of this AccountRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_view_account_billing

    @can_view_account_billing.setter
    def can_view_account_billing(self, can_view_account_billing):
        """Sets the can_view_account_billing of this AccountRights.

        Right to view account billing.  # noqa: E501

        :param can_view_account_billing: The can_view_account_billing of this AccountRights.  # noqa: E501
        :type: bool
        """

        self._can_view_account_billing = can_view_account_billing

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
        if issubclass(AccountRights, dict):
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
        if not isinstance(other, AccountRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

