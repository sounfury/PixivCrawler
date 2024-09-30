# -Time :2024/8/11 下午11:44
# -*- codeing =utf-8 -*-
import re


def sanitize_filename(title):  # 用于处理文件名中的特殊字符
    return re.sub(r'[\\/:*?"<>|]', '-', title)


def parse_time(time_):
    year = time_[:4]
    month = int(time_[4:6])
    if month < 10:
        month = int(time_[5])
    day = int(time_[6:])
    return str(year)+"年"+str(month)+"月"+str(day)+"日"
# 测试


