# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 17:46
# @Author  : Sanzzi


from textblob import TextBlob

# 16: 3.22——4.06

path = '../dataset/Twitter_dailies/'

def Twitter_emotion():
    words = []
    with open(path + "2020-04-06/2020-04-06_top1000trigrams.csv", encoding='utf8') as file: # bigrams、trigrams
        for line in file:
            # print(line.split()[0]) # check　数据
            words.append(line.split()[0])

    del words[0] # 第一个删除

    with open(path + '2020-04-06/2020-04-06_top1000trigrams.txt', 'w', encoding='utf-8') as f:
        sum = 0
        len = 0
        for word in words:
            testimonial = TextBlob(word)
            if str(testimonial.sentiment.polarity) != '0.0' :
                sum += testimonial.sentiment.polarity
                len += 1
                f.write(str(testimonial.sentiment.polarity) + '\n')
        f.write('average:' + str(sum/len) + '\n')




# with open(path + '2020-03-22/2020-03-22_top1000trigrams.txt', 'w', encoding='utf-8') as f:
#     str_01 = ''
#     for i in range(len(words)):
#         if i % 100 != 0:
#             str_01 += words[i]
#         else:
#             testimonial = TextBlob(str_01)
#             f.write(str(testimonial.sentiment.polarity) + '\n')
#             str_01 = ''