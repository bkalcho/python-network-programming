# Author: Bojan G. Kalicanin
# Date: 03-Feb-2017
# Description: Create a network socket.
# Socket - In programming is abstraction of the network code. It is a
# communication endpoint.

import socket

s = socket.socket(AF_INET, SOCK_STREAM)
s.connect(("www.python.org", 80))       # Connect
s.send("GET /index.html HTTP/1.0\n\n")  # Send request
data = s.recv(10000)                    # Get response
s.close()
