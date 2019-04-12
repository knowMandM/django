from django.shortcuts import render
from django.http import HttpResponse,Http404
from myapp import models
import copy


# Create your views here.
def index(request):
    hot_news = copy.deepcopy(models.nearly_type_data["文化"])
    sport_news = copy.deepcopy(models.nearly_type_data["体育"])
    polity_news = copy.deepcopy(models.nearly_type_data["政治"])
    stock_news = copy.deepcopy(models.nearly_type_data["财经"])

    def cutabstract(s):
        if len(s.abstract) > 100:
            s.abstract = s.abstract[:97] + "..."
        return s
    hot_news = list(map(cutabstract, hot_news))
    sport_news = list(map(cutabstract, sport_news))
    polity_news = list(map(cutabstract, polity_news))
    stock_news = list(map(cutabstract, stock_news))
    
    return render(request, "home.html", {"hot_news":hot_news[0:6], "sport_news":sport_news[:6], "polity_news":polity_news[:6], "stock_news":stock_news[:6]})

def detail(request, id):
    if (id - 1 > len(models.csv_data)):
        return Http404(request)
    new_detail = models.csv_data[id]

    nearly_news = None
    if new_detail.label != 999:
        nearly_news = models.nearly_csv_date[new_detail.label]
        nearly_news = list(filter(lambda x : x.id != id, nearly_news))

    text_arr =  new_detail.text.split('　　')
    text_arr = map(lambda x : '　　' + x, text_arr)
    return render(request, "detail.html", {"one_new": new_detail, "text_arr" : text_arr, "nearly_news":nearly_news} )

def fromsrc(request, new_type):
    print(new_type)
    if new_type == "热点新闻":
        return render(request, "list.html", {"news": models.type_csv_data["综合"][:100]} )

    if not (new_type in models.map_csv_data):
        return Http404(request)
    news = models.map_csv_data[new_type]
    return render(request, "list.html", {"news": news[:100]} )

def src(request, src_type):
    if not (src_type in models.type_csv_data):
        return Http404(request)
    news = models.type_csv_data[src_type]
    return render(request, "list.html", {"news": news[:100]} )

def search(request, str):
    match_news = []
    for new in models.csv_data:
        if str in new.title:
            match_news.append(new)

    if len(match_news) > 0:
        return render(request, "list.html", {"news": match_news} )
    else:
        return render(request, "search_fail.html")

def newstype(request, news_type):
    print(news_type)
    if not (news_type in models.type_csv_data):
        return Http404(request)
    news = models.type_csv_data[news_type]
    return render(request, "list.html", {"news": news[:100]} )
    