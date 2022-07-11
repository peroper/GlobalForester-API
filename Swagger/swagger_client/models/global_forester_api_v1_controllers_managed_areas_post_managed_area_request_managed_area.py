# coding: utf-8

"""
    Global Forester API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea(object):
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
        'name': 'str',
        'geometry': 'GeoJSONNetGeometryPolygon'
    }

    attribute_map = {
        'name': 'name',
        'geometry': 'geometry'
    }

    def __init__(self, name=None, geometry=None):  # noqa: E501
        """GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._geometry = None
        self.discriminator = None
        self.name = name
        self.geometry = geometry

    @property
    def name(self):
        """Gets the name of this GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.  # noqa: E501


        :return: The name of this GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.


        :param name: The name of this GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def geometry(self):
        """Gets the geometry of this GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.  # noqa: E501


        :return: The geometry of this GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.  # noqa: E501
        :rtype: GeoJSONNetGeometryPolygon
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.


        :param geometry: The geometry of this GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea.  # noqa: E501
        :type: GeoJSONNetGeometryPolygon
        """
        if geometry is None:
            raise ValueError("Invalid value for `geometry`, must not be `None`")  # noqa: E501

        self._geometry = geometry

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
        if issubclass(GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea, dict):
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
        if not isinstance(other, GlobalForesterApiV1ControllersManagedAreasPostManagedAreaRequestManagedArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
