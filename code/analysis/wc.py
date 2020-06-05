# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 8:49
# @Author  : Sanzzi


import jieba
import wordcloud
import matplotlib.colors as colors


import imageio
mk = imageio.imread("heart.png")
w = wordcloud.WordCloud(mask=mk)
colormaps = colors.ListedColormap(['#FF0000','#FF7F50','#FFE4C4'])  # 换成自己喜欢的颜色


w = wordcloud.WordCloud(width=1000,
                        height=700,
                        colormap=colormaps,
                        background_color='white',
                        font_path='simkai.ttf',
                        mask=mk,
                        scale=15)

f = open('武汉加油.txt',encoding='gbk')
txt = f.read()
txtlist = jieba.lcut(txt)
string = " ".join(txtlist)

string = txt
w.generate(string)

w.to_file('武汉加油.png')
