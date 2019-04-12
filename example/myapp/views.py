from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def index(request):
    obj = {}
    obj["info"] = "你好啊!"
    return JsonResponse(obj)