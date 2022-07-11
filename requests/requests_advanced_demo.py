#!/usr/bin/env python      
# -*- coding: utf-8 -*-
# @Author  : ycli
# @Time    : 2022/7/11 15:06
# @File    : requests_advanced_demo.py
# @annotation    : reqeuests库的高级使用demo
import requests
from requests.auth import HTTPBasicAuth
from requests import Request


def file_upload():
    '''
    文件上传示例
    :return:
    '''
    # 设置请求url
    url = 'https://www.baidu.com'

    # 打开上传的文件
    f = open('1.png','rb')

    # 添加file参数
    file = {'file':f}

    # 发起post请求
    r = requests.post(url,file=file)

    # 关闭文件
    f.close()

def session_persistence():
    '''
    维持一个会话，使用Session对象可以维持一个会话，这样在访问同一网站的不同网页时不用每次都设置Cookies，只需在第一次访问时设置Cookies即可
    :return:
    '''
    # 添加头部信息后可正常获取信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
        'cookies':'KLBRSID=3d7feb8a094c905a519e532f6843365f|1657523959|1657521968; Path=/'
    }

    # 设置url
    url = 'https://www.zhihu.com/explore'

    # 实例化session对象
    s = requests.Session()

    # 使用session发起get请求
    r = s.get(url, headers=headers)

    # 显示响应结果
    print(r.text)

    # 使用session发起get请求，不添加cookies信息
    r = s.get(url)

    # 显示响应结果
    print(r.text)

def SSL():
    '''
    忽略SSL证书认证
    :return:
    '''
    # 设置url
    url = 'https://www.zhihu.com/explore'

    # 使用requests发起get请求
    r = requests.get(url,verify= False)

    # 以文本形式输出请求结果
    print(r.text)

def proxy_setting():
    '''
    代理设置
    :return:
    '''
    # 设置url
    url = 'https://www.zhihu.com/explore'

    # 设置代理
    proxies = {
        'http':'127.0.0.1',
        'https':'127.0.0.1'
    }

    # 使用requests发起get请求
    r = requests.get(url, proxies=proxies)

    # 以文本形式输出请求结果
    print(r.text)

def timeout_demo():
    '''
    超时设置
    :return:
    '''

    # 设置url
    url = 'https://www.zhihu.com/explore'

    # 使用requests发起get请求
    r = requests.get(url,timeout=1)

    # 以文本形式输出请求结果
    print(r.text)

def user_demo():
    '''
    身份认证
    :return:
    '''
    # 设置url
    url = 'https://www.zhihu.com/explore'

    # 使用requests发起get请求
    r = requests.get(url, auth=HTTPBasicAuth('username','password'))
    # 简写
    # r = requests.get(url, auth=('username', 'password'))

    # 以文本形式输出请求结果
    print(r.text)

def prepared_request():
    '''
    构造request对象
    :return:
    '''
    # 添加头部信息后可正常获取信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
        'cookies': 'KLBRSID=3d7feb8a094c905a519e532f6843365f|1657523959|1657521968; Path=/'
    }

    # 设置url
    url = 'https://www.zhihu.com/explore'

    # 实例化session对象
    s = requests.Session()

    # 构造Request对象
    req = Request(url, headers=headers)

    # 使用session发起get请求
    r = s.get(req)

    # 显示响应结果
    print(r.text)


if __name__ == '__main__':
    # 文件上传
    # file_upload()

    # 会话维持
    # session_persistence()

    # 忽略SSL证书认证
    # SSL()

    # 代理设置
    # proxy_setting()

    # 用户认证
    # user_demo()

    # 构造request对象
    prepared_request()