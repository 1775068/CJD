'''
Created on 2015年2月1日

@author: oTyg
'''

import getaccountxuid
import getxboxonegames
import getxuidwithtag

#获取的gameid = Major Nelson

class GetWith(object):
    '''
            控制台获取xboxapi数据入口
    '''


    def __init__(self):
        
        print("------------------------ 欢迎来到控制台获取xboxapi数据入口------------------------\n")
        
        print("-----------------------------请输入相应的命令获取数据------------------------------\n")
        
        print("命令\t\t官方文档\t\t\t\t中文描述")
        print("myxuid\t\tAccount XUID\t\t\t【Account XUID】")
        print("gxuid\t\tGamertag XUID\t\t\t\t【根据gametag 获取 XUID】")
        print("onegames\tXbox ONE Games\t\t\t【根据xuid获取所有xbox one 的游戏】")
      
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
                

x = GetWith()
        