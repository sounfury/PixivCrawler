# -Time :2023/2/14 13:18
# -*- codeing =utf-8 -*-
import requests
import random
import time
import os
def download_(res,headers,cookies,proxies,x,title):
    j = 0
    json0 = res.json()
    if not os.path.exists("E:/图片/" + x):
        os.mkdir("E:/图片/" + x)
    if (len(json0["body"])>1):
        if not os.path.exists("E:/图片/" + x+ '/' + title):
            os.mkdir("E:/图片/" + x+ '/' + title)
        while j < len(json0["body"]):
            print(json0["body"][j]["urls"]["original"])
            k = json0["body"][j]["urls"]["original"]
            tu = requests.get(k, headers=headers, cookies=cookies, proxies=proxies).content
            gs = k.split('.')[-1]
            imgpath = "E:/图片/" + x + '/' + title+'/'+str(j)+'.'+gs
            with open(imgpath, 'wb') as fp:
                fp.write(tu)
            time.sleep(random.randint(1, 2))
            j += 1
    else:
        print(json0["body"][j]["urls"]["original"])
        k = json0["body"][j]["urls"]["original"]
        tu = requests.get(k, headers=headers, cookies=cookies, proxies=proxies).content
        gs = k.split('.')[-1]
        imgpath = "E:/图片/" + x + '/' + title +'.' + gs
        with open(imgpath, 'wb') as fp:
            fp.write(tu)
        time.sleep(random.randint(1, 2))




