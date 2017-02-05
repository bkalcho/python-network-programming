# Author: Bojan G. Kalicanin
# Date: 05-Feb-2017
# Description: Issue a HEAD request to http://www.python.org/index.html

import http.client

con = http.client.HTTPConnection("www.python.org", 80)
con.putrequest("HEAD", "/index.html")
con.putheader("User-agent", "pythonclass")
con.endheaders()
r = con.getresponse()
print(r.status)
print(r.reason)
print(r.getheaders())
con.close()
