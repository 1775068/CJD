'''
Created on 2015年2月1日

@author: oTyg
'''
import getbase

class GetXUIDWithTag(getbase.GetBase):


    def __init__(self,gametag):
        self.GAMETAG = gametag
        self.APIUrl = "https://xboxapi.com/v2/xuid/" + self.GAMETAG

    def ParseGetJson(self,json):
        print("GetXUIDWithTag get : " , json)

        pass
        