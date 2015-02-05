'''
Created on 2015年2月1日
获取XUID
@author: oTyg
'''
import getbase

class GetAccountXUID(getbase.GetBase):


    APIUrl = "https://xboxapi.com/v2/accountXuid"
    

    
    def ParseGetJson(self,json):
        xuid = json
        print(xuid)

        