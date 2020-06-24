from django.shortcuts import render

# Create your views here.

from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.charts import Bar
from analysis import models
from collections import Counter
import jieba.analyse
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))


def index(request):
    # all_list = models.Zhipin.objects.values_list('technology', flat=True)
    # technology_list = []
    # with open('word_count.txt','w',encoding='utf-8') as f:
    #     for lists in all_list:
    #         technology = "".join(lists)
    #         f.write(technology)
    # technology = []
    # word_dict = {}
    # data_pair = []
    # with open('word_count.txt', "r", encoding='utf-8') as f:
    #     data = f.read()
    #     technology.append(data.split(';'))
    #     for word in technology[0]:
    #         if word not in word_dict:
    #             word_dict[word] = 1
    #         else:
    #             word_dict[word] += 1
    # # print(word_dict)
    #
    # for k, v in word_dict.items():
    #     data_pair.append((k, v))
    #
    # c = (
    #     WordCloud()
    #         .add(series_name="热点分析", data_pair=data_pair, word_size_range=[6, 66])
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
    #         ),
    #         tooltip_opts=opts.TooltipOpts(is_show=True),
    #     )
    #         . render("wordcloud.html")
    # )
    return render(request, 'wordcloud.html')


def base(request):
    return render(request, 'base.html')


def python_technology(request):
    # all_list = models.Zhipin.objects.filter(keyword='python').values_list('technology', flat=True)
    # technology_list = []
    # with open('python_word_count.txt','w',encoding='utf-8') as f:
    #     for lists in all_list:
    #         technology = "".join(lists)
    #         f.write(technology)
    # technology = []
    # word_dict = {}
    # data_pair = []
    # with open('python_word_count.txt', "r", encoding='utf-8') as f:
    #     data = f.read()
    #     technology.append(data.split(';'))
    #     for word in technology[0]:
    #         if word not in word_dict:
    #             word_dict[word] = 1
    #         else:
    #             word_dict[word] += 1
    # # print(word_dict)
    #
    # for k, v in word_dict.items():
    #     data_pair.append((k, v))
    #
    # c = (
    #     WordCloud()
    #         .add(series_name="热点分析", data_pair=data_pair, word_size_range=[6, 66])
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
    #         ),
    #         tooltip_opts=opts.TooltipOpts(is_show=True),
    #     )
    #         . render("python_wordcloud.html")
    # )
    return render(request, 'python_wordcloud.html')


def java_technology(request):
    # all_list = models.Zhipin.objects.filter(keyword='java').values_list('technology', flat=True)
    # technology_list = []
    # with open('java_word_count.txt','w',encoding='utf-8') as f:
    #     for lists in all_list:
    #         technology = "".join(lists)
    #         f.write(technology)
    # technology = []
    # word_dict = {}
    # data_pair = []
    # with open('java_word_count.txt', "r", encoding='utf-8') as f:
    #     data = f.read()
    #     technology.append(data.split(';'))
    #     for word in technology[0]:
    #         if word not in word_dict:
    #             word_dict[word] = 1
    #         else:
    #             word_dict[word] += 1
    # # print(word_dict)
    #
    # for k, v in word_dict.items():
    #     data_pair.append((k, v))
    #
    # c = (
    #     WordCloud()
    #         .add(series_name="java分析", data_pair=data_pair, word_size_range=[6, 66])
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="java分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
    #         ),
    #         tooltip_opts=opts.TooltipOpts(is_show=True),
    #     )
    #         . render("java_wordcloud.html")
    # )
    return render(request, 'java_wordcloud.html')


def data_technology(request):
    # all_list = models.Zhipin.objects.filter(keyword='大数据').values_list('technology', flat=True)
    # technology_list = []
    # with open('data_word_count.txt','w',encoding='utf-8') as f:
    #     for lists in all_list:
    #         technology = "".join(lists)
    #         f.write(technology)
    # technology = []
    # word_dict = {}
    # data_pair = []
    # with open('data_word_count.txt', "r", encoding='utf-8') as f:
    #     data = f.read()
    #     technology.append(data.split(';'))
    #     for word in technology[0]:
    #         if word not in word_dict:
    #             word_dict[word] = 1
    #         else:
    #             word_dict[word] += 1
    # # print(word_dict)
    #
    # for k, v in word_dict.items():
    #     data_pair.append((k, v))
    #
    # c = (
    #     WordCloud()
    #         .add(series_name="大数据分析", data_pair=data_pair, word_size_range=[6, 66])
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="大数据分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
    #         ),
    #         tooltip_opts=opts.TooltipOpts(is_show=True),
    #     )
    #         . render("data_wordcloud.html")
    # )
    return render(request, 'data_wordcloud.html')


