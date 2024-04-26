import win32con
import win32gui

from 键鼠类 import *


def move_window(title, class_name):
    # 获取窗口句柄
    hwnd = win32gui.FindWindow(class_name, title)
    if hwnd:
        # 移动窗口
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0,
                              win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
        return True
    else:
        return False


def 启动游戏():
    pass


def 进图():
    key_press_release('down', 3)
    key_press_release('1')


def 进入赛利亚房间():
    key_press_release('esc')
    time.sleep(0.01)
    mouse_move(374, 490)  # 移动鼠标到(500, 500)
    mouse_click()  # 单击鼠标左键
    time.sleep(0.5)
    key_press_release(' ')  # 模拟空格键单击


# 调用函数
if __name__ == '__main__':
    time.sleep(3)
    key_press_release(' ')
