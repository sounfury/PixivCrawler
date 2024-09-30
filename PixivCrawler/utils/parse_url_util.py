# -Time :2024/8/12 下午10:45
# -*- codeing =utf-8 -*-
from PixivCrawler.items import PixivcrawlerItem
from PixivCrawler.utils.file_path_util import sanitize_filename, parse_time


# 注意，只处理 url = f"https://www.pixiv.net/ajax/illust/{illust_id}/pages?lang=zh" 的请求
def get_img_urls(ImgJson):
    # 只下载横向图片，转换成数字再比较

    page_count = int(ImgJson["body"]["pageCount"])
    if page_count >4:
        return []
    item_url = [ImgJson["body"]["urls"]["original"]]
    # 格式"https://i.pximg.net/img-original/img/2018/12/06/00/16/31/71982822_p0.png"
    for i in range(1, page_count):
        item_url.append(ImgJson["body"]["urls"]["original"].replace("p0", f"p{i}"))

    return item_url
