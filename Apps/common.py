'''
Created on 2015年2月7日
 工具
@author: oTyg
'''

import urllib


"""
保存图片，返回站点的保存路径和名称
"""
def DownImg(url,savepath):

    try:
        print(url)
        req = urllib.request.urlopen(url)
        req = req.read()
        #print(len(req))
        if(not req ):
            return(False,None)
        
        file = open(savepath,"wb" )
        file.write(req)
        file.close()
        return(True, savepath)
    except IOError as e:
        print("error",e)
        return(False,None)
        

