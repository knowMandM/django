from django.shortcuts import render
from django.http import HttpResponse,Http404
from myapp import models
import copy


# Create your views here.
def index(request):
    return render(request, "index.html")

def search(request, str):
    math_jobs = models.findJob(str)
    print(math_jobs)
    if len(math_jobs) > 0:
        return render(request, "list.html", {"jobs" : math_jobs})
    else:
        return render(request, "search_fail.html", {"search": str})

def staticsPage(request, pagename):
    dicName2html = {
        "edu_count" : "学历与职位数量.html",
        "edu_salary" : "学历与薪资.html",
        "workYear_salary" : "工作年限与薪资.html",
    }

    if pagename in dicName2html:
        return render(request, dicName2html[pagename])
    else:
        raise Http404