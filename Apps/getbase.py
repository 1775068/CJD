'''
Created on 2015年2月1日

@author: oTyg
'''

import urllib.request
import json

class GetBase(object):
    '''
            获取数据的基类
    '''
    

    #定义每个数据接口的URL，由子类配置
    APIUrl = ""
    XUID = ""
    GAMETAG = ""
    GAMEID = ""
    #API Key
    _headers = {
                
                'X-AUTH' : '553c59589f97a86fca248cc0e4ba1d61bb6c4a90',
                'Accept-Language' : 'en-US'
                }
    
    
    def __init__(self):
        pass
    
    
    '''
            获取数据并返回JSON
    '''
    def GetJsonData(self): 
        #print(self.APIUrl)
        req = urllib.request.Request(self.APIUrl,headers = self._headers)
        response = urllib.request.urlopen(req)
        buff = response.read()
        respdata = buff.decode("utf8")
        response.close()
        
        getjson = json.loads(respdata)
        self.ParseGetJson(getjson)

    def ParseGetJson(self,json):
        pass        
            