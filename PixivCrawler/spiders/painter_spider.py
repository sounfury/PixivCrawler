import re

import scrapy

from PixivCrawler.spiders import PixivSpider


# 子爬虫把id列表传递给父爬虫，父爬虫再根据id列表获取图片信息


class PainterSpider(PixivSpider):
    name = 'painter'

    def __init__(self, painter_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.painter_id = painter_id
        self.painter_name = None
        self.max_ids_per_batch = 70  # 将批次最大数量定义为常量，方便调整
        self.base_url = f"https://www.pixiv.net/ajax/user/{self.painter_id}/profile/illusts"

    def start_requests(self):
        url = f"https://www.pixiv.net/ajax/user/{self.painter_id}/profile/all"
        yield scrapy.Request(url, callback=self.parse_illust_ids)

    def parse_illust_ids(self, response):
        try:
            json_data = response.json()
            self.image_list.image_path = self.painter_name

            # 提取作品 ID 列表
            illust_ids = list(json_data['body']['illusts'].keys())
            print(f"ids_list: {illust_ids}")

            # 生成图片详情请求
            for batch_ids in self.split_illust_ids(illust_ids, self.max_ids_per_batch):
                detail_url = self.generate_illust_url(batch_ids)
                if len(detail_url) <= 2083:
                    yield scrapy.Request(detail_url, callback=self.parse_illust_detail)
                else:
                    print(f"Warning: URL exceeds 2083 characters, further splitting required.")
                    # 这里可以进一步细化逻辑，比如将批次再拆分，处理长 URL

        except KeyError as e:
            print(f"KeyError: {str(e)} - Data format may have changed.")
        except Exception as e:
            print(f"Error in parse_illust_ids: {str(e)}")

    def parse_illust_detail(self, response):
        try:
            json_data = response.json()
            works = json_data["body"]["works"]

            for image_id, details in works.items():
                width = details.get("width")
                height = details.get("height")

                if width and height:
                    # 使用 add_image 方法将图片信息存储到 ImageList
                    self.image_list.add_image(image_id, width, height)

                # 处理每个图片 ID 的其他请求
                yield from self.process_illust_ids()

        except KeyError as e:
            print(f"KeyError: {str(e)} - Possibly missing data.")
        except Exception as e:
            print(f"Error in parse_illust_detail: {str(e)}")

    def split_illust_ids(self, illust_ids, max_batch_size):
        """将 illust_ids 列表按批次拆分，返回生成器"""
        for i in range(0, len(illust_ids), max_batch_size):
            yield illust_ids[i:i + max_batch_size]

    def generate_illust_url(self, illust_ids):
        """生成作品详情请求的 URL"""
        ids_param = "&".join([f"ids%5B%5D={id}" for id in illust_ids])
        detail_url = f"{self.base_url}?{ids_param}&work_category=illustManga&is_first_page=1&sensitiveFilterMode=userSetting&lang=zh"
        return detail_url
