'''
Created on 2015年2月1日

@author: oTyg
'''
import getbase

class GetAccountXUID(getbase.GetBase):
    '''
             获取XUID
    '''

    APIUrl = "https://xboxapi.com/v2/accountXuid"
    

    
    def ParseGetJson(self,json):
        print("GetAccountXUID get : " , json)
        pass
     

        