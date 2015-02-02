from django.conf.urls import patterns, include, url
#from django.contrib import admin

from controller import account

#import settings.STATICFILES_DIRS

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CJD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', account.index),
    url(r'^login/', account.login),
    url(r'^t/', account.template),
)
