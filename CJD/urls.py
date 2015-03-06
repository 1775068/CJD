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
    url(r'^games/', games.index),
    
    
    
    
    url(r'^ajax_gamesindex/', games.ajax_index),
    url(r'^ajax_upgamenamecn/', games.ajax_update_gameNameCN),
    url(r'^ajax_upgamestatus/', games.ajax_update_gamestatus),
    
    url(r'^pager/$', pager.pager),
    
)
