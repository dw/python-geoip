#!/usr/bin/env python

'''setuptools setup.py for CBMS.'''

from distutils.core import setup

setup(
    name='Pure Python GeoIP Library',
    version='0.1',
    description='''
        Library to perform lookups in Maxmind GeoIP, designed specifically for use with Google App Engine.
    ''',
    author='David Wilson',
    author_email='dw+geoip@botanicus.net',
    url='http://code.google.com/p/python-geoip/',
    download_url='http://python-geoip.googlecode.com/hg/pygeoip.py',
    py_modules=['pygeoip']
)
