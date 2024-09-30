# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PixivcrawlerItem(scrapy.Item):
    # alt是图片的标题
    alt = scrapy.Field()

    image_urls = scrapy.Field()

    images = scrapy.Field()

    #图片保存路径
    image_path = scrapy.Field()
    pass


class PixivItemBuilder:
    def __init__(self):
        self._item = PixivcrawlerItem()

    def set_alt(self, alt):
        """设置图片标题"""
        self._item['alt'] = alt
        return self

    def set_image_urls(self, image_urls):
        """设置图片链接"""
        self._item['image_urls'] = image_urls
        return self

    def set_images(self, images):
        """设置图片"""
        self._item['images'] = images
        return self

    def set_image_path(self, image_path):
        """设置图片保存路径"""
        self._item['image_path'] = image_path
        return self

    def build(self):
        """返回构建完成的Item"""
        return self._item
