# Author: Bojan G. Kalicanin
# Date: 05-Feb-2017
# Description:

import http.client

conn = http.client.HTTPConnection("www.python.org", 80)
conn.putrequest("GET", "/index.html")
conn.putheader("User-agent", "pythonclass")
conn.endheaders()
r = conn.getresponse()
data = r.read()
conn.close()
print(data.decode())
