# Author: Bojan G. Kalicanin
# Date: 05-Feb-2017
# Description: Get all links from webpage.\

import html.parser

class GatherLinks(html.parser.HTMLParser):
    """Get links from webpage."""

    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.links.append(value)

import urllib.request
u = urllib.request.urlopen("http://www.python.org")
data = u.read()
parser = GatherLinks()
parser.feed(data.decode())
for l in parser.links:
    print(l)
