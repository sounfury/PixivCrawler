# -Time :2024/9/30 下午11:40
# -*- codeing =utf-8 -*-
from PixivCrawler.models import ImageListBuilder
from PixivCrawler.spiders import PixivSpider


class WorkSpider(PixivSpider):
    name = 'work'

    def start_requests(self):
        work_id = input("请输入作品id: ")
        builder = ImageListBuilder()

        self.image_list = (
            builder
            .add_image(work_id)  # 添加图片
            .set_meta(work_id, "is_max", True)  # 设置元数据
            .build()  # 构建 ImageList 对象
        )

        yield from self.process_illust_ids()
