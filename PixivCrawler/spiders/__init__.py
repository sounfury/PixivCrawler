# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from abc import ABC, abstractmethod
from PixivCrawler.items import PixivcrawlerItem, PixivItemBuilder
from PixivCrawler.utils import parse_url_util
from PixivCrawler.utils.file_path_util import sanitize_filename
from PixivCrawler.models import ImageList


class PixivSpider(scrapy.Spider, ABC):
    allowed_domains = ['pixiv.net', 'i.pximg.net']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image_list = ImageList()

        type_orientation: str = input("选择图片方向：1.横向 2.纵向 3.全部")
        if type_orientation == '1':
            self.image_list.orientation = 'horizontal'
        elif type_orientation == '2':
            self.image_list.orientation = 'vertical'
        else:
            pass

    def process_illust_ids(self):

        illust_ids = self.image_list.filter_by_direction()
        for illust_id in illust_ids:
            title_url = f"https://www.pixiv.net/ajax/illust/{illust_id}"
            yield scrapy.Request(title_url, callback=self.parse_image)

    def parse_image(self, response):
        json_data = response.json()
        title = json_data['body']['title']

        item = PixivItemBuilder() \
            .set_alt(sanitize_filename(title)) \
            .set_image_urls(parse_url_util.get_img_urls(json_data)) \
            .set_image_path(self.image_list.image_path or json_data['body']['userName']) \
            .build()

        print("初始化完成,开始下载图片")

        if item['image_urls']:
            yield item
