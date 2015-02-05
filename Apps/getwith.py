'''
Created on 2015年2月1日

@author: oTyg
'''

import getaccountxuid
import getxboxonegames
import getxuidwithtag
import getgameinfo
import getachievements
import getprofile

#获取的gameid = Major Nelson  xuid = 2584878536129841

class GetWith(object):
    '''
            控制台获取xboxapi数据入口
    '''


    def __init__(self):
        
        print("------------------------ 欢迎来到控制台获取xboxapi数据入口------------------------\n")
        
        print("-----------------------------请输入相应的命令获取数据------------------------------\n")
        
        print("命令\t\t官方文档\t\t\t\t中文描述")
        print("myxuid\t\tAccount XUID\t\t\t【Account XUID】")
        print("gxuid\t\tGamertag XUID\t\t\t【根据gametag 获取 XUID】")
        print("onegames\tXbox ONE Games\t\t\t【根据xuid获取所有xbox one 的游戏】")
        print("gameinfo\tXbox Game Information\t\t【根据titleid获取游戏详细信息】")
        print("cj\t\tXbox Game Achievements\t\t【根据xuid,titleid获取成就信息】")
        print("profile\t\tProfile\t\t\t\t【根据xuid获取个人信息】")
      
        while True:
            print("\n请输入命令:")
            ps = input()
            
            if(ps == "myxuid"):
                getaccountxuid.GetAccountXUID().GetJsonData()
            
            if(ps == "gxuid"):
                print("请输入GameTag:")
                tag = input()
                
                getxuidwithtag.GetXUIDWithTag(tag).GetJsonData()
                pass
                
            if(ps == "onegames"):
                #print("请输入XUID:")
                #xuid = input()
                xuid = "2584878536129841"
                getxboxonegames.GetXBoxOneGames(xuid).GetJsonData()
            
            if(ps == "gameinfo"):
                print("获取游戏详细信息，请输入titleid:")
                titleid = input()
                getgameinfo.GetGameInfo(titleid).GetJsonData()
            if(ps == "cj"):
                xuid = "2584878536129841"
                print("请输入titleid:")
                titleid = input()
                if(titleid==""):
                    titleid = "2147358433"
                getachievements.GetAchievements(xuid,titleid).GetJsonData()
            if(ps == "profile"):
                print("请输入xuid:")
                xuid = input()
                if(xuid == ""):
                    xuid = "2584878536129841"
                getprofile.GetProfile(xuid).GetJsonData()

x = GetWith()
        