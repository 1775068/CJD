'''
Created on 2015年2月1日

@author: oTyg
'''
import getbase
import DataProvider.onegames 
import getgameinfo
from threading import Thread
import time

class GetXBoxOneGames(getbase.GetBase):
    '''
            获取XBoxOne的游戏
    '''
 

    def __init__(self,xuid):
        self.XUID = xuid
        self.APIUrl = "https://xboxapi.com/v2/" + self.XUID + "/xboxonegames"
    
    def timer(self):
        pass
    
        
    def ParseGetJson(self,json):
        #print("titles:" , json["titles"])
        titles = json["titles"]
        for items in titles:
            titleType = items["titleType"]
            #name = items["name"]
            titleId = items["titleId"]
            #maxGamerscore = items["maxGamerscore"]    #总成就分
            #lastUnlock = items["lastUnlock"]
            #serviceConfigId = items["serviceConfigId"]
            #platform = items["platform"]
            #earnedAchievements = items["earnedAchievements"]
            #currentGamerscore = items["currentGamerscore"]
            x = DataProvider.onegames.OneGames()
            if(titleType == "DGame"):
                #print("lastUnlock:", lastUnlock) 
                #print("serviceConfigId:", serviceConfigId)
                #print("platform:", platform)
                #print("earnedAchievements:", earnedAchievements)
                #print("currentGamerscore:", currentGamerscore)
                #print("name:", name)
                #print("titleId:", titleId)
                #print("titleType:", titleType)
                #print("maxGamerscore:", maxGamerscore)
                
                tag = x.NewGameTitleID(titleId)
                insertsuccess = tag[0]         #是否成功插入titleid或者该titleid已经存在
                imgsuccess = tag[1]            #是否已经抓取了其他游戏相关信息
                if(insertsuccess == False):
                    print("操作失败,取下一条......")
                    continue
                if(imgsuccess):
                    print(titleId , "已存在,继续 ...")
                    continue
                else:
                    global _thread 
                    self._thread = Thread(target=self.gameInfo,args=(titleId,))
                    self._thread.start()
                    
                    #return
                    
        
        
        
    def gameInfo(self,args):
        titleId = args
        print("游戏(titleid:",titleId,")已存在,游戏信息不存在,\n开始获取游戏(titleid:",titleId,")信息、下载游戏图片......")
        getgameinfo.GetGameInfo(titleId).GetJsonData()
        print("游戏(titleid:" ,titleId ,")信息更新完成......\n-------------------------")
        time.sleep(1)
        self._thread._delete()
        #self._thread.daemon = True
        
