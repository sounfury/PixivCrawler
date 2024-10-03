# -Time :2024/8/14 下午11:24
# -*- codeing =utf-8 -*-
import string

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from PixivCrawler import PainterSpider, PixivRankSpider
from PixivCrawler.spiders.search_spider import SearchSpider
from PixivCrawler.spiders.work_spider import WorkSpider


class CrawlerFactory:
    def __init__(self):
        self.pixiv_spider = None
        self.spider_args = {}

    def create_spider(self, type: str):
        if type == 'painter':
            painter_id = input("请输入画师id: ")
            self.pixiv_spider = PainterSpider
            self.spider_args = {'painter_id': painter_id}
        elif type == 'rank':
            num_pages = int(input("请输入要查询的页数: "))
            time_span = int(input("请选择时间跨度：1. 日，2. 周，3. 月: "))
            time_ = input("请输入要查询的时间，以20230227格式: ")
            self.pixiv_spider = PixivRankSpider
            self.spider_args = {'num_pages': num_pages, 'time_span': time_span, 'time_': time_}
        elif type == 'search':
            self.pixiv_spider = SearchSpider
        elif type == 'work':
            self.pixiv_spider = WorkSpider
        else:
            print("功能未开放")
            return None

    def process_spider(self):
        if not self.pixiv_spider:
            print("请先创建爬虫实例。")
            return

        process = CrawlerProcess(get_project_settings())
        process.crawl(self.pixiv_spider, **self.spider_args)  # 传递spider类和参数
        process.start()
