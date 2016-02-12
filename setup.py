#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Pure-Python-GeoIP-Library',
    version='0.2',
    description='''
        Library to perform lookups in Maxmind GeoIP, designed specifically for
        use with Google App Engine.
    ''',
    url='https://github.com/dw/python-geoip',
    py_modules=['pygeoip']
)
