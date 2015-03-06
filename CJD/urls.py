from django.conf.urls import patterns, include, url
#from django.contrib import admin

from controller import account
from controller import games

#import settings.STATICFILES_DIRS
import pager

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CJD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', account.index),
    url(r'^login/', account.login),
    
    
    url(r'^t/', account.template),
    
    
    url(r'^games/', games.page_gameindex),                        #游戏列表
    url(r'^gameachievements/', games.page_gameAchievements),      #成就列表
    
    
    url(r'^ajax_gamesindex/', games.ajax_index),                  #游戏列表数据
    url(r'^ajax_gameachievementsdetail/', games.ajax_gameAchievements_Detail),      #成就列表
    url(r'^ajax_upgamenamecn/', games.ajax_update_gameNameCN),    #更新游戏中文名称
    url(r'^ajax_upgamestatus/', games.ajax_update_gamestatus),    #更新游戏显示状态
    url(r'^ajax_upgameachievements/', games.ajax_updategameAchievements_Detail),    #更新游戏成就信息
    
    url(r'^pager/$', pager.pager),
    
)
