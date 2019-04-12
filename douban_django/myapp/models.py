from django.db import models
from django.conf import settings
import os, csv
from myapp import mysqlOperate

# 根据id获取电影
def getMovieByID(id):
    if (id + 1) > len(mysqlOperate.all_data) or id < 0:
        return None
    return mysqlOperate.all_data[id + 1]

def getMovieByTile(search_str):
    for movie in mysqlOperate.all_data:
        if search_str in movie.title:
            return movie
    return None
