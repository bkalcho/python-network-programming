# Author: Bojan G. Kalicanin
# Date: 04-Feb-2017
# Description: Prediction of how long you'll have to wait for a bus to
# arrive at a particular stop and route.

import urllib.parse
import urllib.request

def bus_prediction(route, stop):
    """Retrive XML data with prediction about waiting time."""
    fields = {'stop': stop, 'route': route}
    params = urllib.parse.urlencode(fields)
    u = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getStopPredictions.jsp?"+params)
    resp = u.read()
    return resp.decode()
