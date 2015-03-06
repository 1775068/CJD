'''
Created on 2015年2月1日
MySql操作类
@author: oTyg
'''


import time
from threading import Thread
from mysql import connector



class MySqlBase(object):
    
    USER = "root"
    PWD = "123456ok."
    HOST = "127.0.0.1"
    PORT = "3306"
    DB = "CJD"
    
    global _conn
    global _cursor

    
    def __init__(self):
        self.openConn()
    
    def __del__(self):
        #self.closeConn()
        #del(self._conn)
        #del(self._cursor)
        pass
    
        
    #获取数据List        
    def GetList(self):
        #self.closeConn()
        pass
    
    #获取数据集
    def GetAllData(self,sql):
        #self.OpenConn()
        #_cursor.execute(sql)
        #self._firewall()
        _conn = connector.connect(user=self.USER,password=self.PWD,host=self.HOST,port = self.PORT,database=self.DB)
        _cursor = _conn.cursor()
        _cursor.execute(sql)
        return _cursor.fetchall() 

    #获取一个数据
    def GetOneData(self,sql):
        #self.OpenConn()
        #_cursor.execute(sql)
        #self._firewall()
        _conn = connector.connect(user=self.USER,password=self.PWD,host=self.HOST,port = self.PORT,database=self.DB)
        _cursor = _conn.cursor()
        _cursor.execute(sql)
        return _cursor.fetchone()
    
    
    """
           判断数据是否存在，如果存在则返回数据
    return (False,None)
    [0]: 是否存在数据
    [1]: 如果存在则返回数据
    """
    def IsExistsBack(self,sql):
        """
        if(self.openConn() == False):
            self.openConn()
        """
        _conn = connector.connect(user=self.USER,password=self.PWD,host=self.HOST,port = self.PORT,database=self.DB)
        _cursor = _conn.cursor()
        _cursor.execute(sql)
        result = _cursor.fetchone()
        if( result is None):
            return (False,None)
        return (True,result)
    
    
    def OpenConn(self):
        _conn = connector.connect(user=self.USER,password=self.PWD,host=self.HOST,port = self.PORT,database=self.DB)
        _cursor = _conn.cursor()

    #执行一条SQL语句返回True / False
    def ExeSQL(self,sql):
        _conn = connector.connect(user=self.USER,password=self.PWD,host=self.HOST,port = self.PORT,database=self.DB)
        _cursor = _conn.cursor()
        try:
            _cursor.execute(sql)
            _conn.commit()
            return True
        except connector.Error as e:
            print("db error:",e)
            return False
        """
        try:
            _cursor.execute(sql)
            _conn.commit()
            return True
        except:
            _conn.rollback()
            return False
        
        
        """
           

        
        
        
        
        
        
        
        
        

    #连接到mysql
    def openConn(self):
        
        #print('"1",_cursor,_conn')
        try:
            _conn = connector.connect(user=self.USER,password=self.PWD,host=self.HOST,port = self.PORT,database=self.DB)
            _cursor = _conn.cursor()
            
            return True
        except connector.Error as e:
            print(e)
            return False

    #关闭sql链接
    def closeConn(self):
        try:
            _conn.close()
            _cursor.close()
        except:
            pass

    #临时，执行需要返回数据的函数时启动该函数，防止返回空数据
    def _firewall(self):
        self._thread = Thread(target=self._firewall_run)
        #self._thread.daemon = True
        self._thread.start()
        
    def _firewall_run(self):
        time.sleep(0.1)

   
        