from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kavi(request):
    return HttpResponse('<h1>my name is kavitha</h1>')
    
def madhu(request):
    return HttpResponse('<h1>my name is madhusree<h1>')

def manu(request):
    return HttpResponse('<marquee><h1>we are good friends</h1><marquee>')

def kavi(request):
    return HttpResponse('<marquee><h1>kavitha Ramakrishna</h1><marquee>')