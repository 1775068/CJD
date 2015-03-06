'''
Created on 2015年2月4日

@author: oTyg
'''

from django.http import HttpResponse
from django.http import HttpRequest

from django.shortcuts import render_to_response
import DataProvider.onegames
import json

from django.views.decorators.csrf import csrf_exempt
from Models.GameInfo import  GameInfo

def index(req):
    return render_to_response("games\games.html")

#游戏列表页面
@csrf_exempt
def ajax_index(request):
    pageIndex = 1
    if (request.method == 'POST'):
        pageIndex = request.POST.get('pageIndex')
    else:
        pageIndex = request.GET.get('pageIndex')

    list_db ,count = DataProvider.onegames.OneGames().PageGames(pageIndex)
     
    list_jsonobj = [] 
    for ID,GameName, GameTypeID,GameName_CN,Status in list_db:
        
        if( GameName is None or GameName == 'None'):
            continue
        obj = {}
        obj["ID"] = ID
        obj["GameName"] = GameName
        
        if(GameTypeID == 1):
            obj["GameType"] = 'XBox'
        elif(GameTypeID == 2):
            obj["GameType"] = 'PS'
        else:
            obj["GameType"] = '---'
         
        if( GameName_CN is None or GameName_CN == 'None'):
            obj["GameName_CN"] = ''
        else:
            obj["GameName_CN"] = GameName_CN
            
        obj["Status"] = Status
        list_jsonobj.append(obj)
       
    rjson = {}
    rjson["RecordCount"]= count
    rjson["Signlist"] = list_jsonobj 
    
    return HttpResponse(json.dumps(rjson) , content_type="application/json")

#更新游戏中文名称
@csrf_exempt
def ajax_update_gameNameCN(request):

    if (request.method == 'POST'):
        GameInfo.ID = request.POST.get('id')
        GameInfo.GameName_CN = request.POST.get('gamenameCn')
    else:
        GameInfo.ID  = request.GET.get('id')
        GameInfo.GameName_CN = request.GET.get('gamenameCn')
  
    dd = DataProvider.onegames.OneGames().UpdateGameNameCN(GameInfo)

    return HttpResponse(json.dumps(dd) , content_type="application/json")
    
@csrf_exempt
def ajax_update_gamestatus(request):
    
    if (request.method == 'POST'):
        GameInfo.ID = request.POST.get('id')
        GameInfo.Status = request.POST.get('status')
    else:
        GameInfo.ID  = request.GET.get('id')
        GameInfo.Status = request.GET.get('status')
    
    dd = DataProvider.onegames.OneGames().UpdateGameStatus(GameInfo)
    
    return  HttpResponse(json.dumps(dd) , content_type="application/json")

   
