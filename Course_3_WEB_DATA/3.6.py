import urllib.request, urllib.parse, urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input("Enter - : ")
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
#print('comments:', info["comments"])
sum = 0
for item in info["comments"]:
    sum = sum + item['count']
print(sum)
