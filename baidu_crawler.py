# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     baidu_crawler
   Description :
   Author :       dik
   date：          2018/11/27
-------------------------------------------------
   Change Activity:
                   2018/11/27:
-------------------------------------------------
"""
__author__ = 'dik'

# coding = utf-8
import urllib.request
import re
import requests
import time

def getDatas(keyword, pages):
    params = []
    for i in range(30, 30 * pages + 30, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': i,
            'rn': 30,
            'gsm': '1e',
            '1526377465547': ''
        })

    url = 'https://image.baidu.com/search/index'
    urls = []
    for i in params:
        try:
            urls.append(requests.get(url, params=i).json().get('data'))
            print(urls)
        except Exception as e:
            print(e)
    return urls


def getImg(datalist, path):
    x = 0
    for list in datalist:
        for i in list:
            if i.get('thumbURL') != None:
                print('正在下载：%s' % i.get('thumbURL'))
                #如果报错停止10秒后再继续
                try:
                    urllib.request.urlretrieve(i.get('thumbURL'), path + '%d.jpg' % x)
                except Exception as e:
                    print(e)
                    time.sleep(10)
                x += 1
            else:
                print('图片链接不存在')

            time.sleep(2)  # 间隔2s，防止被封IP
if __name__ == '__main__':
    datalist = getDatas('狮子鱼', 15)#关键词，要爬的页数
    getImg(datalist, 'E:\\python\\shiziyu\\')