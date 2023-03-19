# -Time :2023/3/1 15:49
# -*- codeing =utf-8 -*-
import requests
import download
import safe
def rank__():
    safe.safe_()
    headers = {
                'referer': 'https://www.pixiv.net/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
            }
    cookies = "your-cookie"
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
    proxy = '127.0.0.1:7890/'
    proxies = {
            'http': 'http://' + proxy,
            'https': 'http://' + proxy
        }
    page=input("请输入要查询的页数")
    z=input("请选择时间跨度           1，日          2.周        3.月 ")
    w=input("是否开启r18模式        1.是     2.否")
    time=input("请输入要查询的时间，以20230227格式")
    x=int(page)
    y=1
    if (int(z) == 1):
        url = "https://www.pixiv.net/ranking.php?mode=daily&date={}&p={}&format=json".format(time, y)
        if(int(w)):
            url = "https://www.pixiv.net/ranking.php?mode=daily_r18&date={}&p={}&format=json".format(time, y)
    if (int(z) == 2):
        url = "https://www.pixiv.net/ranking.php?mode=weekly&date={}&p={}&format=json".format(time, y)
        if (int(w)):
            url = "https://www.pixiv.net/ranking.php?mode=weekly_r18&date={}&p={}&format=json".format(time, y)
    if (int(z) == 3):
        url = "https://www.pixiv.net/ranking.php?mode=monthly&date={}&p={}&format=json".format(time, y)
    while(x):
     y+=1
     x-=1
     res=requests.get(url=url,headers=headers,cookies=cookies,proxies=proxies)
     js=res.json()
     for i in range(49):
        ID=str(js['contents'][i]['illust_id'])
        title=js['contents'][i]['title']
        URL = "https://www.pixiv.net/ajax/illust/" + ID + "/pages?lang=zh"
        res2 = requests.get(URL, headers=headers, cookies=cookies, proxies=proxies)
        download.download_(res2, headers, cookies, proxies, time+"月排行榜", title)