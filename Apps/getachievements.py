'''
Created on 2015年2月5日
获取成就详细信息
@author: oTyg
'''

import getbase

class GetAchievements(getbase.GetBase):



    def __init__(self, xuid,titleid):
        self.APIUrl = "https://xboxapi.com/v2/"+xuid+"/achievements/"+titleid
       
    def ParseGetJson(self,json):
        for achi in json:
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
            
            break
        