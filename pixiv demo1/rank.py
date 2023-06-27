# -Time :2023/3/1 15:49
# -*- codeing =utf-8 -*-
import requests
import browser_cookie3
import download
import safe
import concurrent.futures
import time

def rank__():
    pixiv_cookies = browser_cookie3.edge(domain_name='pixiv.net')
    headers = {
        'referer': 'https://www.pixiv.net/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
    }
    cookies = pixiv_cookies
    proxy = '127.0.0.1:7890/'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }
    safe.safe_()

    num_pages = int(input("请输入要查询的页数"))
    time_span = int(input("请选择时间跨度：1. 日，2. 周，3. 月 "))
    use_r18_mode = int(input("是否开启R18模式：1. 是，2. 否"))
    time_ = input("请输入要查询的时间，以20230227格式")
    c_count=int(input("请输入每页要多少图片"))
    current_page = 1
    pages_crawled = 0
    with concurrent.futures.ThreadPoolExecutor(16) as executor:
        while pages_crawled < num_pages:
            if time_span == 1:
                url = "https://www.pixiv.net/ranking.php?mode=daily&date={}&p={}&format=json".format(time_, current_page)
                if use_r18_mode:
                    url = "https://www.pixiv.net/ranking.php?mode=daily_r18&date={}&p={}&format=json".format(time_, current_page)
            elif time_span == 2:
                url = "https://www.pixiv.net/ranking.php?mode=weekly&date={}&p={}&format=json".format(time_, current_page)
                if use_r18_mode:
                    url = "https://www.pixiv.net/ranking.php?mode=weekly_r18&date={}&p={}&format=json".format(time_, current_page)
            elif time_span == 3:
                url = "https://www.pixiv.net/ranking.php?mode=monthly&date={}&p={}&format=json".format(time_, current_page)
            current_page += 1
            response = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies)
            time.sleep(1)
            print(response)
            json_data = response.json()
            count=0
            for i in range(len(json_data['contents'])):
                ID = str(json_data['contents'][i]['illust_id'])
                title = json_data['contents'][i]['title']
                URL = "https://www.pixiv.net/ajax/illust/" + ID + "/pages?lang=zh"
                print("已添加" + title + "到下载队列")
                response2 = requests.get(URL, headers=headers, cookies=cookies, proxies=proxies)
                time.sleep(1)
                executor.submit(download.download_, (response2, time_ + "月排行榜", title))
                count+=1
                if count>=c_count:
                    pages_crawled += 1
                    break

    print("已完成爬取{}页".format(num_pages))
