'''
Created on 2015年2月7日

@author: oTyg
'''
#encoding=encode
import DataProvider.mysqlbase


class OneGames(DataProvider.mysqlbase.MySqlBase):
    '''
    classdocs
    '''
      
    global _gameType

    def __init__(self):
        self._gameType = 1
    
   
    """
           返回数组 (False,False)
    [0] True/False  表示新Title是否插入成功
    [1] True/False  表示是否已经存在ImgURL
    """
    def NewGameTitleID(self,title_id):
       
        checkgame = 'select TitleID ,GameName,ImgURL from games where titleid = ' + str(title_id) + ';'
        x = self.GetData(checkgame)
        
        if(x == None):
            sql = 'Insert into games (TitleID , GameTypeID,status) values ('+ str(title_id) +','+ str(self._gameType)+',0);'
            try:
                self.ExeSQL(sql)
            except:
                print("新游戏添加失败：titleid:",title_id )
                return (False,False)
            print("新游戏添加成功：titleid:",title_id )
            return (True,False)
        elif( x[1] == None or x[2] == None):
            tag = False
        else:
            tag = True
        return (True,tag)
    
    def GetGameIDs(self):
        sql = "select ID from games;"
        return self.GetData(sql)
    '''
    publisherName  发行商
    developerName  开发商
    releaseDate    发布时间
    img            游戏图片地址
    '''
    def UpDateGameInfoBytitleid(self,titleid,gamename,publisherName , developerName , releaseDate ,img):
        sql = 'update games set GameName="'+gamename+'",' + ' publisherName="'+publisherName +'",' + 'developerName="'+developerName +'",releaseDate=DATE_FORMAT("'+releaseDate[:10]+'","%Y~%m~%d"),imgURL="'+img +'" where titleid='+str(titleid)+';'
        #print(sql)
        return self.ExeSQL(sql)
    
    
    