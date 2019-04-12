from django.shortcuts import render
from django.http import HttpResponse,Http404
from myapp import models
import copy


# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request, str):
    match_news = []

    if len(match_news) > 0:
        return render(request, "list.html")
    else:
        return render(request, "search_fail.html")
