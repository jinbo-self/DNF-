import numpy as np
import win32gui
import win32ui
import win32con
import win32api
from PIL import Image, ImageOps
from paddleocr import PaddleOCR

import logging

# 设置ppocr的日志级别为WARNING，这将关闭DEBUG信息
logging.getLogger('ppocr').setLevel(logging.WARNING)

class 识字初始化:
    人物 = (636, 31, 662, 45)
    赛丽亚 = (424,178,466,198)
    def __init__(self):
        hdesktop = win32gui.GetDesktopWindow()
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

        desktop_dc = win32gui.GetWindowDC(hdesktop)
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)
        mem_dc = img_dc.CreateCompatibleDC()

        screenshot = win32ui.CreateBitmap()
        screenshot.CreateCompatibleBitmap(img_dc, width, height)
        mem_dc.SelectObject(screenshot)
        mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

        signedIntsArray = screenshot.GetBitmapBits(True)
        self.img = Image.frombuffer('RGB', (width, height), signedIntsArray, 'raw', 'BGRX', 0, 1)

        mem_dc.DeleteDC()
        win32gui.ReleaseDC(hdesktop, desktop_dc)
        win32gui.DeleteObject(screenshot.GetHandle())


    def 识字(self, region):
        ocr = PaddleOCR()
        cropped_image = self.img.crop(region)
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
        字符 = self.识字(self.人物)
        if 字符=="人物":
            return True
        else:
            return False

    def in赛利亚房间(self):
        字符 = self.识字(self.赛丽亚)
        if 字符 == "赛丽亚":
            return True
        else:
            return False


if __name__ == '__main__':
    识字 = 识字初始化()
    print(识字.in赛利亚房间())
