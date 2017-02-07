# Author: Bojan G. Kalicanin
# Date: 07-Feb-2017
# Description: Wrote a function that returns bus predictions by parsing
# XML data using ElementTree module.

import xml.etree.ElementTree
import urllib.parse
import urllib.request

def bus_prediction(route, stop):
    """Retrive XML data with prediction about waiting time."""
    fields = {'stop': stop, 'route': route}
    params = urllib.parse.urlencode(fields)
    u = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getStopPredictions.jsp?"+params)
    resp = u.read()
    data = resp.decode()
    doc = xml.etree.ElementTree.parse("example.xml")
    predictions = []
    for pre in doc.findall("pre"):
        pt = pre.findtext("pt")
        predictions.append(pt)
    
    return predictions


prediction_times = bus_prediction("6", "5037")
print(prediction_times)
