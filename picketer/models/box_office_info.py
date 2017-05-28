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


class BoxOfficeInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phone_number_detail=None, open_hours_detail=None, accepted_payment_detail=None, will_call_detail=None):
        """
        BoxOfficeInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phone_number_detail': 'str',
            'open_hours_detail': 'str',
            'accepted_payment_detail': 'str',
            'will_call_detail': 'str'
        }

        self.attribute_map = {
            'phone_number_detail': 'phoneNumberDetail',
            'open_hours_detail': 'openHoursDetail',
            'accepted_payment_detail': 'acceptedPaymentDetail',
            'will_call_detail': 'willCallDetail'
        }

        self._phone_number_detail = phone_number_detail
        self._open_hours_detail = open_hours_detail
        self._accepted_payment_detail = accepted_payment_detail
        self._will_call_detail = will_call_detail

    @property
    def phone_number_detail(self):
        """
        Gets the phone_number_detail of this BoxOfficeInfo.

        :return: The phone_number_detail of this BoxOfficeInfo.
        :rtype: str
        """
        return self._phone_number_detail

    @phone_number_detail.setter
    def phone_number_detail(self, phone_number_detail):
        """
        Sets the phone_number_detail of this BoxOfficeInfo.

        :param phone_number_detail: The phone_number_detail of this BoxOfficeInfo.
        :type: str
        """

        self._phone_number_detail = phone_number_detail

    @property
    def open_hours_detail(self):
        """
        Gets the open_hours_detail of this BoxOfficeInfo.

        :return: The open_hours_detail of this BoxOfficeInfo.
        :rtype: str
        """
        return self._open_hours_detail

    @open_hours_detail.setter
    def open_hours_detail(self, open_hours_detail):
        """
        Sets the open_hours_detail of this BoxOfficeInfo.

        :param open_hours_detail: The open_hours_detail of this BoxOfficeInfo.
        :type: str
        """

        self._open_hours_detail = open_hours_detail

    @property
    def accepted_payment_detail(self):
        """
        Gets the accepted_payment_detail of this BoxOfficeInfo.

        :return: The accepted_payment_detail of this BoxOfficeInfo.
        :rtype: str
        """
        return self._accepted_payment_detail

    @accepted_payment_detail.setter
    def accepted_payment_detail(self, accepted_payment_detail):
        """
        Sets the accepted_payment_detail of this BoxOfficeInfo.

        :param accepted_payment_detail: The accepted_payment_detail of this BoxOfficeInfo.
        :type: str
        """

        self._accepted_payment_detail = accepted_payment_detail

    @property
    def will_call_detail(self):
        """
        Gets the will_call_detail of this BoxOfficeInfo.

        :return: The will_call_detail of this BoxOfficeInfo.
        :rtype: str
        """
        return self._will_call_detail

    @will_call_detail.setter
    def will_call_detail(self, will_call_detail):
        """
        Sets the will_call_detail of this BoxOfficeInfo.

        :param will_call_detail: The will_call_detail of this BoxOfficeInfo.
        :type: str
        """

        self._will_call_detail = will_call_detail

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
        if not isinstance(other, BoxOfficeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
