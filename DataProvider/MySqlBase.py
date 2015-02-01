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
    
    
    def __init__(self, params):
        self.openConn()
    
    def __del__(self):
        self.closeConn()
        del(self._conn)
        del(self._cursor)
        
    #获取数据List        
    def GetList(self):
        self.closeConn()
        pass
    
    #获取一个数据
    def GetAData(self,sql):
        _cursor.execute(sql)
        self._firewall()
        return  _cursor.fetchall()
    
    def IsExists(self,sql):
        x = len(_cursor.execute(sql))
        if(x>0):
            return True
        return False
        
        
    #执行一条SQL语句返回True / False
    def ExeSQL(self,sql):
        _cursor.execute(sql)
        _exeresult = _conn.commit()
        columns = _exeresult['columns']
        
        #eof = _exeresult['eof']
        
        if(columns >=0):
            return True
        else:
            False
    
        
        
        
        

    #连接到mysql
    def openConn(self):
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

    
        
    
    
    
    
            
        