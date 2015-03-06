'''
Created on 2015年3月5日

@author: oTyg
'''
from django.http import HttpResponse,Http404
from django import template


def pager(req):
    
    fp = open('C:/CodeSpace/CJD/static/pager.html')
    t = template.Template(fp.read())
    fp.close()
    html = t.render(template.Context( {'pager':pager}))
    
    return HttpResponse(html)