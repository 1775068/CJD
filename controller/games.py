'''
Created on 2015年2月4日

@author: oTyg
'''

from django.http import HttpResponse

from django.shortcuts import render_to_response
import DataProvider.onegames
import json
from django.views.decorators.csrf import csrf_exempt
from Models.GameInfo import  GameInfo
from Models.achievements import  Achievements


#游戏列表页面
def page_gameindex(req):
    return render_to_response("games\games.html")

#游戏成就列表页面
def page_gameAchievements(request):
    return render_to_response("games\gameachievements.html")

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

#游戏成就
@csrf_exempt
def ajax_gameAchievements_Detail(request):
    
    if (request.method == 'POST'):
        gameID = request.POST.get('gameid')
        pageIndex = request.POST.get('pageIndex')
    else:
        gameID  = request.GET.get('gameid')
        pageIndex = request.GET.get('pageIndex')
    
    tb , count = DataProvider.onegames.OneGames().AchievementsDetail(gameID,pageIndex)
    
    list_jsonobj = []
    
    for ID,Name,Name_Cn,Description,Description_Cn,GuideCount in tb:
        obj = {}
        obj["ID"] = ID
        obj["Name"] = Name
        obj["Name_Cn"] = Name_Cn
        obj["Description"] = Description
        obj["Description_Cn"] = Description_Cn
        obj["GuideCount"] = GuideCount
        list_jsonobj.append(obj)

    rjson = {}
    rjson["RecordCount"] = count
    rjson["Signlist"] = list_jsonobj 
    
    return HttpResponse(json.dumps(rjson) , content_type="application/json")
    
#更新成就内容
@csrf_exempt
def ajax_updategameAchievements_Detail(request):
    if (request.method == 'POST'):
        aid = request.POST.get('aid')
        name_cn = request.POST.get('name_cn')
        description_cn = request.POST.get('description_cn')
    else:
        aid = request.GET.get('aid')
        name_cn = request.GET.get('name_cn')
        description_cn = request.GET.get('description_cn')
        
    db = DataProvider.onegames.OneGames().UpdateAchievementsDetail(aid, name_cn, description_cn)
    return HttpResponse(json.dumps(db) , content_type="application/json")

   
