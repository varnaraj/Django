from email import message
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.utils import resample
# Create your views here.
# we planned to http//127.0.0.1:8000/wish  nu adikka hii nu varanum
#request http//127.0.0.1:8000/wish
#response hii

def wish(request):
    message='<h1>Hello good Evening</h1>'
    return HttpResponse(message)

