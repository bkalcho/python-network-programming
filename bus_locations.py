# Author: Bojan G. Kalicanin
# Date: 07-Feb-2017
# Description: write a function bus_locations(f) that accepts an open
# file as input and prints lines of comma separated values id, route,
# direction, latitude, longitude corresponding to parsed bus location
# data.

import xml.etree.ElementTree

def bus_locations(f):
    """Return bus locations data."""

    parser = xml.etree.ElementTree.iterparse(f, ('start', 'end'))
    for event, elem in parser:
        if event == 'start' and elem.tag == 'buses':
            buses = elem
        elif event == 'end' and elem.tag == 'bus':
            print("{0:s},{1:s},{2:s},{3:s},{4:s}".format(
                elem.findtext('id'),
                elem.findtext('route'),
                elem.findtext('direction'),
                elem.findtext('latitude'),
                elem.findtext('longitude'))
                )
            # Discard the bus element from the parent
            buses.remove(elem)

if __name__ == '__main__':
    f = open("allroutes.xml", 'r')
    bus_locations(f)
