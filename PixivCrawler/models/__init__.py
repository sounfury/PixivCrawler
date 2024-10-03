class ImageList:
    def __init__(self):
        self.images = {}  # 用字典存储id:(width, height,meta)
        self.image_path = None
        self.ids = []
        self.is_able_filter = True
        self.orientation = 'all'

    def add_image(self, image_id, width=None, height=None):
        # 添加id和图片的宽度、高度
        self.images[image_id] = {
            "width": width,
            "height": height,
            "meta": {
                "is_max": False
            }
        }

    def set_meta(self, image_id, key, value):
        # 设置图片的元数据
        if image_id in self.images:
            self.images[image_id]["meta"][key] = value

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


class ImageListBuilder:
    def __init__(self):
        # 初始化存储图片信息
        self.image_list = ImageList()

    def set_image_path(self, image_path):
        # 设置图片路径
        self.image_list.image_path = image_path
        return self

    def set_is_able_filter(self, is_able_filter):
        # 设置是否需要筛选图片
        self.image_list.is_able_filter = is_able_filter
        return self

    def add_image(self, image_id, width=None, height=None):
        # 添加图片信息
        self.image_list.add_image(image_id, width, height)
        return self

    def set_orientation(self, orientation):
        # 设置图片的方向（横向、纵向或正方形）
        self.image_list.orientation = orientation
        return self

    def set_meta(self, image_id, key, value):
        # 设置图片的元数据信息
        self.image_list.set_meta(image_id, key, value)
        return self

    def build(self):
        # 构建完成后返回 ImageList 对象
        return self.image_list
