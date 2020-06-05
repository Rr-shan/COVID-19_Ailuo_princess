# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 16:42
# @Author  : sanzzi

from snownlp import SnowNLP

path = '../dataset/'

text = []

def weibo_emotions():

    r3 = ['`','；','，','·','～',' ','』','『','：','“','”','.','!','/','_','$','&','%','^','*','（','）','(',')','<','>','+','?','@','#','-','|',':','~','{','}',']','+','|','丨','[','——','—','！','"','。','？','、',':','‘','’','《','》','【','】','…']
    with open(path + "nCoV_900k.csv", encoding='gbk',errors='ignore') as file:
    # 这两种编码都不行
    # with open(path + "nCoV_100k.csv", encoding='utf8') as file:
        for line in file:
            line = line.split(',',1) # 只分一次
            line[0] = line[0].split()[0]
            # line[0]是 str
            # print(line[0])
            # 去除一些无用的符号
            for i in r3:
                line[1] = line[1].replace(i,'')
            '''
            # line[1] = [jieba.cut(words) for words in line[1]]
            # line[1] = [' '.join(word) for word in line[1]]
            '''
            text.append(line[0] +','+ line[1])
            # print(line[1])  # 数据的查看
    # print(len(text))


    da = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18']
    for kk in da:
        print(kk)
        words = []
        for i in text:
            list = i.split(',')
            if list[0] == '02月'+ kk +'日':
                if list[1] != '':
                    words.append(list[1])
            # print(list[1])

        print(len(words))

        sum = 0
        with open(path + '02'+kk+'.txt', 'w', encoding='utf-8') as f:
            for i in range(len(words)):
                sentiment = SnowNLP(words[i])
                sum += sentiment.sentiments
                f.write(str(sentiment.sentiments) + '\n')
            f.write('\n'+'\n'+"average:"+str(sum/len(words)))

        with open(path + 'average_01.txt', 'a', encoding='utf-8') as f:
            f.write('\n' + "02"+kk+":" + str(sum / len(words))  )

        print(sum/len(words))





def zhihu_emotions():

    remove = ['=',',',' ','`','；','，','·','～',' ','』','『','：','“','”','.','!','/','_','$','&','%','^','*','（','）','(',')','<','>','+','?','@','#','-','|',':','~','{','}',']','+','|','丨','[','——','—','！','"','。','？','、',':','‘','’','《','》','【','】','…']

    text = []
    with open(path +'raw_data/'+ "如何看待世界疫情对中国经济的影响.csv", encoding='gbk',errors='ignore') as file:
        for line in file:
            line = line.split(',',1) # once
            for i in remove:
                line[1] = line[1].replace(i,'')
            print(line[1])
            text.append(line[1])

    print(len(text)) # check the length

    sum = 0
    with open(path +'raw_data/'+ '如何看待世界疫情对中国经济的影响.txt', 'w', encoding='utf-8') as f:
        f.write("answer_nums:" + str(len(text)) + '\n' + '\n')
        for i in range(len(text)):
            sentiment = SnowNLP(text[i])
            sum += sentiment.sentiments
            f.write(str(sentiment.sentiments) + '\n')
            # print(sentiment) # check
        f.write('\n' + "average:"+str(sum/len(text)) + '\n')

    print(sum/len(text)) # check the average














'''
# 
# 计算出数据！
# num = [1019,1011,1083,1017,1020,1089,1100,1076,1106,1037,1027,958,1067,1022,1120,1027,1013,1000,1170,1542,2001,2023,
#        2333,2370,2530,2572,2610,2664,2582,2573,2485,2712,2836,2846,2838,2708,2847,2943,2789,2953,2870,2910,3128,2949,
#        2850,2837,2880,2937,3002]
# 
# 
# day = ['01月01日','01月02日','01月03日','01月04日','01月05日','01月06日','01月07日','01月08日','01月09日',
#        '01月10日','01月11日','01月12日','01月13日','01月14日','01月15日','01月16日','01月17日','01月18日',
#        '01月19日','01月20日','01月21日','01月22日','01月23日','01月24日','01月25日','01月26日','01月27日',
#        '01月28日','01月29日','01月30日','01月31日','02月01日','02月02日','02月03日','02月04日','02月05日',
#        '02月06日','02月07日','02月08日','02月09日','02月10日','02月11日','02月12日','02月13日','02月14日',
#        '02月15日','02月16日','02月17日','02月18日']
# 
# sum = 0
# for i in num:
#     sum += i
# 
# print(sum)
# # 99999
# # 100082
'''
