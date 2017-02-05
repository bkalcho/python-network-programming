# Author: Bojan G. Kalicanin
# Date: 04-Feb-2017
# Description: Write a function that accepts as input a subject string
# and maximum number of search results and submits a search request to
# Twitter. Have the function return the raw output.

import urllib.parse
import urllib.request

def tweets(subject, nresults):
    """Return search results on the tweet subjects."""
    auth = urllib.request.HTTPBasicAuthHandler()
    password = 'example'
    auth.add_password("Twitter API", "https://twitter.com", "pythonclass", password)
    opener = urllib.request.build_opener(auth)

    fields = {'q': subject, 'rpp': nresults}
    params = urllib.parse.urlencode(fields)
    request = urllib.request.Request("https://api.twitter.com/1.1/search/tweets.json?"+params)
    u = opener.open(request)
    response = u.read()
    return response.decode()

if __name__ == '__main__':
    tweets('python', 25)
