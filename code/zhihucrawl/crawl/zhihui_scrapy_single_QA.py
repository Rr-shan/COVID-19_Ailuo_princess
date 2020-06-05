# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 17:21
# @Author  : Sanzzi

import requests
from bs4 import BeautifulSoup
import json
import re

path = '../raw_data/'

def draw_ans(string):
    RE = re.compile('<[^>]*>')
    temp_list = RE.sub("", string).replace("\n", "").replace(" ","")
    return temp_list


def Crawl_answer():

    headers = {
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://www.zhihu.com',
        'referer': 'https://www.zhihu.com/question/388922853', # 修改
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    begin_url = 'https://www.zhihu.com/api/v4/questions/388922853/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=3&offset=0&platform=desktop&sort_by=default' #修改
    next_url = [begin_url]

    answers = []
    for url in next_url:
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.text, "lxml")
        content = str(soup.p).split("<p>")[1].split("</p>")[0]
        c = json.loads(content)
        answers += [draw_ans(item["content"]) for item in c["data"] if draw_ans(item["content"]) != ""]
        next_url.append(c["paging"]["next"])

        if c["paging"]["is_end"]:
            break

    i = 0
    with open(path + '5月10日全球共确诊新冠肺炎患者400万例_死亡20万例_目前全球情况如何.csv', 'w', encoding='utf-8') as f:
        for elem in range(len(answers)):
            f.write(answers[elem] + '\n')
            print(str(i)+':'+ answers[elem]) # check the items
            i += 1

    print(len(answers)) # check the answers number


def Crawl_answer_time():

    headers = {
        'accept-language': 'zh-CN,zh;q=0.9',
        'origin': 'https://www.zhihu.com',
        'referer': 'https://www.zhihu.com/question/388922853',  # 修改
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    begin_url = 'https://www.zhihu.com/api/v4/questions/388922853/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=3&offset=0&platform=desktop&sort_by=default'  # 修改
    next_url = [begin_url]

    answers = []
    data = []
    for url in next_url:
        html = requests.get(url, headers=headers)
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.text, "lxml")
        content = str(soup.p).split("<p>")[1].split("</p>")[0]
        c = json.loads(content)
        data += [item["ContentItem-time"] for item in c["data"] if item["ContentItem-time"] != ""]
        answers += [draw_ans(item["content"]) for item in c["data"] if draw_ans(item["content"]) != ""]
        next_url.append(c["paging"]["next"])

        if c["paging"]["is_end"]:
            break

    i = 0
    with open(path + '5月10日全球共确诊新冠肺炎患者400万例_死亡20万例_目前全球情况如何.csv', 'w', encoding='utf-8') as f:
        for elem in range(len(answers)):
            f.write(str(data[elem]) + ',' + answers[elem] + '\n')
            f.write(answers[elem] + '\n')
            print(str(i) + ':' + answers[elem])  # check the items
            i += 1

    print(len(answers))  # check the answers number