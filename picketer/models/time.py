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


class Time(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, chronology=None, millis_of_second=None, millis_of_day=None, second_of_minute=None, minute_of_hour=None, hour_of_day=None, no_specific_time=None, local_date=None, local_time=None, time_tba=None, values=None, field_types=None, fields=None):
        """
        Time - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'chronology': 'Chronology',
            'millis_of_second': 'int',
            'millis_of_day': 'int',
            'second_of_minute': 'int',
            'minute_of_hour': 'int',
            'hour_of_day': 'int',
            'no_specific_time': 'bool',
            'local_date': 'str',
            'local_time': 'Time',
            'time_tba': 'bool',
            'values': 'list[TimeValue]',
            'field_types': 'list[FieldType]',
            'fields': 'list[Field]'
        }

        self.attribute_map = {
            'chronology': 'chronology',
            'millis_of_second': 'millisOfSecond',
            'millis_of_day': 'millisOfDay',
            'second_of_minute': 'secondOfMinute',
            'minute_of_hour': 'minuteOfHour',
            'hour_of_day': 'hourOfDay',
            'no_specific_time': 'noSpecificTime',
            'local_date': 'localDate',
            'local_time': 'localTime',
            'time_tba': 'timeTBA',
            'values': 'values',
            'field_types': 'fieldTypes',
            'fields': 'fields'
        }

        self._chronology = chronology
        self._millis_of_second = millis_of_second
        self._millis_of_day = millis_of_day
        self._second_of_minute = second_of_minute
        self._minute_of_hour = minute_of_hour
        self._hour_of_day = hour_of_day
        self._no_specific_time = no_specific_time
        self._local_date = local_date
        self._local_time = local_time
        self._time_tba = time_tba
        self._values = values
        self._field_types = field_types
        self._fields = fields

    @property
    def chronology(self):
        """
        Gets the chronology of this Time.

        :return: The chronology of this Time.
        :rtype: Chronology
        """
        return self._chronology

    @chronology.setter
    def chronology(self, chronology):
        """
        Sets the chronology of this Time.

        :param chronology: The chronology of this Time.
        :type: Chronology
        """

        self._chronology = chronology

    @property
    def millis_of_second(self):
        """
        Gets the millis_of_second of this Time.

        :return: The millis_of_second of this Time.
        :rtype: int
        """
        return self._millis_of_second

    @millis_of_second.setter
    def millis_of_second(self, millis_of_second):
        """
        Sets the millis_of_second of this Time.

        :param millis_of_second: The millis_of_second of this Time.
        :type: int
        """

        self._millis_of_second = millis_of_second

    @property
    def millis_of_day(self):
        """
        Gets the millis_of_day of this Time.

        :return: The millis_of_day of this Time.
        :rtype: int
        """
        return self._millis_of_day

    @millis_of_day.setter
    def millis_of_day(self, millis_of_day):
        """
        Sets the millis_of_day of this Time.

        :param millis_of_day: The millis_of_day of this Time.
        :type: int
        """

        self._millis_of_day = millis_of_day

    @property
    def second_of_minute(self):
        """
        Gets the second_of_minute of this Time.

        :return: The second_of_minute of this Time.
        :rtype: int
        """
        return self._second_of_minute

    @second_of_minute.setter
    def second_of_minute(self, second_of_minute):
        """
        Sets the second_of_minute of this Time.

        :param second_of_minute: The second_of_minute of this Time.
        :type: int
        """

        self._second_of_minute = second_of_minute

    @property
    def minute_of_hour(self):
        """
        Gets the minute_of_hour of this Time.

        :return: The minute_of_hour of this Time.
        :rtype: int
        """
        return self._minute_of_hour

    @minute_of_hour.setter
    def minute_of_hour(self, minute_of_hour):
        """
        Sets the minute_of_hour of this Time.

        :param minute_of_hour: The minute_of_hour of this Time.
        :type: int
        """

        self._minute_of_hour = minute_of_hour

    @property
    def hour_of_day(self):
        """
        Gets the hour_of_day of this Time.

        :return: The hour_of_day of this Time.
        :rtype: int
        """
        return self._hour_of_day

    @hour_of_day.setter
    def hour_of_day(self, hour_of_day):
        """
        Sets the hour_of_day of this Time.

        :param hour_of_day: The hour_of_day of this Time.
        :type: int
        """

        self._hour_of_day = hour_of_day

    @property
    def no_specific_time(self):
        """
        Gets the no_specific_time of this Time.

        :return: The no_specific_time of this Time.
        :rtype: bool
        """
        return self._no_specific_time

    @no_specific_time.setter
    def no_specific_time(self, no_specific_time):
        """
        Sets the no_specific_time of this Time.

        :param no_specific_time: The no_specific_time of this Time.
        :type: bool
        """

        self._no_specific_time = no_specific_time

    @property
    def local_date(self):
        """
        Gets the local_date of this Time.

        :return: The local_date of this Time.
        :rtype: str
        """
        return self._local_date

    @local_date.setter
    def local_date(self, local_date):
        """
        Sets the local_date of this Time.

        :param local_date: The local_date of this Time.
        :type: str
        """

        self._local_date = local_date

    @property
    def local_time(self):
        """
        Gets the local_time of this Time.

        :return: The local_time of this Time.
        :rtype: Time
        """
        return self._local_time

    @local_time.setter
    def local_time(self, local_time):
        """
        Sets the local_time of this Time.

        :param local_time: The local_time of this Time.
        :type: Time
        """

        self._local_time = local_time

    @property
    def time_tba(self):
        """
        Gets the time_tba of this Time.

        :return: The time_tba of this Time.
        :rtype: bool
        """
        return self._time_tba

    @time_tba.setter
    def time_tba(self, time_tba):
        """
        Sets the time_tba of this Time.

        :param time_tba: The time_tba of this Time.
        :type: bool
        """

        self._time_tba = time_tba

    @property
    def values(self):
        """
        Gets the values of this Time.

        :return: The values of this Time.
        :rtype: list[TimeValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this Time.

        :param values: The values of this Time.
        :type: list[TimeValue]
        """

        self._values = values

    @property
    def field_types(self):
        """
        Gets the field_types of this Time.

        :return: The field_types of this Time.
        :rtype: list[FieldType]
        """
        return self._field_types

    @field_types.setter
    def field_types(self, field_types):
        """
        Sets the field_types of this Time.

        :param field_types: The field_types of this Time.
        :type: list[FieldType]
        """

        self._field_types = field_types

    @property
    def fields(self):
        """
        Gets the fields of this Time.

        :return: The fields of this Time.
        :rtype: list[Field]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this Time.

        :param fields: The fields of this Time.
        :type: list[Field]
        """

        self._fields = fields

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
        if not isinstance(other, Time):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
