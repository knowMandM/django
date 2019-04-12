from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return reder(request, "home.html")
    
def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    result = int(a) + int(b)
    return HttpResponse(str(result))

def add2(request, a, b):
    return HttpResponse(str(a + b))