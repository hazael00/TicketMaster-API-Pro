# coding: utf-8

"""
    Ticketmaster Discovery API

    Swagger spec based on Ticketmaster Discovery API

    OpenAPI spec version: 1.0.0
    Contact: git@edward.sh
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "picketer"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Ticketmaster Discovery API",
    author_email="git@edward.sh",
    url="https://github.com/arcward/ticketpy",
    keywords=["Swagger", "Ticketmaster Discovery API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Swagger spec based on Ticketmaster Discovery API
    """
)
