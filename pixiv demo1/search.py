# -Time :2023/2/10 16:19
# -*- codeing =utf-8 -*-
import requests
import re
import browser_cookie3
import download
import safe
import concurrent.futures
def search__():
    re1 = re.compile('"width":.*?,"height":.*?,"pageCount":.*?,"bookmarkCount":(\d*),"likeCount":.*?')

    headers = {
        'referer': 'https://www.pixiv.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
    }

    safe.safe_()

    edge_cookie = browser_cookie3.edge(domain_name='pixiv.net')
    cookies = edge_cookie
    search_query = input("输入要搜索的对象：")
    bookmark_threshold = input("请输入收藏数阈值：")
    search_pages = input("请输入要搜索的页数：")
    current_page_number = 1
    url_template = "https://www.pixiv.net/ajax/search/artworks/{name}?word={name}&order=date_d&mode=all&p={num}&s_mode=s_tag&type=all"

    proxy = '127.0.0.1:7890/'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }

    with concurrent.futures.ThreadPoolExecutor(16) as executor:
            while current_page_number <= int(search_pages):
                search_url = url_template.format(name=search_query, num=current_page_number)
                response = requests.get(url=search_url, headers=headers, cookies=cookies, proxies=proxies)  # 打开搜索api
                json = response.json()
                i = 0
                while i < len(json["body"]["illustManga"]["data"]):  # 获取搜索页面各组图群的全部ID
                    artwork_id = json["body"]["illustManga"]["data"][i]["id"]
                    artwork_title = json["body"]["illustManga"]["data"][i]["title"]
                    pages_url = "https://www.pixiv.net/ajax/illust/" + artwork_id + "/pages?lang=zh"
                    pages_response = requests.get(pages_url, headers=headers, cookies=cookies, proxies=proxies)
                    artwork_url = "https://www.pixiv.net/artworks/" + artwork_id
                    artwork_response = requests.get(artwork_url, headers=headers, cookies=cookies, proxies=proxies)  # 打开详情页检索收藏数
                    bookmark_count = re.findall(re1, artwork_response.text)

                    if int(bookmark_count[0]) > int(bookmark_threshold):
                        print("已添加" + artwork_title + "到下载队列")
                        executor.submit(download.download_, (pages_response, search_query, artwork_title))

                    i += 1
                current_page_number += 1

    print(response.status_code)