# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = input('Enter Count : ')
cval = int(count)
position = input('Enter Position : ')
pval = int(position)
url = input('Enter - ')
counter = 0
while counter<cval :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    temp = 1
    for tag in tags :

            if temp == pval :
                print(tag.get('href', None))
                url = tag.get('href', None)
                break
            temp = temp + 1
    counter = counter + 1
