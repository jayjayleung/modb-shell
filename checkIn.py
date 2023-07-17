#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from datetime import datetime
import time
import json
import sys
import os

COOKIE = os.getenv("COOKIE")
push_Token = os.getenv("PUSH_COOKIE")

# 填写对应参数的值
data = {
    'cookie': COOKIE
}

header = {
    "cookie": COOKIE,
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate,",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Length": "2",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "www.modb.pro",
    "Origin": "https://www.modb.pro",
    "Referer": "https://www.modb.pro/point/signin",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
    "sec-ch-ua-platform": "Windows"

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
    num = 1
    while COOKIE is not None:
        str = start()
        send(str)
        COOKIE = os.getenv("COOKIE"+num)
        num += 1
exit(0)
