# Author: Bojan G. Kalicanin
# Date: 04-Feb-2017
# Description: Prediction of how long you'll have to wait for a bus to
# arrive at a particular stop and route.

import xml.sax
import urllib.parse
import urllib.request

class MyHandler(xml.sax.ContentHandler):
    """Parse XML document for bus arrival prediction time."""

    def __init__(self):
        super().__init__()
        # Use predictions list to store all prediction times
        self.predictions = []
        # Use pt to store catched prediction time
        self.pt = None
    
    def startElement(self, name, attrs):
        """If element name equals 'pt', prepare self.pt to collect text."""
        if name == 'pt':
            self.pt = ""

    def characters(self, data):
        """Collect text if self.pt is not None."""
        if self.pt is not None:
            self.pt += data
    
    def endElement(self, name):
        """If encounter endding 'pt', append collected text."""
        if name == 'pt':
            self.predictions.append(self.pt)
            self.pt = None


def bus_prediction(route, stop):
    """Retrive XML data with prediction about waiting time."""
    fields = {'stop': stop, 'route': route}
    params = urllib.parse.urlencode(fields)
    u = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getStopPredictions.jsp?"+params)
    resp = u.read()
    hand = MyHandler()
    data = resp.decode()
    xml.sax.parse(data, hand)
    return hand.predictions


prediction_times = bus_prediction("6", "5037")
print(prediction_times)
