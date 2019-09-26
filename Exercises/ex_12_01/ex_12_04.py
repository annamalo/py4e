# BeautifulSoup

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


# Count all of the paragraph tags and print the count of tags
count = 0
tags = soup('p')
for tag in tags:
    count = count + 1
print(count)

# Code: http://www.py4e.com/code3/urllinks.py
