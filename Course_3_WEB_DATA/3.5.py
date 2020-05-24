import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter - : ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
#comment is a list
sum = 0
counts = tree.findall('.//count')
print('User count:', len(counts))
for item in counts :
    sum = sum + int(item.text)
print(sum)
