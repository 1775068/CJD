'''
Created on 2015年2月1日

@author: oTyg
'''

import time
from threading import Thread

class aaaa:
    
    def __init__(self):
        print("int it ")
        self._firewall()
        pass
    
    def __del__(self):
        
        print("del......")
    #临时，执行需要返回数据的函数时启动该函数，防止返回空数据
    def _firewall(self):
        
        self._thread = Thread(target=self._firewall_run)
        #self._thread.daemon = True
        self._thread.start()
      
    def _firewall_run(self):
        time.sleep(5)
        print("delll")
        

c = aaaa()


   



"""
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

print(type(respdata))
print(encodedjson)
print(type(encodedjson))
print(decodejson)
print(type(decodejson))
"""