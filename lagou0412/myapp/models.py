from django.db import models
from django.conf import settings
import os, csv
from myapp import mysqlOperate

# return: job array
def findJob(searchStr):
    ret = []
    for oneJob in mysqlOperate.all_data:
        if str.lower(searchStr) in str.lower(oneJob.positionName):
            ret.append(oneJob)
    return ret
