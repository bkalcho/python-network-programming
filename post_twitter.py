# Author: Bojan G. Kalicanin
# Date: 05-Feb-2017
# Description: Write a function that posts an update message to Twitter.

import urllib.request
import urllib.parse

def update(username, password, status):
    # Build an URL Opener
    auth = urllib.request.HTTPBasicAuthHandler()
    auth.add_password("Twitter API", "http://twitter.com", username, password)
    opener = urllib.request.build_opener(auth)

    # Post message to Twitter
    fields = {'status': status}
    params = urllib.parse.urlencode(fields)
    req = urllib.request.Request("http://twitter.com/statuses/update.json?", params.encode())
    u = opener.open(req)
    resp = u.read()
    return resp.decode()

r = update('pythonclass', 'example', 'hello all!')
print(r)
