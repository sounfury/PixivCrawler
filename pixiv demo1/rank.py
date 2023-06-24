# -Time :2023/3/1 15:49
# -*- codeing =utf-8 -*-
import requests
import browser_cookie3
import download
import safe
import multiprocessing as mp
def rank__():
    pixiv_cookies = browser_cookie3.edge(domain_name='pixiv.net')
    safe.safe_()
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
    num_pages = int(input("请输入要查询的页数"))
    time_span = int(input("请选择时间跨度：1. 日，2. 周，3. 月 "))
    use_r18_mode = int(input("是否开启R18模式：1. 是，2. 否"))
    time = input("请输入要查询的时间，以20230227格式")
    current_page = 1
    while (num_pages> 0):
        if time_span == 1:
            url = "https://www.pixiv.net/ranking.php?mode=daily&date={}&p={}&format=json".format(time, current_page)
            if use_r18_mode:
                url = "https://www.pixiv.net/ranking.php?mode=daily_r18&date={}&p={}&format=json".format(time,
                                                                                                         current_page)
        elif time_span == 2:
            url = "https://www.pixiv.net/ranking.php?mode=weekly&date={}&p={}&format=json".format(time, current_page)
            if use_r18_mode:
                url = "https://www.pixiv.net/ranking.php?mode=weekly_r18&date={}&p={}&format=json".format(time,
                                                                                                          current_page)
        elif time_span == 3:
            url = "https://www.pixiv.net/ranking.php?mode=monthly&date={}&p={}&format=json".format(time, current_page)
        current_page += 1
        num_pages -= 1
        response = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies)
        print(response)
        json_data = response.json()
        download_args = []
        for i in range(len(json_data['contents'])):
            ID = str(json_data['contents'][i]['illust_id'])
            title = json_data['contents'][i]['title']
            URL = "https://www.pixiv.net/ajax/illust/" + ID + "/pages?lang=zh"
            print(URL)
            response2 = requests.get(URL, headers=headers, cookies=cookies, proxies=proxies)
            download_args.append((response2, time + "月排行榜", title))
        pool = mp.Pool(processes=8)
        pool.map(download.download_, download_args)# 根据您的系统资源调整进程数
        pool.close()
        pool.join()