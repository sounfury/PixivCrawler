# -Time :2024/8/15 上午12:10
# -*- codeing =utf-8 -*-
import scrapy
import re
import json
import concurrent.futures

from PixivCrawler.spiders import PixivSpider
from PixivCrawler.utils.file_path_util import sanitize_filename


class SearchSpider(PixivSpider):
    name = 'search'
    re1 = re.compile('"width":.*?,"height":.*?,"pageCount":.*?,"bookmarkCount":(\d*),"likeCount":.*?')

    def start_requests(self):
        self.image_list.is_able_filter = False
        ratio_group = {"horizontal": 0.5, "vertical": -0.5, "square": 0, "all": None}

        search_query = input("输入要搜索的对象：")
        search_pages = int(input("请输入要搜索的页数："))

        url_template = "https://www.pixiv.net/ajax/search/artworks/{name}?word={name}&order=date_d&mode=all&p={num}&s_mode=s_tag&type=all"
        url_template += '&ratio=' + str(ratio_group[self.image_list.orientation])

        self.image_list.image_path = search_query

        for page_num in range(1, search_pages + 1):
            search_url = url_template.format(name=search_query, num=page_num)
            yield scrapy.Request(url=search_url, callback=self.parse_search_results)

    def parse_search_results(self, response):
        data = json.loads(response.text)
        for artwork in data["body"]["illustManga"]["data"]:
            self.image_list.ids.append(artwork["id"])

        yield from self.process_illust_ids()
