import numpy as np
from PIL import Image, ImageOps
from paddleocr import PaddleOCR
import mss


import logging

from 数据 import *

# 设置ppocr的日志级别为WARNING，这将关闭DEBUG信息
logging.getLogger('ppocr').setLevel(logging.WARNING)

class 识字初始化:

    def __init__(self):
        pass
    def 识字(self, region):

        with mss.mss() as sct:
            # 捕获指定区域的屏幕
            sct_img = sct.grab(region)
            # 将捕获的数据转换为PIL.Image对象
            self.img = Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb)
        ocr = PaddleOCR()
        cropped_image = self.img
        # cropped_image = self.img.crop(region)
        # 计算新的尺寸，假设我们想要放大到原来的两倍
        h, w = cropped_image.height, cropped_image.width
        border = [0, 0]
        transform_size = 320  # 图片增加边框到320大小
        if w < transform_size or h < transform_size:
            if h < transform_size:
                border[0] = (transform_size - h) / 2.0
            if w < transform_size:
                border[1] = (transform_size - w) / 2.0
            # top，buttom，left，right 对应边界的像素数目（分别为图像上面， 下面， 左面，右面填充边界的长度）

            cropped_image = ImageOps.expand(cropped_image, border= (int(border[0]), int(border[0]), int(border[1]), int(border[1])),
                                     fill=(215, 215, 215))
        try:
            result = ocr.ocr(np.array(cropped_image) , cls=False)
            for line in result:
                for i in line:
                    return i[-1][0]
        except Exception as e:
            return ""

    def in城镇(self):
        字符 = self.识字(人物)
        if 字符=="人物":
            return True
        else:
            return False

    def in赛利亚房间(self):
        字符 = self.识字(赛丽亚)
        if 字符 == "赛丽亚":
            return True
        else:
            return False
    def is公告界面(self):
        字符 = self.识字(公告_关闭)
        if 字符 == "关闭":
            return True
        else:
            return False

    def 获取所选地图名称(self):
        字符 = self.识字(所选地图名字)
        if 字符 != "":
            return 字符
        else:
            return ""
if __name__ == '__main__':
    识字 = 识字初始化()
    print(识字.in城镇())
