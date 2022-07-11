#!/usr/bin/env python      
# -*- coding: utf-8 -*-
# @Author  : ycli
# @Time    : 2022/7/11 11:24
# @File    : requests_demo.py
# @annotation    : requests 联系Demo
import re

import requests


def get_demo_1():
    '''
    get请求
    :return:
    '''
    # 设置请求url
    url = 'https://www.baidu.com'

    # 使用requests发起get请求
    r = requests.get(url)

    # 以文本形式输出请求结果
    print(r.text)

def get_demo_2():
    '''
    带参数的get请求
    :return:
    '''
    # 方式1，直接修改url
    url = 'https://www.baidu.com/s?wd=python'
    # 使用requests发起get请求
    r = requests.get(url)
    # 以文本形式输出请求结果
    print(r.text)

    # 方式2，添加请求参数
    # 设置请求url
    url = 'https://www.baidu.com/s'
    # 添加请求参数
    data = {
            'wd': 'python'
    }
    # 使用requests发起带参数的get请求
    r = requests.get(url,params=data)
    # 以文本形式输出请求结果
    print(r.text)

def get_demo_3():
    '''
    给请求添加头部信息，伪装成普通浏览器
    :return:
    '''
    # 直接使用get方法无法爬取到信息
    url = 'https://www.zhihu.com/explore'
    # 使用requests发起get请求
    r = requests.get(url)
    # 以文本形式输出请求结果
    print(r.text)

    # 添加头部信息后可正常获取信息
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
    }
    url = 'https://www.zhihu.com/explore'
    # 使用requests发起get请求
    r = requests.get(url,headers = headers)
    # 以文本形式输出请求结果
    print(r.text)


def get_demo_4():
    '''
    抓取网页信息并使用正则表达式解析
    :return:
    '''
    # 添加头部信息后可正常获取信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
    }
    url = 'https://www.zhihu.com/explore'
    # 使用requests发起get请求
    r = requests.get(url, headers=headers)
    pattern = re.compile('href="https://www\.zhihu\.com/question/.*?>(.*?)</a>',re.S)
    title = re.findall(pattern,r.text)
    print(title)

def get_demo_5():
    '''
    爬取非文本信息
    :return:
    '''
    # 设置请求url
    url = 'https://tse4-mm.cn.bing.net/th/id/OIP-C.RenGsxEEDdU4Rx7egl27qQHaHa?pid=ImgDet&rs=1'

    # 使用requests发起get请求
    r = requests.get(url)

    # 以二进制形式输出请求结果
    print(r.content)

def post_demo():
    '''
    post请求
    :return:
    '''
    # 设置请求url
    url = 'https://www.baidu.com'

    # 设置表单数据
    data = {
        'name':'germey'
    }

    # 使用requests发起post请求
    r = requests.post(url)

def response_demo():
    '''
    分析请求的响应信息
    :return:
    '''
    # 设置请求url
    url = 'https://www.baidu.com'

    # 使用requests发起get请求
    r = requests.get(url)

    # 输出响应信息
    print(r.status_code) # 状态码
    print(r.headers) # 响应头
    print(r.cookies) # cookies

if __name__ == '__main__':
    # GET请求
    # get_demo_1()

    # 带参数的GET请求
    # get_demo_2()

    # 给请求添加头部信息
    # get_demo_3()

    # 使用正则表达式解析
    # get_demo_4()

    # 爬取二进制信息
    # get_demo_5()

    # POST请求
    # post_demo()

    # 分析请求的响应信息
    response_demo()