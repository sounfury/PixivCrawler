# -Time :2023/2/14 13:18
# -*- codeing =utf-8 -*-
import requests
import random
import time
import os
import browser_cookie3
import re
def download_(args):
    res, x, title = args
    headers = {
        'referer': 'https://www.pixiv.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
    }
    cookies = browser_cookie3.edge(domain_name='pixiv.net')
    proxy = '127.0.0.1:7890/'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }
    json0 = res.json()
    if not os.path.exists("E:/图片/" + x):
        os.mkdir("E:/图片/" + x)
        print("创建"+x+"文件夹成功")
    for j in range(len(json0["body"])):
        print(json0["body"][j]["urls"]["original"])
        k = json0["body"][j]["urls"]["original"]
        tu = requests.get(k, headers=headers, cookies=cookies, proxies=proxies).content
        gs = k.split('.')[-1]
        if any(c in title for c in '\/:*?"<>|'):
            title = re.sub(r'[\\/:*?"<>|]', '-', title)
        if len(json0["body"]) > 1:
            if not os.path.exists("E:/图片/" + x + '/' + title):
                os.mkdir("E:/图片/" + x + '/' + title)
            imgpath = "E:/图片/" + x + '/' + title + '/' + str(j) + '.' + gs
        else:
            imgpath = "E:/图片/" + x + '/' + title + '.' + gs
        with open(imgpath, 'wb') as fp:
            fp.write(tu)
        time.sleep(random.randint(1, 2))



