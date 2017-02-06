# Author: Bojan G. Kalicanin
# Date: 06-Feb-2017
# Description: Parse example HTML document.

import html.parser

class GatherLinks(html.parser.HTMLParser):
    """Catch links from HTML document."""

    def __init__(self):
        super().__init__()
        self.links = []
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for name, value in attrs:
                if name == 'href':
                    self.links.append(value)

parser = GatherLinks()
import urllib.request
u = urllib.request.urlopen("http://www.python.org")
data = u.read()
parser.feed(data.decode())
for link in parser.links:
    print(link)
