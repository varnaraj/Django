from unittest import result
from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def tellMeTime(request):
    time=datetime.datetime.now()
    result='<h1>Hi the time is '+ str(time)+'</h1>'
    return HttpResponse(result)