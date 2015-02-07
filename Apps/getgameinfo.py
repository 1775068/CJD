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
import DataProvider.onegames
import common

class GetGameInfo(getbase.GetBase):
    '''
             获取游戏信息
            条件 ：bygameid
    '''

    global imgSavepath     
    global titleid
    def __init__(self, titleid):
        self.GAMEID = self.dec2hex(titleid)
        self.APIUrl = "https://xboxapi.com/v2/game-details-hex/"+ self.GAMEID
        self.imgSavepath = "../static/gameimg/"
        self.titleid = titleid
        #print("imgSavepath1=",self.imgSavepath)
        
    def ParseGetJson(self,json):
        #print(json)
        js = json["Items"]
        
        publisherName = js[0]["PublisherName"]#发行商
        developerName = js[0]["DeveloperName"]#开发商
        releaseDate = js[0]["ReleaseDate"]    #发行时间
        gamename = js[0]["Name"]              #游戏名称
        
        global imgurl
        its = js[0]["Images"]
       
        for it in its:
            if it["Purposes"][0] == "BrandedKeyArt":
                imgurl = it["ResizeUrl"]

        #print (publisherName , developerName , releaseDate ,imgurl)
        #print("imgSavepath=",self.imgSavepath+name , imgurl)
        self.imgSavepath = self.imgSavepath + gamename + ".png"
        down = common.DownImg(imgurl, self.imgSavepath)
        downsuccess = down[0]
        filename = down[1]
        print("图片下载结果：",downsuccess )
        if(downsuccess):
            x = DataProvider.onegames.OneGames().UpDateGameInfoBytitleid(self.titleid , gamename,publisherName, developerName, releaseDate, filename)
            print("游戏信息更新结果：",x)
    
    
    
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

        
        