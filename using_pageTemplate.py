# Author: Bojan G. Kalicanin
# Date: 08-Feb-2017
# Description: Generate static content.

from string import Template

# Load page template into a Template string.
f_obj = open("exercisetemplate.html")
data = f_obj.read()
pagetemp = Template(data)
print(pagetemp)

# Read body content into a string 'body'.
f_body = open("exercise.ht")
body = f_body.read()
print(body)

# Render an HTML page.
f = open("exercise.html", 'w')
f.write(pagetemp.substitute(body=body, section=4, problem=2))
f.close()

# Open HTML page in web browser.
import webbrowser
webbrowser.open("exercise.html")
