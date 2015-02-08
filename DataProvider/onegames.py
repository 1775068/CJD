'''
Created on 2015年2月7日

@author: oTyg
'''
#encoding=encode
import DataProvider.mysqlbase
from Models.achievements import  *


class OneGames(DataProvider.mysqlbase.MySqlBase):
    '''
    XBox游戏DB相关
    '''
      
    global _gameType

    def __init__(self):
        self._gameType = 1
    
    """
             获取所有游戏的titleid
    """
    def GetAllTitleIds(self):
        sql = 'select id,titleid from games where GameTypeID = 1'
        ls = self.GetAllData(sql)
        return ls
    
    """
            根据titleid 更新游戏的成就信息
    """
    def NewGameAchievements(self,achievements):
        obj = achievements
        check = 'select GameID,AID,TitleID,IsRevoked from achievements where GameID = ' +str(obj.GameID) + ' and AID = '+str(obj.AID) + ' and TitleID = ' + str(obj.TitleID)  
        
        x = self.IsExistsBack(check)
        exists = x[0]                         #是否存在数据
        data = x[1]                           #如果存在返回的数据
        if(exists):
            isRevoked = data[3]
            if(isRevoked != obj.IsRevoked):
                print("成就存在，撤销值改变，更新......")
                up = 'update achievements set IsRevoked  = ' +obj.IsRevoked+' where GameID = ' +str(obj.GameID) + ' and AID = '+str(obj.AID) + ' and TitleID = ' + str(obj.TitleID)
                success = self.ExeSQL(up)
                print("成就撤销值值更新结果:", success)
            print("成就已存在，继续......")
            return
        #x = self. escape_string("asfasdf")    
        newachi = "insert into achievements (GameID , AID,TitleID,Name, AchievementType,ParticipationType,Description,Score,AchievementsImgUrl,IsSecret,IsRevoked) values("+str(obj.GameID) + "," +  str(obj.AID) + ","+ str(obj.TitleID) + ",'" +  obj.Name + "','"+  obj.AchievementType+ "','"+ obj.ParticipationType + "','"+ obj.Description + "',"+ str(obj.Sore) + ",'" +  obj.AchievementsImgUrl + "',"+ str(obj.IsSecret) + ","+  str(obj.IsRevoked) + ")"        
        #print(newachi)
        if (self.ExeSQL(newachi)):
            print("游戏成就添加成功：titleid:",str(obj.TitleID))
        else:
            print(newachi)
            print("游戏成就添加失败：titleid:",str(obj.TitleID))
        
                  

    """
            返回数组 (False,False)
    [0] True/False  表示新Title是否插入成功
    [1] True/False  表示是否已经存在ImgURL
    """
    def NewGameTitleID(self,title_id,maxGamerscore):
       
        checkgame = 'select TitleID ,GameName,ImgURL,maxGamerscore from games where titleid = ' + str(title_id) + ';'
        x = self.GetOneData(checkgame)
        
        
        if(x == None):
            sql = 'Insert into games (TitleID , GameTypeID,maxGamerscore,status) values ('+ str(title_id) +','+ str(self._gameType)+','+ str(maxGamerscore)+',0);'
            try:
                self.ExeSQL(sql)
            except:
                print("新游戏添加失败：titleid:",title_id )
                return (False,False)
            print("新游戏以及分数添加成功：titleid:",title_id )
            return (True,False)
        
    
            
        gamename = x[1]
        imgurl = x[2]
        gamescore = x[3]
        
  
        if(gamescore == None or gamescore != maxGamerscore):
            sql = 'update games set maxGamerscore = ' + str(maxGamerscore) +' where titleid = ' + str(title_id) 
            try:
                self.ExeSQL(sql)
            except:
                print("游戏分数更新失败：titleid:",title_id )
            print("游戏分数更新成功：titleid:",title_id )
            
        
    
        gameimg = True
        if(gamename  == None or imgurl == None ):
            gameimg = False
            
        return (True,gameimg)
            
    
    
    def GetGameIDs(self):
        sql = "select ID from games;"
        return self.GetData(sql)
    '''
    publisherName  发行商
    developerName  开发商
    releaseDate    发布时间
    img            游戏图片地址
    '''
    def UpDateGameInfoBytitleid(self,titleid,gamename,publisherName , developerName , releaseDate ,img ):
        sql = 'update games set GameName="'+gamename+'",' + ' publisherName="'+publisherName +'",' + 'developerName="'+developerName  +'",releaseDate=DATE_FORMAT("'+releaseDate[:10]+'","%Y~%m~%d"),imgURL="'+img +'" where titleid='+str(titleid)+';'
        #print(sql)
        return self.ExeSQL(sql)
    
    
    