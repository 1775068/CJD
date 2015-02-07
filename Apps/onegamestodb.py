'''
Created on 2015年2月7日

@author: oTyg
'''
import getbase
import DataProvider.onegames 

class OneGamesToDB(getbase.GetBase):
    '''
    classdocs
    '''


    global gametitles
    
    def __init__(self):
        
        
        self.APIUrl = "https://xboxapi.com/v2/" + self.XUID + "/xboxonegames"

        
    def ParseGetJson(self,json):
        pass