This is a native GeoIP.dat reader for Python. It allows the use of GeoIP without an external service, or Datastore, from Google App Engine.

Cold start takes about 5ms to open the database. Warm lookups are so fast they can't reliably be measured (an urlfetch will cost ~100 ms, a single Datastore get ~20ms).

*Note that the returned CIDR prefixes aren't reliable. Suggest not using them for abuse prevention!*

*The database is cached in memory. This adds 1.1mb to your interpreter size!*

----

== Example ==

Ensure `GeoIP.dat` ([http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz download]) and `pygeoip.py` ([http://python-geoip.googlecode.com/hg/pygeoip.py download]) are in your !AppEngine project directory.

Simple example:

{{{
from google.appengine.ext import webapp

import pygeoip


# Load the database once and store it globally in interpreter memory.
GEOIP = pygeoip.Database('GeoIP.dat')


class LookupHandler(webapp.RequestHandler):
    def get(self):
        info = GEOIP.lookup(self.request.remote_addr)
        if not info.country:
            msg = 'Could not locate country for ' + self.request.remote_addr
        else:
            msg = 'Country for %s is %s' % (self.request.remote_addr, info.country)

        self.response.out.write(msg)
}}}