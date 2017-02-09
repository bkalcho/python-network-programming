# Author: Bojan G. Kalicanin
# Date: 09-Feb-2017
# Description: Run simple webserver

from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import os

os.chdir("Exercises")
serv = HTTPServer(("", 8080), SimpleHTTPRequestHandler)
serv.serve_forever()
