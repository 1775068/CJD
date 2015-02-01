'''
Created on 2015年2月1日

@author: oTyg
'''

import urllib.request
import json

print("-----------------------------------------")


apiurl = "https://xboxapi.com/v2/accountXuid"
""" 
values = {
'X-AUTH' : '553c59589f97a86fca248cc0e4ba1d61bb6c4a90'
}
"""

headers={
'X-AUTH' : '553c59589f97a86fca248cc0e4ba1d61bb6c4a90'
}
req = urllib.request.Request(apiurl,headers=headers)
response = urllib.request.urlopen(req)
buff = response.read()

respdata = buff.decode("utf8")
response.close()

 
print(respdata)
t = json.loads(respdata)
print ( t.keys())
print ( t["xuid"])
"""
print(type(respdata))
print(encodedjson)
print(type(encodedjson))
print(decodejson)
print(type(decodejson))
"""