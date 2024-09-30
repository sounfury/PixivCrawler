# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from urllib.parse import urlparse
import browser_cookie3


class PixivcrawlerPipeline:
    def process_item(self, item, spider):
        return item


class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        # 如果只有一个图片，直接返回图片名
        image_guid = os.path.basename(urlparse(request.url).path)
        if len(item['image_urls']) == 1:
            image_guid = image_guid.split('.')[-1]
            return item['image_path'] + '/' + item['alt'] + '.' + image_guid

        image_guid = image_guid.split('_')[-1]
        filename = f"{item['image_path']}/{item['alt']}/{image_guid}"
        return filename

    def item_completed(self, results, item, info):
        item['images'] = [x['path'] for ok, x in results if ok]
        if item['images']:
            print(f"已下载: {item['alt']}")
        return item
