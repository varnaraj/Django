import imp
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def gm_view(request):
    return HttpResponse('<h1>Good Morning</h1>')
def ga_view(request):
    return HttpResponse('<h1>Good afternoon</h1>')
def ge_view(request):
    return HttpResponse('<h1>Good evening</h1>')