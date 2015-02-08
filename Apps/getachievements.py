'''
Created on 2015年2月5日
获取成就详细信息
@author: oTyg
'''

import getbase
import DataProvider.onegames
from Models.achievements import  Achievements
class GetAchievementsMain():
    
    def Into(self,xuid):
        lis = DataProvider.onegames.OneGames().GetAllTitleIds()
        self.gameid = 0  #games表中的主键ID
        dbgamecount = len(lis)
        if(dbgamecount == 0):
            print("系统中不存在XboxOne游戏 ")
            return
        
        print("系统中存在:",str(dbgamecount),"个XboxOne游戏...")
        
        for row in lis:
            self.gameid = row[0]
            self.titleid = row[1]
            print("开始获取游戏titleid:",str(self.titleid),"的成就......")
            GetAchievements(xuid,self.gameid,self.titleid).GetJsonData()
            print("游戏titleid:",str(self.titleid),"的成就更新完成......")
        


class GetAchievements(getbase.GetBase):


    def __init__(self, xuid, gameid,titleid):
        Achievements.GameID = gameid
        self.titleid = titleid
        self.APIUrl = "https://xboxapi.com/v2/"+str(xuid)+"/achievements/"+str(titleid)
       
    def ParseGetJson(self,json):
        for achi in json:
            
            """
            gid = achi["id"]
            name = achi["name"]
            url = achi["mediaAssets"][0]["url"]            #图片url
            isSecret = achi["isSecret"]                    #是否为秘密成就
            description = achi["description"]
            lockedDescription = achi["lockedDescription"]  #解锁后描述
            achievementType = achi["achievementType"]      #成就类型
            participationType= achi["participationType"]   #参与类型
            isRevoked = achi["isRevoked"]                  #是否撤销
            
            valuetype = achi["rewards"][0]["type"]
            if(valuetype == "Gamerscore"):
                value = achi["rewards"][0]["value"]
            else:
                value = ""

            print(gid)
            print(name)
            print(url)
            print(isSecret)
            print(description)
            print(lockedDescription)
            print(achievementType)
            print(participationType)
            print(valuetype)
            print(value)
            print(isRevoked)
            
            """
            
            Achievements.AID = achi["id"]                                       #成就ID
            Achievements.TitleID = self.titleid
            Achievements.Name = achi["name"]
            Achievements.AchievementsImgUrl = ""#achi["mediaAssets"][0]["url"]       #图片url
            Achievements.IsSecret = achi["isSecret"]                              #是否为秘密成就
            Achievements.Description = achi["description"]
            #lockedDescription = achi["lockedDescription"]                        #解锁后描述
            Achievements.AchievementType = achi["achievementType"]                #成就类型
            Achievements.ParticipationType = achi["participationType"]            #参与类型
            Achievements.IsRevoked = achi["isRevoked"]                            #是否撤销
            
            if( "type" in achi["rewards"][0] ):
                Achievements.Valuetype = achi["rewards"][0]["type"]                   #成就值类型
                if(Achievements.Valuetype == "Gamerscore"):
                    Achievements.Sore = achi["rewards"][0]["value"]
            else:
                Achievements.Sore = 0

            DataProvider.onegames.OneGames().NewGameAchievements( Achievements)
            
        