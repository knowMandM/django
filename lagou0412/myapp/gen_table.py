from pyecharts import Map, Geo, Bar, Page, Line
import data_analyze
import pandas,os
'''
生成各种报表
'''

def cvtSalaryArr(salaries):
    def cvtSalary(x):
        return round(x,1)*1000
    return list(map(cvtSalary, salaries))

def sort_dic(dic, sortField, ascending = False):
    data = pandas.DataFrame(dic)
    data = data.sort_values(sortField, ascending = ascending)
    ret_dic = data.to_dict('list')
    return ret_dic

def render(echarts, name):
    echarts.render(path=os.path.join(name+".html"))

def gen_table(tableName, x_name, keys, values):
    bar = Bar(tableName)
    bar.add(x_name, keys, values, is_label_show=True, xaxis_rotate=30)
    render(bar, tableName)
    return bar

def run():
    data_dict = data_analyze.education_jobcount_salary()
    gen_table("学历与职位数量", "职位数量", data_dict["keys"], data_dict["job_count"])

    data_dict = sort_dic(data_dict, "salary")
    gen_table("学历与薪资", "平均薪资", data_dict["keys"], cvtSalaryArr(data_dict["salary"]))

    data_dict = data_analyze.workYear_jobcount_salary()
    data_dict = sort_dic(data_dict, "salary")
    gen_table("工作年限与薪资", "平均薪资", data_dict["keys"], cvtSalaryArr(data_dict["salary"]))

if __name__ == "__main__":
    run()