# coding: utf-8

"""
    Ticketmaster Discovery API

    Swagger spec based on Ticketmaster Discovery API

    OpenAPI spec version: 1.0.0
    Contact: git@edward.sh
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PublicDate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, start_date_time=None, end_date_time=None, start_tbd=None):
        """
        PublicDate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'start_date_time': 'str',
            'end_date_time': 'str',
            'start_tbd': 'bool'
        }

        self.attribute_map = {
            'start_date_time': 'startDateTime',
            'end_date_time': 'endDateTime',
            'start_tbd': 'startTBD'
        }

        self._start_date_time = start_date_time
        self._end_date_time = end_date_time
        self._start_tbd = start_tbd

    @property
    def start_date_time(self):
        """
        Gets the start_date_time of this PublicDate.

        :return: The start_date_time of this PublicDate.
        :rtype: str
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """
        Sets the start_date_time of this PublicDate.

        :param start_date_time: The start_date_time of this PublicDate.
        :type: str
        """

        self._start_date_time = start_date_time

    @property
    def end_date_time(self):
        """
        Gets the end_date_time of this PublicDate.

        :return: The end_date_time of this PublicDate.
        :rtype: str
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """
        Sets the end_date_time of this PublicDate.

        :param end_date_time: The end_date_time of this PublicDate.
        :type: str
        """

        self._end_date_time = end_date_time

    @property
    def start_tbd(self):
        """
        Gets the start_tbd of this PublicDate.

        :return: The start_tbd of this PublicDate.
        :rtype: bool
        """
        return self._start_tbd

    @start_tbd.setter
    def start_tbd(self, start_tbd):
        """
        Sets the start_tbd of this PublicDate.

        :param start_tbd: The start_tbd of this PublicDate.
        :type: bool
        """

        self._start_tbd = start_tbd

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PublicDate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
