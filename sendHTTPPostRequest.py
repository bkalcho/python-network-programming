# Author: Bojan G. Kalicanin
# Date: 11-Feb-2017
# Description: Send XML data using POST method via HTTP protocol.

import http.client

# Define variables
host = "localhost"
port = "8080"
http_method = "POST"
service_url = ""
filename = ""

try:
    with open(filename, 'r') as f_obj:
        body = f_obj.read()
    headers = {"Content-type": "application/xml"}
    connection = http.client.HTTPConnection(host, port)
    connection.connect()
    connection.request(http_method, service_url, body, headers)
except FileNotFoundError as fe:
    print("File '{0:s}' was not found ({1:d}): {2:s}".format(fe.filename,
        fe.errno, fe.strerror))
except NameError as e:
    print("Variable {0} has not been defined".format(e.args[0].split()[1]))
else:
    response = connection.getresponse()
    # Print response status
    print(response.status)
    # Print whole response
    print(response.read())
    connection.close()
