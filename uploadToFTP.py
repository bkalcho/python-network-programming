# Author: Bojan G. Kalicanin
# Date: 05-Feb-2017
# Description: Upload file to FTP server.

import ftplib

host = "ftp.foo.com"
username = "dave"
password = "1235"
filename = "somefile.dat"

ftp_serv = ftplib.FTP(host, username, password)

# Open the file you want to send
f = open(filename, "rb")

# Send it to the FTP server
resp = ftp_serv.storbinary("STOR " + filename, f)

# Close the connection
ftp_serv.close()
