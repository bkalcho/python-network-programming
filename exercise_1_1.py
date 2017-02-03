# Author: Bojan G. Kalicanin
# Date: 03-Feb-2017
# Description: The HTTP protocol used by the web is based on TCP.
# Experiment with the protocol by manually connecting to a web server,
# issuing a request, and reading the response.
# Socket - In programming is abstraction of the network code. It is a
# communication endpoint.

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))                   # Connect to a server
s.send("GET /index.html HTTP/1.0\r\n\r\n".encode()) # Send data to a server
chunks = []
while True:
    chunk = s.recv(16384)                           # Read data in chunks
    if not chunk:
        break
    chunks.append(chunk.decode())
s.close()
response = "".join(chunks)                          # Using join is faster than using string concatenation (+)
print(response)
