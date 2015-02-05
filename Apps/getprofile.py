'''
Created on 2015年2月5日
获取个人信息
@author: oTyg
'''
import getbase
class GetProfile(getbase.GetBase):
    '''
    classdocs
    '''


    def __init__(self, xuid):
        self.APIUrl = "https://xboxapi.com/v2/" + xuid +"/profile"
        
    
    def ParseGetJson(self,json):
        #print(json)
        gamertag = json["Gamertag"]                    #账户名
        gamerscore = json["Gamerscore"]                #个人成就总分                
        gameDisplayPicRaw = json["GameDisplayPicRaw"]  #头像
        xboxOneRep = json["XboxOneRep"]                #玩家评价
        accountTier = json["AccountTier"]              #金会员状态
        print(gamertag ,gamerscore,gameDisplayPicRaw,xboxOneRep,accountTier )
        