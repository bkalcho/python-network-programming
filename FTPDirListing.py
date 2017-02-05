# Author: Bojan G. Kalicanin
# Date: 05-Feb-2017
# Description: Capture a directory listing from the FTP server.

import ftplib

f = ftplib.FTP("ftp.gnu.org", "anonymous", "dave@dabeaz.com")
files = []
f.retrlines("LIST", files.append)
print("Length of the directory listing: " + str(len(files)))
print("First file in the list: " + files[0])
