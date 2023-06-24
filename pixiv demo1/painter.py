# -Time :2023/2/14 14:00
# -*- codeing =utf-8 -*-
import requests
import browser_cookie3
import safe
import re
import download
import multiprocessing as mp
def painter__():
    name=input("请输入画师id")
    url="https://www.pixiv.net/ajax/user/{}/profile/all?lang=zh".format(name)
    re1=re.compile(r'\d+')
    headers = {
            'referer': 'https://www.pixiv.net/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
        }

    safe.safe_()
    edge_cookie = browser_cookie3.edge(domain_name='pixiv.net')
    cookies = edge_cookie
    proxy = '127.0.0.1:7890/'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }
    res0=requests.get(url,headers=headers,cookies=cookies,proxies=proxies)#打开画师主页,获取id用的
    json=res0.json()
    s=re.findall(re1,str(json['body']['illusts']))#获取画师全部作品ID
    i=0
    download_args = []
    while i<len(s):
        ID = s[i]#获取画师全部作品ID
        URL = "https://www.pixiv.net/ajax/illust/" + ID
        URL2="https://www.pixiv.net/ajax/illust/" + ID + "/pages?lang=zh"
        print(URL)
        res1 = requests.get(URL, headers=headers, cookies=cookies, proxies=proxies)
        title = res1.json()["body"]["illustTitle"]
        res2= requests.get(URL2, headers=headers, cookies=cookies, proxies=proxies)
        download_args.append((res2,name,title))
        i+=1
    pool = mp.Pool(processes=8)
    pool.map(download.download_, download_args)
    pool.close()
    pool.join()


