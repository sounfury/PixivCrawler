# 这里定义你的 Spider 中间件
#
# 参考文档：
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import browser_cookie3
# 用于使用单一接口处理不同的 item 类型
from itemadapter import is_item, ItemAdapter


class PixivcrawlerSpiderMiddleware:
    # 并非所有方法都需要定义。如果某个方法未定义，
    # Scrapy 会认为 Spider 中间件没有修改传递的对象。

    @classmethod
    def from_crawler(cls, crawler):
        # Scrapy 用这个方法来创建你的 Spiders。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # 每个经过 Spider 中间件并传递给 Spider 的 response 都会调用该方法。

        # 应返回 None 或抛出异常。
        return None

    def process_spider_output(self, response, result, spider):
        # 当 Spider 处理完 response 后，
        # 会调用该方法返回结果。

        # 必须返回一个 Request 或 item 对象的迭代器。
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # 当 Spider 或 process_spider_input() 方法
        # （来自其他 Spider 中间件）抛出异常时调用。

        # 应返回 None 或者一个 Request 或 item 对象的迭代器。
        pass

    def process_start_requests(self, start_requests, spider):
        # 该方法会在 spider 的 start requests 调用时被调用，
        # 类似于 process_spider_output() 方法，但没有与之关联的 response。

        # 必须只返回 requests（而不是 items）。
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider 已开启: %s" % spider.name)


class PixivcrawlerDownloaderMiddleware:
    # 并非所有方法都需要定义。如果某个方法未定义，
    # Scrapy 会认为下载中间件没有修改传递的对象。

    @classmethod
    def from_crawler(cls, crawler):
        # Scrapy 用这个方法来创建你的 Spiders。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # 每次 request 经过下载中间件时都会调用该方法。
        pixivCookie = browser_cookie3.edge(domain_name='pixiv.net')

        # print(pixivCookie)
        # 将 cookie 添加到 request 中
        request.cookies = {cookie.name: cookie.value for cookie in pixivCookie}
        # 设置代理
        proxy = '127.0.0.1:7890/'
        request.meta['proxy'] = 'http://' + proxy
        # 必须返回以下之一：
        # - 返回 None: 继续处理此 request
        # - 返回一个 Response 对象
        # - 返回一个 Request 对象
        # - 或抛出 IgnoreRequest: 安装的 downloader 中间件的 process_exception() 方法将会被调用
        return None

    def process_response(self, request, response, spider):
        # 该方法会在 downloader 返回 response 时被调用。

        # 必须返回以下之一：
        # - 返回一个 Response 对象
        # - 返回一个 Request 对象
        # - 或抛出 IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # 当下载处理器或 process_request()
        # （来自其他下载中间件）抛出异常时调用。

        # 必须返回以下之一：
        # - 返回 None: 继续处理此异常
        # - 返回一个 Response 对象: 停止 process_exception() 链
        # - 返回一个 Request 对象: 停止 process_exception() 链
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider 已开启: %s" % spider.name)
