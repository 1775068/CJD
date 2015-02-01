#@coding="utf-8"
'''
Created on 2015��1��30��

@author: oTyg
'''


"""
from mysql import connector
#import mysql

user = "root"
pwd = "123456ok."
host = "127.0.0.1"
port = "3306"
db = "world"


try:
    conn = connector.connect(user=user, password=pwd, host=host,port = port,database=db)
except:
    print('fail[]')
    
    
cursor = conn.cursor()
#cursor.execute("SELECT * FROM ttt;")

#cursor.execute("delete FROM CITY where id in (4080);")
#conn.commit()

#cursor.execute("SELECT * FROM CITY;")



cursor.execute("""insert into ttt (name) values("Heaton 何涛") """)
conn.commit()

cursor.execute("SELECT * FROM ttt;")

dts = cursor.fetchall()

conn.close()
cursor.close()
print(dts)
for a in dts:
    print(a);


    
     

"""


 


