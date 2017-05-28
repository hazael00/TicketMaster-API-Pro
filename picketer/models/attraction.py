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


class Attraction(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, type=None, url=None, locale=None, images=None, classifications=None, description=None, additional_info=None, external_links=None, test=None, links=None):
        """
        Attraction - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'url': 'str',
            'locale': 'str',
            'images': 'list[Image]',
            'classifications': 'list[Classification]',
            'description': 'str',
            'additional_info': 'str',
            'external_links': 'list[Link]',
            'test': 'bool',
            'links': 'Links'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'url': 'url',
            'locale': 'locale',
            'images': 'images',
            'classifications': 'classifications',
            'description': 'description',
            'additional_info': 'additionalInfo',
            'external_links': 'externalLinks',
            'test': 'test',
            'links': '_links'
        }

        self._id = id
        self._name = name
        self._type = type
        self._url = url
        self._locale = locale
        self._images = images
        self._classifications = classifications
        self._description = description
        self._additional_info = additional_info
        self._external_links = external_links
        self._test = test
        self._links = links

    @property
    def id(self):
        """
        Gets the id of this Attraction.

        :return: The id of this Attraction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Attraction.

        :param id: The id of this Attraction.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Attraction.

        :return: The name of this Attraction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Attraction.

        :param name: The name of this Attraction.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Attraction.

        :return: The type of this Attraction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Attraction.

        :param type: The type of this Attraction.
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """
        Gets the url of this Attraction.

        :return: The url of this Attraction.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Attraction.

        :param url: The url of this Attraction.
        :type: str
        """

        self._url = url

    @property
    def locale(self):
        """
        Gets the locale of this Attraction.

        :return: The locale of this Attraction.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """
        Sets the locale of this Attraction.

        :param locale: The locale of this Attraction.
        :type: str
        """

        self._locale = locale

    @property
    def images(self):
        """
        Gets the images of this Attraction.

        :return: The images of this Attraction.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Attraction.

        :param images: The images of this Attraction.
        :type: list[Image]
        """

        self._images = images

    @property
    def classifications(self):
        """
        Gets the classifications of this Attraction.

        :return: The classifications of this Attraction.
        :rtype: list[Classification]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """
        Sets the classifications of this Attraction.

        :param classifications: The classifications of this Attraction.
        :type: list[Classification]
        """

        self._classifications = classifications

    @property
    def description(self):
        """
        Gets the description of this Attraction.

        :return: The description of this Attraction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Attraction.

        :param description: The description of this Attraction.
        :type: str
        """

        self._description = description

    @property
    def additional_info(self):
        """
        Gets the additional_info of this Attraction.

        :return: The additional_info of this Attraction.
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """
        Sets the additional_info of this Attraction.

        :param additional_info: The additional_info of this Attraction.
        :type: str
        """

        self._additional_info = additional_info

    @property
    def external_links(self):
        """
        Gets the external_links of this Attraction.

        :return: The external_links of this Attraction.
        :rtype: list[Link]
        """
        return self._external_links

    @external_links.setter
    def external_links(self, external_links):
        """
        Sets the external_links of this Attraction.

        :param external_links: The external_links of this Attraction.
        :type: list[Link]
        """

        self._external_links = external_links

    @property
    def test(self):
        """
        Gets the test of this Attraction.

        :return: The test of this Attraction.
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """
        Sets the test of this Attraction.

        :param test: The test of this Attraction.
        :type: bool
        """

        self._test = test

    @property
    def links(self):
        """
        Gets the links of this Attraction.

        :return: The links of this Attraction.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this Attraction.

        :param links: The links of this Attraction.
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
        if not isinstance(other, Attraction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
