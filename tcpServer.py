# Author: Bojan G. Kalicanin
# Date: 03-Feb-2017
# Description: Simple TCP Server

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9000))
s.listen(5)
while True:
    c, a = s.accept()
    print("Received connection from", a)
    c.send("Hello {0:s}\n".format(a[0]).encode())
    c.close
