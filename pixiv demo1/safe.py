# -Time :2023/2/14 13:45
# -*- codeing =utf-8 -*-
# 增加重试连接次数
import requests
import urllib3
def safe_():
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.Session()
    # 关闭多余连接
    s.keep_alive = False
    # 取消验证证书
    s.verify = False
    urllib3.disable_warnings()