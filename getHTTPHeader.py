# Author: Bojan G. Kalicanin
# Date: 05-Feb-2016
# Description: Get HTTP response

import http.client

c = http.client.HTTPConnection("www.python.org", 80)
c.putrequest("HEAD", "/tut/tut.html")
c.putheader("Someheader", "Somevalue")
c.endheaders()

r = c.getresponse()
data = r.read()
print(data.decode())
c.close()
