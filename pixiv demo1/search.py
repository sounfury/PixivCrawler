# -Time :2023/2/10 16:19
# -*- codeing =utf-8 -*-
import requests
import re
import browser_cookie3
import download
import safe
def search__():
    re1 = re.compile('"width":.*?,"height":.*?,"pageCount":.*?,"bookmarkCount":(\d*),"likeCount":.*?')

    headers = {
        'referer': 'https://www.pixiv.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
    }

    safe.safe_()

    edge_cookie = browser_cookie3.edge(domain_name='pixiv.net')
    cookies=edge_cookie
    x = input("输入要搜索的对象")
    y = input("请输入收藏数")
    e=input("请输入页数")
    z = 1
    url = "https://www.pixiv.net/ajax/search/artworks/{name}?word={name}&order=date_d&mode=all&p={num}&s_mode=s_tag&type=all"

    proxy = '127.0.0.1:7890/'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }
    while z <= int(e):
        newurl = url.format(name=x, num=z)
        response = requests.get(url=newurl, headers=headers, cookies=cookies, proxies=proxies)#打开搜索api
        json = response.json()
        i = 0
        while i < len(json["body"]["illustManga"]["data"]):#获取搜索页面各组图群的全部ID
            ID = json["body"]["illustManga"]["data"][i]["id"]
            title=json["body"]["illustManga"]["data"][i]["title"]
            URL = "https://www.pixiv.net/ajax/illust/" + ID + "/pages?lang=zh"
            res = requests.get(URL, headers=headers, cookies=cookies, proxies=proxies)
            url2 = "https://www.pixiv.net/artworks/" + ID
            res2 = requests.get(url2, headers=headers, cookies=cookies, proxies=proxies)#打开详情页检索收藏数
            bookmark = re.findall(re1, res2.text)

            if int(bookmark[0])> int(y):
                download.download_(res,x,title)

            i += 1
        z+=1

    print(response.status_code)

