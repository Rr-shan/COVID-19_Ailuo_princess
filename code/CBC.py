# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 17:46
# @Author  : Sanzzi


from textblob import TextBlob


# 加拿大CBC新闻报道

path = '../dataset/CBC/'

def text_notime():
    words = []
    with open(path + "news.csv", encoding='gbk',errors='ignore') as file:
        for line in file:
            # print(line) # check　数据
            words.append(line)

    del words[0]

    print(words)

    with open(path + 'news_result.txt', 'w', encoding='utf-8') as f:
        sum = 0
        len = 0
        for word in words:
            testimonial = TextBlob(word)
            if str(testimonial.sentiment.polarity) != '0.0' :
                sum += testimonial.sentiment.polarity
                len += 1
                f.write(str(testimonial.sentiment.polarity) + '\n')
        f.write('average:' + str(sum/len) + '\n')



# 按照时间顺序
def text_time():
    time = []
    words = []
    with open(path + "news_time_text.csv", encoding='gbk',errors='ignore') as file:
        for line in file:
            # print(line.split(',')[1]) # check　数据
            words.append(line.split(',')[1])
            time.append(line.split(',')[0].split()[0])
                # print(line.split(',')[0].split()[0])

    del words[0]
    del time[0]
    k = len(words)
        # print(words) # check

    with open(path + 'news_time_text_result_0.0.txt', 'w', encoding='utf-8') as f:
        sum = 0
        len = 0
        for i in range(k):
            # for word in words:
            testimonial = TextBlob(words[i])
            # if str(testimonial.sentiment.polarity) != '0.0' :
            #     sum += testimonial.sentiment.polarity
            #     len += 1
            #     f.write(str(testimonial.sentiment.polarity) + '\n')

            sum += testimonial.sentiment.polarity
            len += 1
            f.write(time[i] +","+ str(testimonial.sentiment.polarity) + '\n')
        f.write('average:' + str(sum/len) + '\n')

# text_time()


# title
def title_time():
    words = []
    with open(path + "news_time_title.csv", encoding='gbk',errors='ignore') as file:
        for line in file:
            # print(line.split(',')[1]) # check　数据
            words.append(line.split(',')[0])

    del words[0]
    # print(words) # check

    with open(path + 'news_time_title_result.txt', 'w', encoding='utf-8') as f:
        sum = 0
        len = 0
        for word in words:
            testimonial = TextBlob(word)
            if str(testimonial.sentiment.polarity) != '0.0' :
                sum += testimonial.sentiment.polarity
                len += 1
                f.write(str(testimonial.sentiment.polarity) + '\n')
        f.write('average:' + str(sum/len) + '\n')

# description
def description_time():
    words = []
    with open(path + "news_time_description.csv", encoding='gbk',errors='ignore') as file:
        for line in file:
            # print(line.split(',')[1]) # check　数据
            words.append(line.split(',')[1])

    del words[0]
    print(words) # check

    with open(path + 'news_time_description_result.txt', 'w', encoding='utf-8') as f:
        sum = 0
        len = 0
        for word in words:
            testimonial = TextBlob(word)
            if str(testimonial.sentiment.polarity) != '0.0' :
                sum += testimonial.sentiment.polarity
                len += 1
                f.write(str(testimonial.sentiment.polarity) + '\n')
        f.write('average:' + str(sum/len) + '\n')
