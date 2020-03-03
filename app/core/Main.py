# -*- coding: utf-8 -*-

__author__='gyj2006@foxmail.com'

import datetime,random,uuid

from app.core.data.spider import *
import os
from wordcloud import WordCloud


def tid_maker():
    return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())+''.join([str(random.randint(1,10)) for i in range(5)])

#用于生成词云图并保存
def create_wordcloud(_dict):
    uid = uuid.uuid1().hex+'.png'
    result = {}
    result['data'] = _dict['string']

    if _dict['string'] is not '': #判断分词结果是否为空字符串，结束程序，避免发生错误
        fontpath='app/core/data/font/SourceHanSerifCN-Medium-6.otf'
        wc = WordCloud(font_path=fontpath,  # 设置字体
                background_color="white",  # 背景颜色
                random_state=42,
                scale=4 #图像缩放，增加清晰度
                )
        my_wordcloud = wc.generate_from_frequencies(_dict['frequencies']) #由于已经是经过处理的字典格式,可直接生成词云图
        my_wordcloud.to_file("app//image//{}".format(uid))
        result['path'] = "image/{}".format(uid)
        return result
    else: 
        return 'Empty Content!'


#网络爬取文档并作词云图的操作
def create_image_by_url(url,mode,Num):

    if url == '':
        return 'Empty Url!'

    if mode == 'BeautifulSoup': #两种不同的爬取模式
        context = bs4spider(url)
    else:
        context = smartspider(url)

    #进行分词
    result = split(''.join(context),mode,Num) #该函数集成度较高,可以在函数内完成指定模式分词与词组数量
    

    return create_wordcloud(result)
    
#本地读取文件并建图的操作
def create_image_by_text(text,mode,Num):
    #进行分词
    result = split(''.join(text),mode,Num) #该函数集成度较高,可以在函数内完成指定模式分词与词组数量

    print(type(result))
    
    return create_wordcloud(result)


