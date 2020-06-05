# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 17:46
# @Author  : Sanzzi


import jiagu


path = '../dataset/raw_data/'
def emotions():
    text = []
    with open(path + "如何看待4月3日全球新冠确诊人数突破100万_我们需要多久才能控制住疫情_.csv", encoding='gbk',errors='ignore') as file:
        for line in file:
            line = line.split(',',1) # 只分一次
            text.append(line[1])
            # print(line[1])  # 数据的查看

    # print(len(text)) # 长度100001


    with open(path + '如何看待4月3日全球新冠确诊人数突破100万_我们需要多久才能控制住疫情_.txt', 'w', encoding='utf-8') as f:
        for i in range(len(text)):
            sentiment = jiagu.sentiment(text[i])
            f.write(str(sentiment) + '\n')
            # print(sentiment)

