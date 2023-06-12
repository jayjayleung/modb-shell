#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from datetime import datetime
import time
import json
import sys
import os

COOKIE= os.getenv("COOKIE")
push_Token =  os.getenv("PUSH_COOKIE")

# 填写对应参数的值
data = {
    'cookie': COOKIE
}

header = {
    "cookie": COOKIE
}

def sign_in():
    """
    请求签到接口
    :return:
    """
    url = 'https://www.modb.pro/api/user/checkIn'
    r = requests.post(url, data, headers=header)
    print(r.text)
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
    if push_Token is None or push_Token == "":
        return
    body = {
		"token": push_Token,
		"title": '墨天轮签到',
		"content": str
    }
    r = requests.post('http://www.pushplus.plus/send', data=body)
    print(json.loads(r.text))

if __name__ == "__main__":
    str = start()
    send(str)
exit(0)
