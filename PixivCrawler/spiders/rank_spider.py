import scrapy

from PixivCrawler.spiders import PixivSpider
from PixivCrawler.utils.file_path_util import parse_time


class PixivRankSpider(PixivSpider):
    name = 'pixiv_rank'

    def __init__(self, num_pages, time_span, time_, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_pages = int(num_pages)
        self.time_span = int(time_span)
        self.time_ = time_
        self.current_page = 1
        self.TIME_LIST = ['日榜', '周榜', '月榜']

    def start_requests(self):
        while self.current_page <= self.num_pages:
            if self.time_span == 1:  # 日榜
                url = f"https://www.pixiv.net/ranking.php?mode=daily&date={self.time_}&p={self.current_page}&format=json"
            elif self.time_span == 2:  # 周榜
                url = f"https://www.pixiv.net/ranking.php?mode=weekly&date={self.time_}&p={self.current_page}&format=json"
            elif self.time_span == 3:  # 月榜
                url = f"https://www.pixiv.net/ranking.php?mode=monthly&date={self.time_}&p={self.current_page}&format=json"
            else:
                url = f"https://www.pixiv.net/ranking.php?mode=daily&date={self.time_}&p={self.current_page}&format=json"
            self.current_page += 1
            yield scrapy.Request(url, callback=self.parse_rank)

    def parse_rank(self, response):
        json_data = response.json()
        for content in json_data['contents']:
            illust_id = str(content['illust_id'])
            width = content['width']
            height = content['height']
            self.image_list.add_image(illust_id, width, height)

        self.image_list.image_path = parse_time(self.time_) + self.TIME_LIST[self.time_span - 1]

        yield from self.process_illust_ids()

