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


class Classification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, primary=None, segment=None, genre=None, sub_genre=None, type=None, sub_type=None, links=None):
        """
        Classification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'primary': 'bool',
            'segment': 'Segment',
            'genre': 'Genre',
            'sub_genre': 'SubGenre',
            'type': 'ClassificationType',
            'sub_type': 'ClassificationType',
            'links': 'Links'
        }

        self.attribute_map = {
            'primary': 'primary',
            'segment': 'segment',
            'genre': 'genre',
            'sub_genre': 'subGenre',
            'type': 'type',
            'sub_type': 'subType',
            'links': '_links'
        }

        self._primary = primary
        self._segment = segment
        self._genre = genre
        self._sub_genre = sub_genre
        self._type = type
        self._sub_type = sub_type
        self._links = links

    @property
    def primary(self):
        """
        Gets the primary of this Classification.

        :return: The primary of this Classification.
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """
        Sets the primary of this Classification.

        :param primary: The primary of this Classification.
        :type: bool
        """

        self._primary = primary

    @property
    def segment(self):
        """
        Gets the segment of this Classification.

        :return: The segment of this Classification.
        :rtype: Segment
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """
        Sets the segment of this Classification.

        :param segment: The segment of this Classification.
        :type: Segment
        """

        self._segment = segment

    @property
    def genre(self):
        """
        Gets the genre of this Classification.

        :return: The genre of this Classification.
        :rtype: Genre
        """
        return self._genre

    @genre.setter
    def genre(self, genre):
        """
        Sets the genre of this Classification.

        :param genre: The genre of this Classification.
        :type: Genre
        """

        self._genre = genre

    @property
    def sub_genre(self):
        """
        Gets the sub_genre of this Classification.

        :return: The sub_genre of this Classification.
        :rtype: SubGenre
        """
        return self._sub_genre

    @sub_genre.setter
    def sub_genre(self, sub_genre):
        """
        Sets the sub_genre of this Classification.

        :param sub_genre: The sub_genre of this Classification.
        :type: SubGenre
        """

        self._sub_genre = sub_genre

    @property
    def type(self):
        """
        Gets the type of this Classification.

        :return: The type of this Classification.
        :rtype: ClassificationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Classification.

        :param type: The type of this Classification.
        :type: ClassificationType
        """

        self._type = type

    @property
    def sub_type(self):
        """
        Gets the sub_type of this Classification.

        :return: The sub_type of this Classification.
        :rtype: ClassificationType
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """
        Sets the sub_type of this Classification.

        :param sub_type: The sub_type of this Classification.
        :type: ClassificationType
        """

        self._sub_type = sub_type

    @property
    def links(self):
        """
        Gets the links of this Classification.

        :return: The links of this Classification.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Classification.

        :param links: The links of this Classification.
        :type: Links
        """

        self._links = links

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
        if not isinstance(other, Classification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other