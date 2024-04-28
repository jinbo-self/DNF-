
import time
import pydirectinput


def mouse_move(x, y):
    """
    移动鼠标到指定的(x, y)坐标位置。
    """
    pydirectinput.moveTo(x, y)


def mouse_click():
    """
    模拟鼠标点击
    """
    pydirectinput.mouseDown()
    time.sleep(0.1)
    pydirectinput.mouseUp()
def mouse_mov_click(x,y):
    mouse_move(int(x), int(y))  # 移动鼠标到(x, y)
    mouse_click()  # 单击鼠标左键

def key_press_release(key_name, delay=0.01):
    """
    模拟按键的长按功能，持续按下指定的键'key_code'，持续时间为'delay'秒。
    """
    # 开始时间
    start_time = time.time()

    # 按下按键
    while (time.time() - start_time) < delay:
        pydirectinput.keyDown(key_name)
        time.sleep(0.01)  # 微小延时

    # 释放按键
    pydirectinput.keyUp(key_name)

# 使用示例
if __name__ == "__main__":
    time.sleep(2)  # 延时2秒，给你时间准备切换到一个可以接收输入的地方
    mouse_click()
