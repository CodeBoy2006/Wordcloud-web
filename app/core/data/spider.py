# -*- coding: utf-8 -*-

import collections
import re

import jieba.analyse
import requests
from bs4 import BeautifulSoup
from newspaper import Article


#用newspaper库智能爬取网页数据
def smartspider(url):
    try:
        news = Article(url, language='zh')

        news .download()  #先下载
        news .parse()    #再解析

        print('context= '+str(news.text)) #新闻正文
        return str(news.text)
    except:
        print('URL出错')
        return ''

#用 BeautifulSoup4 来爬取数据
def bs4spider(url):
    try:
        newsurl = url
        res = requests.get(newsurl)
        res.encoding = 'utf-8'

        soup = BeautifulSoup(res.text, 'html.parser')
        article = []
        for p in soup.select('.art_p')[:-1]:
            article.append(p.text.strip())
        ''.join(article)
        print('context= '+str(article))
        return str(article)
    except:
        print('URL出错')
        return ''

#2019/12/18新增函数,经过本人剖析源代码,发现优化方案:
#该函数生成一个字典用于直接生成词云图,不需通过wordcloud库自带的字频统计功能,实现单字词云图，提高效率。
def make_fake_frequencies(textlist):
    frequencies = {}
    for n in textlist:
        frequencies[n]=1 #由于事先经过统计,词频全部记为一对最终结果无影响

    return frequencies

def collection_characters(text,num):
    rule = re.compile(r"[^a-zA-Z0-9\u4e00-\u9fa5]")
    text = rule.sub('',text)
    mylist = list(str(text))
    mycount = collections.Counter(mylist)
    words = []
    reslut = {} #最终返回的数组由两部分组成,用于生成词云图的字典与便于用户识别的字符串
    for key, val in mycount.most_common(num):  # 有序（返回前150个）
        print(key, val)
        words.append(key)
    # print(reslut)
    # print(type(' '.join(reslut)))
    reslut['string']=' '.join(words)
    reslut['frequencies']=make_fake_frequencies(words)
    return reslut

def jiebaclearText(text,num):
    reslut = {} #最终返回的数组由两部分组成,用于生成词云图的字典与便于用户识别的字符串
    stopwords_path = 'app/core/data/stopwords/stopwords_baidu.txt' # 停用词词表
    #摒弃老旧的方法，使用 jieba 库智能提取前150个关键词
    jieba.analyse.set_stop_words(stopwords_path)
    tags = jieba.analyse.extract_tags(text,num)
    print(tags)
    reslut['string']=' '.join(tags)
    reslut['frequencies']=make_fake_frequencies(tags)
    return reslut

def split(string,mode,num):
    if mode == 'words':
        reslut = jiebaclearText(string,num)
    else:
        reslut = collection_characters(string,num)

    print(reslut['string'])
    return reslut




