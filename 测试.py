import cv2
import mss
import numpy as np
from ultralytics import YOLO
import logging

# 设置ppocr的日志级别为WARNING，这将关闭DEBUG信息

if __name__ == '__main__':
    # model = YOLO("last.pt")  # 加载预训练模型（建议用于训练）
    logging.basicConfig(level=logging.ERROR)  # 只显示错误信息
    model = YOLO("best.pt")
    with mss.mss() as sct:
        # 捕获指定区域的屏幕

        while True:
            sct_img = sct.grab((0, 0, 800, 600))
            img = np.array(sct_img)[:, :, :3]
            img = img.astype(np.uint8)
            results = model(img)  # 对图像进行预测
            #
            for r in results:
                boxes = r.boxes  # Boxes object for bbox outputs
                for box in boxes:
                    loc = np.array(box.xyxy.cpu())[0]
                    if loc is not None:
                        x1, y1, x2, y2 = map(int, [loc[0], loc[1], loc[2], loc[3]])
                        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.imshow('dnf', img)
            if cv2.waitKey(1) == ord('q'):  # 按 'q' 键退出
                break

        cv2.destroyAllWindows()