def Android_technology(request):
    # all_list = models.Zhipin.objects.filter(keyword='Android').values_list('technology', flat=True)
    # technology_list = []
    # with open('Android_word_count.txt','w',encoding='utf-8') as f:
    #     for lists in all_list:
    #         technology = "".join(lists)
    #         f.write(technology)
    # technology = []
    # word_dict = {}
    # data_pair = []
    # with open('Android_word_count.txt', "r", encoding='utf-8') as f:
    #     data = f.read()
    #     technology.append(data.split(';'))
    #     for word in technology[0]:
    #         if word not in word_dict:
    #             word_dict[word] = 1
    #         else:
    #             word_dict[word] += 1
    # # print(word_dict)
    #
    # for k, v in word_dict.items():
    #     data_pair.append((k, v))
    #
    # c = (
    #     WordCloud()
    #         .add(series_name="Android分析", data_pair=data_pair, word_size_range=[6, 66])
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="Android分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
    #         ),
    #         tooltip_opts=opts.TooltipOpts(is_show=True),
    #     )
    #         . render("Android_wordcloud.html")
    # )
    return render(request, 'Android_wordcloud.html')


def algorithm_technology(request):
    # all_list = models.Zhipin.objects.filter(keyword='算法').values_list('technology', flat=True)
    # technology_list = []
    # with open('algorithm_word_count.txt','w',encoding='utf-8') as f:
    #     for lists in all_list:
    #         technology = "".join(lists)
    #         f.write(technology)
    # technology = []
    # word_dict = {}
    # data_pair = []
    # with open('algorithm_word_count.txt', "r", encoding='utf-8') as f:
    #     data = f.read()
    #     technology.append(data.split(';'))
    #     for word in technology[0]:
    #         if word not in word_dict:
    #             word_dict[word] = 1
    #         else:
    #             word_dict[word] += 1
    # # print(word_dict)
    #
    # for k, v in word_dict.items():
    #     data_pair.append((k, v))
    #
    # c = (
    #     WordCloud()
    #         .add(series_name="算法技术分析", data_pair=data_pair, word_size_range=[6, 66])
    #         .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title="算法技术分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
    #         ),
    #         tooltip_opts=opts.TooltipOpts(is_show=True),
    #     )
    #         . render("algorithm_wordcloud.html")
    # )
    return render(request, 'algorithm_wordcloud.html')


def min_average_wages(request):
    # data_pair = []
    # # python 平均最低工资
    # python_test = []
    # python_sum = 0.0
    # python_list = models.Zhipin.objects.filter(keyword='python', wages__contains='K').values_list('wages', flat=True)
    # for python_all in python_list:
    #     wage = python_all.split('-')
    #     python_test.append(wage[0])
    #
    # for i in range(len(python_test)):
    #     x = eval(python_test[i])
    #     python_sum = python_sum + x
    #
    # python_average = round(python_sum/len(python_test), 2)
    # print(python_average)
    # data_pair.append(python_average)
    #
    # # java平均最低工资
    # java_test = []
    # java_sum = 0.0
    # java_list = models.Zhipin.objects.filter(keyword='java', wages__contains='K').values_list('wages', flat=True)
    # for java_all in java_list:
    #     wage = java_all.split('-')
    #     java_test.append(wage[0])
    #
    # for i in range(len(java_test)):
    #     x = eval(java_test[i])
    #     java_sum = java_sum + x
    #
    # java_average = round(java_sum / len(java_test), 2)
    # print(java_average)
    # data_pair.append(java_average)
    #
    # # 大数据平均最低工资
    # data_test = []
    # data_sum = 0.0
    # data_list = models.Zhipin.objects.filter(keyword='大数据', wages__contains='K').values_list('wages', flat=True)
    # for data_all in data_list:
    #     wage = data_all.split('-')
    #     data_test.append(wage[0])
    #
    # for i in range(len(data_test)):
    #     x = eval(data_test[i])
    #     data_sum = data_sum + x
    #
    # data_average = round(data_sum / len(data_test), 2)
    # print(data_average)
    # data_pair.append(data_average)
    #
    # # Android平均最低工资
    # android_test = []
    # android_sum = 0.0
    # android_list = models.Zhipin.objects.filter(keyword='Android', wages__contains='K').values_list('wages', flat=True)
    # for android_all in android_list:
    #     wage = android_all.split('-')
    #     android_test.append(wage[0])
    #
    # for i in range(len(android_test)):
    #     x = eval(android_test[i])
    #     android_sum = android_sum + x
    #
    # android_average = round(android_sum / len(android_test), 2)
    # print(android_average)
    # data_pair.append(android_average)
    #
    # # 算法平均最低工资
    # algorithm_test = []
    # algorithm_num = 0.0
    # algorithm_list = models.Zhipin.objects.filter(keyword='算法', wages__contains='K').values_list('wages', flat=True)
    # for algorithm_all in algorithm_list:
    #     wage = algorithm_all.split('-')
    #     algorithm_test.append(wage[0])
    #
    # for i in range(len(algorithm_test)):
    #     x = eval(algorithm_test[i])
    #     algorithm_num = algorithm_num + x
    #
    # algorithm_average = round(algorithm_num / len(algorithm_test), 2)
    # print(algorithm_average)
    # data_pair.append(algorithm_average)
    # c = (
    #     Bar()
    #         .add_xaxis(["python", "java", "大数据", "Android", "算法"])
    #         .add_yaxis("平均最低工资/K", data_pair)
    #         .set_global_opts(title_opts=opts.TitleOpts(title="技术平均最低工资"))
    #         .render("min_average_wages.html")
    # )
    return render(request, 'min_average_wages.html')


