from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def one(request):
    return HttpResponse('<h1>one</h1>')

