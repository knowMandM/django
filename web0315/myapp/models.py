from django.db import models
from django.conf import settings
import os, csv

# 定义字段在csv中的位置
title = 0
time = 1
author = 2
text = 3
web = 4
abstract = 9
newstype = 6
label = 8


csv_data = []        # 所有新闻数据
map_csv_data ={}     # 按来源分类的新闻数据
type_csv_data = {}   # 按新闻类型分类的新闻数据
nearly_csv_date = {} # 按相似度分类
nearly_type_data = {}# 只有有相似度的数据(上面的都是所有数据)

class CMyNew:
    id = None
    title = None
    time = None
    author = None
    text = None
    web = None
    abstract = None
    new_type = None
    label = None
    
    
def get_data():
    if len(csv_data) == 0:
        load_data()
    return csv_data

def load_data():
    print("load csv start ...")
    file_path = os.path.join(settings.BASE_DIR, "datas2.csv")
    news = []
    try:
        news = csv.reader(open(file_path))
    except Exception as err:
        print(err)
    
    for one_new in news:
        if one_new[0] == 'title':
            continue
        else:
            data = CMyNew()
            data.time = one_new[time]
            data.title = one_new[title]
            data.web = one_new[web]
            data.new_type = one_new[newstype]
            data.text = one_new[text]
            data.author = one_new[author]
            data.abstract = one_new[abstract]
            data.id = len(csv_data)
            data.label = int(one_new[label])

            #id2data
            csv_data.append(data)

            #web2datalist 来源
            if not (data.web in map_csv_data):
                map_csv_data[data.web] = []
            map_csv_data[data.web].append(data)

            # 相似度
            if not (data.label in nearly_csv_date):
                nearly_csv_date[data.label] = []
            nearly_csv_date[data.label].append(data)

            # 有相似度的数据
            if data.label < 20:
                if not (data.new_type in nearly_type_data):
                    nearly_type_data[data.new_type] = []
                nearly_type_data[data.new_type].append(data)

            #type2dataList 类型
            if not (data.new_type in type_csv_data):
                type_csv_data[data.new_type] = []
            type_csv_data[data.new_type].append(data)

    print("综合：", len(type_csv_data["综合"]))
    print("load csv complete ...")

# 获取一下数据
get_data()
