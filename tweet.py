# Author: Bojan G. Kalicanin
# Date: 04-Feb-2017
# Description: Write a function that accepts as input a subject string
# and maximum number of search results and submits a search request to
# Twitter. Have the function return the raw output.

import urllib.parse
import urllib.request

def tweets(subject, nresults):
    """Return search results on the tweet subjects."""
    fields = {'q': subject, 'rpp': nresults}
    params = urllib.parse.urlencode(fields)
    u = urllib.request.urlopen("https://api.twitter.com/1.1/search/tweets.json?"+params)
    response = u.read()
    return response.decode()