def max_average_wages(request):
    # data_pair = []
    # # python 平均最低工资
    # python_test = []
    # python_sum = 0.0
    # python_list = models.Zhipin.objects.filter(keyword='python', wages__contains='K').values_list('wages', flat=True)
    # for python_all in python_list:
    #     wage = python_all.split('-')[1].split('K')
    #     python_test.append(wage[0])
    #
    # for i in range(len(python_test)):
    #     x = eval(python_test[i])
    #     python_sum = python_sum + x
    #
    # python_average = round(python_sum/len(python_test), 2)
    # print(python_average)
    # data_pair.append(python_average)
    #
    # # java平均最低工资
    # java_test = []
    # java_sum = 0.0
    # java_list = models.Zhipin.objects.filter(keyword='java', wages__contains='K').values_list('wages', flat=True)
    # for java_all in java_list:
    #     wage = java_all.split('-')[1].split('K')
    #     java_test.append(wage[0])
    #
    # for i in range(len(java_test)):
    #     x = eval(java_test[i])
    #     java_sum = java_sum + x
    #
    # java_average = round(java_sum / len(java_test), 2)
    # print(java_average)
    # data_pair.append(java_average)
    #
    # # 大数据平均最低工资
    # data_test = []
    # data_sum = 0.0
    # data_list = models.Zhipin.objects.filter(keyword='大数据', wages__contains='K').values_list('wages', flat=True)
    # for data_all in data_list:
    #     wage = data_all.split('-')[1].split('K')
    #     data_test.append(wage[0])
    #
    # for i in range(len(data_test)):
    #     x = eval(data_test[i])
    #     data_sum = data_sum + x
    #
    # data_average = round(data_sum / len(data_test), 2)
    # print(data_average)
    # data_pair.append(data_average)
    #
    # # Android平均最低工资
    # android_test = []
    # android_sum = 0.0
    # android_list = models.Zhipin.objects.filter(keyword='Android', wages__contains='K').values_list('wages', flat=True)
    # for android_all in android_list:
    #     wage = android_all.split('-')[1].split('K')
    #     android_test.append(wage[0])
    #
    # for i in range(len(android_test)):
    #     x = eval(android_test[i])
    #     android_sum = android_sum + x
    #
    # android_average = round(android_sum / len(android_test), 2)
    # print(android_average)
    # data_pair.append(android_average)
    #
    # # 算法平均最低工资
    # algorithm_test = []
    # algorithm_num = 0.0
    # algorithm_list = models.Zhipin.objects.filter(keyword='算法', wages__contains='K').values_list('wages', flat=True)
    # for algorithm_all in algorithm_list:
    #     wage = algorithm_all.split('-')[1].split('K')
    #     algorithm_test.append(wage[0])
    #
    # for i in range(len(algorithm_test)):
    #     x = eval(algorithm_test[i])
    #     algorithm_num = algorithm_num + x
    #
    # algorithm_average = round(algorithm_num / len(algorithm_test), 2)
    # print(algorithm_average)
    # data_pair.append(algorithm_average)
    # c = (
    #     Bar()
    #         .add_xaxis(["python", "java", "大数据", "Android", "算法"])
    #         .add_yaxis("平均最高工资/K", data_pair)
    #         .set_global_opts(title_opts=opts.TitleOpts(title="技术平均最高工资"))
    #         .render("max_average_wages.html")
    # )
    return render(request, 'max_average_wages.html')




