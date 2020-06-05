# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 13:46
# @Author  : Sanzzi


import jiagu
from snownlp import SnowNLP

path = '../dataset/'


def keywords():
    f = open(path + '政府的救助措施.txt',encoding='gbk') # 疫情传播、疫情防控、疫情救治、疫情对经济的影响、政府的救助措施
    text = f.read()
    n = 10 # keywords_nums

    # SnowNLP
    s = SnowNLP(text)
    print(s.keywords(n))
    # jiagu
    keywords = jiagu.keywords(text, n) # 关键词
    print(keywords)

'''
疫情传播:  
'媒体', '武汉', '新闻', '直播', '公众', '用户', '自媒体','社会'

疫情防控：
'国家', '民警', '医护', '分局', '人员','工作','防控','部门','口罩'

疫情救治:
'感染', '肺炎','医院', '病毒','全国','疫情', '中国','医生', '患者'

疫情对经济的影响:
'疫情', '企业', '经济','消费', '产业', '行业', '需求', '政策', '发展'

政府的救助措施:
'企业', '政策', '支持' ,'贷款', '缴纳', '金融','行业', '机构', '发展'
'''