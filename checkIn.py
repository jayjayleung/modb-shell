#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from datetime import datetime
import time
import json
import sys


# 填写对应参数的值
data = {
    'cookie': '值1'
}

header = {
    "cookie": data.get('cookie')
}

def sign_in():
    """
    请求签到接口
    :return: 
    """
    url = 'https://www.modb.pro/api/user/checkIn'
    r = requests.post(url, data, headers=header)
    # print(r.text)
    return json.loads(r.text)['operateMessage']

def start():
    """
    启动任务
    :return: 
    """
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sign_msg = sign_in()
    time.sleep(10)
    return "签到返回：" + sign_msg

def send(str):
    body = {
		"token": '值2',
		"title": '【xxx】墨天轮签到',
		"content": str
    }
    r = requests.post('http://www.pushplus.plus/send', data=body)
    print(json.loads(r.text))

if __name__ == "__main__":
    str = start()
    send(str)
exit(0)
