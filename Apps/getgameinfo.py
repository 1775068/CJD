'''
Created on 2015年2月5日
获取游戏详细信息
@author: oTyg
'''
import getbase
"""
import os
import sys
"""
class GetGameInfo(getbase.GetBase):
    '''
             获取游戏信息
            条件 ：bygameid
    '''
     

    def __init__(self, titleid):
        self.GAMEID = self.dec2hex(titleid)
        #print (self.GAMEID)
        self.APIUrl = "https://xboxapi.com/v2/game-details-hex/"+ self.GAMEID
        
        
    def ParseGetJson(self,json):
        #print(json)
        
        js = json["Items"]

        PublisherName = js[0]["PublisherName"]#发行商
        DeveloperName = js[0]["DeveloperName"]#开发商
        ReleaseDate = js[0]["ReleaseDate"]#发行时间
        
        its = js[0]["Images"]
       
        for it in its:
            if it["Purposes"][0] == "BrandedKeyArt":
                img1 = it["ResizeUrl"]
                #img2 = it["Url"]
                print (img1)
                #print (img2)
            
        print (PublisherName , DeveloperName , ReleaseDate ,img1 )
        
    
    
    
    """
    10进制转16进制
    """
    def dec2hex(self,decstr):
        base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)]
        num = int(decstr)
        mid = []
        while True:
            if num == 0: break
            num,rem = divmod(num, 16)
            mid.append(base[rem])
        return ''.join([str(x) for x in mid[::-1]])

        
        