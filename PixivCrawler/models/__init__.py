class ImageList:
    def __init__(self):
        self.images = {}  # 用字典存储id:(width, height)
        self.image_path = None
        self.ids = []
        self.is_able_filter = True
        self.orientation = 'all'

    def add_image(self, image_id, width, height):
        # 添加id和图片的宽度、高度
        self.images[image_id] = (width, height)

    def __repr__(self):
        # 返回当前存储的所有图像信息
        return f"ImageList(images={self.images})"

    def filter_by_direction(self):
        if not self.ids:
            self.ids = self.images.keys()

        if self.orientation == "all":
            self.is_able_filter = False

        if not self.is_able_filter:
            return self.ids
        # 根据给定的方向筛选是该方向的图片id
        filtered_ids = []
        for image_id in self.ids:
            if self.orientation == "horizontal" and self.is_horizontal(image_id):
                filtered_ids.append(image_id)
            elif self.orientation == "vertical" and self.is_vertical(image_id):
                filtered_ids.append(image_id)
            elif self.orientation == "square" and self.is_square(image_id):
                filtered_ids.append(image_id)
        return filtered_ids

    def is_square(self, image_id):
        # 判断某个id的图片是否为正方形
        if image_id in self.images:
            return self.images[image_id][0] == self.images[image_id][1]
        return False

    def is_horizontal(self, image_id):
        # 判断某个id的图片是否为横向图片
        if image_id in self.images:
            return self.images[image_id][0] > self.images[image_id][1]
        return False

    def is_vertical(self, image_id):
        # 判断某个id的图片是否为纵向图片
        if image_id in self.images:
            return self.images[image_id][0] < self.images[image_id][1]
        return False
