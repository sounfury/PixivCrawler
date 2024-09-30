from PixivCrawler.spiders import rank_spider
from PixivCrawler.spiders.painter_spider import PainterSpider
from PixivCrawler.spiders.rank_spider import PixivRankSpider

from PixivCrawler.factory.crawler_factory import CrawlerFactory


def main():
    factory = CrawlerFactory()
    while True:
        print("请选择：")
        print("1.搜索画师")
        print("2.排行榜")
        print("3.搜索tag")
        a = input("请输入你的选择（数字1-3）：")
        if a == "1":
            factory.create_spider('painter')
        elif a == "2":
            factory.create_spider('rank')
        elif a == "3":
            factory.create_spider('search')

        factory.process_spider()


if __name__ == '__main__':
    main()
