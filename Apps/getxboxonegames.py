'''
Created on 2015年2月1日

@author: oTyg
'''
import getbase

class GetXBoxOneGames(getbase.GetBase):
    '''
            获取XBoxOne的游戏
    '''
 

    def __init__(self,xuid):
        self.XUID = xuid
        self.APIUrl = "https://xboxapi.com/v2/" + self.XUID + "/xboxonegames"

        
    def ParseGetJson(self,json):
     
        print("titles:" , json["titles"])
        titles = json["titles"]
        for items in titles:
            titleType = items["titleType"]
            name = items["name"]
            titleId = items["titleId"]
            maxGamerscore = items["maxGamerscore"]    #总成就分
            #lastUnlock = items["lastUnlock"]
            #serviceConfigId = items["serviceConfigId"]
            #platform = items["platform"]
            #earnedAchievements = items["earnedAchievements"]
            #currentGamerscore = items["currentGamerscore"]
            if(titleType == "DGame"):
                #print("lastUnlock:", lastUnlock) 
                #print("serviceConfigId:", serviceConfigId)
                #print("platform:", platform)
                #print("earnedAchievements:", earnedAchievements)
                #print("currentGamerscore:", currentGamerscore)
                print("name:", name)
                print("titleId:", titleId)
                print("titleType:", titleType)
                print("maxGamerscore:", maxGamerscore)
        
        
        