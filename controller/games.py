'''
Created on 2015年2月4日

@author: oTyg
'''

from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(req):
    return render_to_response("games\games.html")