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


class Sales(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, public=None, presales=None):
        """
        Sales - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'public': 'PublicDate',
            'presales': 'list[PresaleDate]'
        }

        self.attribute_map = {
            'public': 'public',
            'presales': 'presales'
        }

        self._public = public
        self._presales = presales

    @property
    def public(self):
        """
        Gets the public of this Sales.

        :return: The public of this Sales.
        :rtype: PublicDate
        """
        return self._public

    @public.setter
    def public(self, public):
        """
        Sets the public of this Sales.

        :param public: The public of this Sales.
        :type: PublicDate
        """

        self._public = public

    @property
    def presales(self):
        """
        Gets the presales of this Sales.

        :return: The presales of this Sales.
        :rtype: list[PresaleDate]
        """
        return self._presales

    @presales.setter
    def presales(self, presales):
        """
        Sets the presales of this Sales.

        :param presales: The presales of this Sales.
        :type: list[PresaleDate]
        """

        self._presales = presales

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
        if not isinstance(other, Sales):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
