from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def one(request):
    return HttpResponse('<h1>One</h1>');
def two(request):
    return HttpResponse('<h1>two</h1>');
def three(request):
    return HttpResponse('<h1>three</h1>');
def four(request):
    return HttpResponse('<h1>four</h1>');
def five(request):
    return HttpResponse('<h1>five</h1>');

