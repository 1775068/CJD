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
     
        #print("titles:" , json["titles"])
        titles = json["titles"]
        for items in titles:
            lastUnlock = items["lastUnlock"]
            titleId = items["titleId"]
            serviceConfigId = items["serviceConfigId"]
            titleType = items["titleType"]
            platform = items["platform"]
            name = items["name"]
            earnedAchievements = items["earnedAchievements"]
            currentGamerscore = items["currentGamerscore"]
            maxGamerscore = items["maxGamerscore"]
            if(titleType == "DGame"):
                print(name) 
        
        
        