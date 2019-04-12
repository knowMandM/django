import pandas, numpy
import mysqlOperate

def calc_salary(lagou_salary):
    lagou_salary = lagou_salary.replace('以上','').replace('以下','')
    splitsalary = lagou_salary.split('-')
    min = splitsalary[0]
    max = min
    if len(splitsalary) > 1:
        max = splitsalary[1]
    avg = (int(min.upper().replace('K','')) + int(max.upper().replace('K',''))) / 2
    return avg

def genDataFrame():
    datas = mysqlOperate.getData()
    data_dict = {}
    
    for key in mysqlOperate.headers:
        data_dict[key] = []

    for data in datas:
        for key in mysqlOperate.headers:
            value = getattr(data, key)
            if key == "salary":
                value = calc_salary(value)
            data_dict[key].append(value)

    print(data_dict)

    df = pandas.DataFrame(data_dict)
    return df
    
df = genDataFrame()

def analyze_jobcount_salary(sIndex, df = df, sortField = "job_count", ascending=False):
    ret_dict = {}
    dict_data = df.pivot_table(index=sIndex, values=["companyId","salary"], aggfunc=[len, numpy.mean])
    ret_df = pandas.DataFrame({
        sIndex : [x for x in dict_data.index],
        "job_count" : [x for x in dict_data["len"]["companyId"]],
        "salary" : [x for x in dict_data["mean"]["salary"]]
    })

    ret_df = ret_df.sort_values(sortField, ascending=ascending)
    print(ret_df.head(100))
    ret_dict["keys"] = [str(x) for x in ret_df[sIndex]]
    ret_dict["job_count"] = [x for x in ret_df["job_count"].values]
    ret_dict["salary"] = [x for x in ret_df["salary"].values]
    return ret_dict


def workYear_jobcount_salary():
    return analyze_jobcount_salary("workYear")

def education_jobcount_salary():
    return analyze_jobcount_salary("education")





