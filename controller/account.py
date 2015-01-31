'''
Created on 2015年1月31日

@author: oTyg
'''

from django.http import HttpResponse
from django.shortcuts import render_to_response

def template(req):
    return render_to_response("base.html")


def index(req):
    return render_to_response("tables_control.html")
    #return HttpResponse("This is index......")
    

def login(req):
    return render_to_response("login.html")
    #return HttpResponse("This is index......")    