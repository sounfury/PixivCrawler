# -Time :2023/2/14 14:00
# -*- codeing =utf-8 -*-
import requests
import safe
import re
import download
def painter__():
    name=input("请输入画师id")
    url="https://www.pixiv.net/ajax/user/{}/profile/all?lang=zh".format(name)
    url1="https://www.pixiv.net/ajax/user/{}/profile/top?lang=zh".format(name)
    re1=re.compile(r'\d+')
    headers = {
            'referer': 'https://www.pixiv.net/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
        }

    safe.safe_()

    cookies = "first_visit_datetime_pc=2022-12-21+20%3A07%3A56; yuid_b=dkR2kRA; p_ab_id=6; p_ab_id_2=5; p_ab_d_id=310520654; __utmz=235335808.1671620879.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=50386531_QX9xhdUHcQlIHtMw6NpDnpzuJ92uuxP1; privacy_policy_agreement=5; _ga_MZ1NL4PHH0=GS1.1.1671620888.1.0.1671620894.0.0.0; c_type=24; privacy_policy_notification=0; a_type=0; b_type=0; __utmv=235335808.|3=plan=normal=1^6=user_id=50386531=1^11=lang=zh=1; _fbp=fb.1.1671620898472.33793616; adr_id=r2RYduMA5s5Qcl5iIJIqyaGgZVkKOTCC5ORanpnVORtKvjZr; _im_vid=01GMT5XJZRPQR1QTGGVTZA51YW; tag_view_ranking=0xsDLqCEW6~NsbQEogeyL~ML8s4PH95U~tIthLEM_gP~sRQy4rKivk~XuyGDA99Fy~7DE47SDNsq~1ZVO4Xhgk4~_hSAdpN9rx~qoS-Wwt3vy~PBc5N-_lhj~xNNQ5EFViW~Mp95LfB2KZ~gCB7z_XWkp~7Fffe9XHNn~JQAXuOnb_K~x_UimhvMir~5oPIfUbtd6~LiKCwPE0p2~ujS7cIBGO-~NTGKRMt6r7~4QveACRzn3~MM6RXH_rlN~s1DI4r3R9d~BXJoC8jDBr~o0zABn6q7p~RokSaRBUGr~5-XlMRdlZg~Ti1gvrVQFO~CkDjyRo6Vc~m6OUVhtqNR~IZhlWAh6lN~F8u6sord4r~bXMh6mBhl8~h7pIblggQz~Ngi2xRu_X4~D1cQAh66ix~oQVi_isie4~liM64qjhwQ~QJ0EuFHij-~DADQycFGB0~n5N_kcq8gx~eVxus64GZU~LX3_ayvQX4~nInT2dTMR6~MuYMXFwtWv~4LfBhWYcxv~ouiK2OKQ-A~Ie2c51_4Sp~qF9TK-b6N_~vdbd7LdFLQ~hoz0Zlsd-n~6o6m4yJCaj~8ch4HlASni~e_NH0RuRiq~6DKdJTDKfY; __utma=235335808.1082663053.1671620879.1671620879.1675072374.2; p_b_type=1; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; __cf_bm=W09DcLWdHDHBHvBFnMBrqXVq0LYdG_BI6u4.pXGP1oY-1676020349-0-AaKFxm3d5lM0MxgGaDXSIDK/M2zcMLdMeZRbwVBgUyZa/a8RielKHoh9JhfzxYY4fgmFWa3qOIFhWWFBVBKaiiM+A/cETb9Al1t3w72P8P1k; _ga=GA1.2.1214912980.1671620881; _gid=GA1.2.270258942.1676020356; cto_bundle=GXz2rV9uTGd3JTJGaDhtJTJCREIyVktjam0lMkZsNVlTOVlZdWEzSjZINWFjd09RdzhPdVNJYnhSR2dtUVJpU2s4WW40c3hGZzFzJTJCUlhjRmVmJTJCcU5sbmJncU1CTHVVUkxPU1k1QkFMQW1TQWVnbXNMa0YzSnlGV0UxTU82bWtNbmdIbmNIOFlaMEpPN1NvYlBMdnJJQWdDMGlkZUFjdVdnJTNEJTNE; _ga_75BBYNYN9J=GS1.1.1676020346.3.1.1676020478.0.0.0"
    cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
    proxy = '127.0.0.1:7890/'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }
    res0=requests.get(url,headers=headers,cookies=cookies,proxies=proxies)
    json=res0.json()
    res1=requests.get(url1,headers=headers,cookies=cookies,proxies=proxies)
    json1=res1.json()
    s=re.findall(re1,str(json['body']['illusts']))
    i=0
    while i<len(s):
        ID = s[i]
        title=json1["body"]["illusts"][ID]["title"]
        URL = "https://www.pixiv.net/ajax/illust/" + ID + "/pages?lang=zh"
        res2 = requests.get(URL, headers=headers, cookies=cookies, proxies=proxies)
        download.download_(res2, headers, cookies, proxies, name,title)
        i+=1


