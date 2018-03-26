#!/usr/bin/env python

"""Quick and dirty smoke test that looks up IPs using the Python library and
command line tool, printing any mismatches."""

import os
import random
import re
import sys

from socket import inet_aton
from socket import inet_ntoa

import pygeoip


MATCH_PATTERN = re.compile('GeoIP Country Edition: ([A-Z0-9][0-9A-Z]),.*')
TRIES = 20000


def make_ip():
    """Return a random IP address as a string."""
    return inet_ntoa(inet_aton(str(random.randint(0, 0xffffffff))))

def clookup(ip):
    """Get the country code for an IP address using the 'geoiplookup'
    utility."""
    with os.popen('geoiplookup ' + ip) as fp:
        match = MATCH_PATTERN.match(fp.read())
    if match:
        return match.group(1)

def main():
    dbfile = 'GeoIP.dat'
    if len(sys.argv) > 1:
        dbfile = sys.argv[1]

    db = pygeoip.Database(dbfile)

    for ip in (make_ip() for x in xrange(TRIES)):
        cc1 = clookup(ip)
        cc2 = db.lookup(ip).country

        if cc1 != cc2:
            print
            print 'mismatch', ip, cc1, cc2

if __name__ == '__main__':
    main()
