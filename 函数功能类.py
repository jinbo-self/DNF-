import math
import random

import win32con
import win32gui

from 识字类 import *
from 键鼠类 import *
import heapq


class Node:

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0  # Cost from start to node
        self.h = 0  # Heuristic from node to end
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Manhattan distance


def A星寻路(maze, start, end):
    """A*寻路"""
    start_node = Node(None, tuple(start))
    end_node = Node(None, tuple(end))
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, (start_node.f, start_node))

    while open_list:
        current_node = heapq.heappop(open_list)[1]
        closed_list.add(current_node)

        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        (x, y) = current_node.position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next in neighbors:
            try:
                maze_value = maze[next[0]][next[1]]
            except IndexError:
                continue
            if maze_value == 1:
                continue
            neighbor = Node(current_node, next)

            if neighbor in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, end_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if add_to_open(open_list, neighbor):
                heapq.heappush(open_list, (neighbor.f, neighbor))


def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node[1] and neighbor.g > node[1].g:
            return False
    return True


# Define the maze


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


def 从城镇进图():
    key_press_release('down', 1.5)
    key_press_release('1')
    time.sleep(3)
    mouse_mov_click(比拉谢尔面板[0], 比拉谢尔面板[1])
    time.sleep(0.5)
    mouse_mov_click(比拉谢尔面板_毁坏的克洛诺斯岛[0], 比拉谢尔面板_毁坏的克洛诺斯岛[1])
    key_press_release('space')
    time.sleep(0.5)
    key_press_release('right', 3)


def 进入赛利亚房间():
    key_press_release('esc')
    time.sleep(0.01)
    mouse_mov_click(设置_选择角色[0], 设置_选择角色[1])
    time.sleep(0.5)
    key_press_release('space')  # 模拟空格键单击


def 关闭公告():
    mouse_mov_click((公告_关闭[0] + 公告_关闭[2]) / 2, (公告_关闭[1] + 公告_关闭[3]) / 2)


def 选图(识字):
    while 识字.获取所选地图名称() != 地图名:
        key_press_release('down')
    key_press_release('space')


def 打怪(识字):
    #
    怪物坐标 = 获取怪物坐标(识字)
    while 怪物坐标 != (0, 0):
        # print("跑到目标", 怪物坐标)
        人物坐标 = 获取人物坐标(识字)
        技能列表 = 获取技能可用列表(识字)
        while not is距离近(人物坐标, 怪物坐标, 120, 40) and 怪物坐标 != (0, 0):
            技能列表 = 获取技能可用列表(识字)
            人物坐标 = 获取人物坐标(识字)
            怪物坐标 = 获取怪物坐标(识字)
            # print("人物坐标", 人物坐标, "怪物坐标", 怪物坐标)
            跑到目标(怪物坐标, 识字)
            if 怪物坐标 == (0, 0):
                break
            释放技能(技能列表)
            if 人物坐标 == (999, 999):  #被遮挡
                释放技能(技能列表)
        # print("获取技d能列表")

        # print("释放技能:", 技能列表)
        释放技能(技能列表)
        怪物坐标 = 获取怪物坐标(识字)
        # print("获取怪物坐标：", 怪物坐标)
    按键.release_all_keys()


def 捡物(识字):
    物品坐标 = 获取物品坐标(识字)
    while 物品坐标 != (0, 0):
        # print("跑到目标", 怪物坐标)
        人物坐标 = 获取人物坐标(识字)
        while not is距离近(人物坐标, 物品坐标, 40, 40) and 物品坐标 != (0, 0):
            if is距离近(人物坐标, 物品坐标, 120, 120):
                走到目标(物品坐标, 识字)
                key_press_release('x')
            人物坐标 = 获取人物坐标(识字)
            物品坐标 = 获取物品坐标(识字)
            # print("人物坐标", 人物坐标, "怪物坐标", 怪物坐标)
            跑到目标(物品坐标, 识字)

            if 人物坐标 == (999, 999):  # 被遮挡往中间跑
                跑到目标((428, 379), 识字)
        # print("获取技d能列表")
        key_press_release('x')
        # print("释放技能:", 技能列表)
        物品坐标 = 获取物品坐标(识字)
        # print("获取怪物坐标：", 怪物坐标)
    按键.release_all_keys()


def 过图(识字):
    """直接写死得了"""
    当前房间 = 取当前房间(识字)
    上个房间 = 当前房间
    print(当前房间, 上个房间, 获取怪物坐标(识字))
    路径算法 = A星寻路(小地图路径.地图数据, 当前房间, 小地图路径.终点)
    当前路径 = 路径算法.index(当前房间)
    # 小地图的xy与像素点坐标的xy居然是相反的。。。。。
    if 当前路径 != len(路径算法) + 1:
        下个房间走法 = 路径算法[当前路径 + 1]
        index = 1
        while 当前房间 == 上个房间 or 获取怪物坐标(识字) == (0, 0):
            # 0,0  0,1  0,2
            # 1,0  1,1  1,2
            # 2,0  2,1  2,2
            print(当前房间, 上个房间)
            所有门坐标 = 获取门坐标(识字)
            当前房间 = 取当前房间(识字)
            人物坐标 = 获取人物坐标(识字)
            if isBoss房间(识字):
                break
            if 人物坐标 == (999, 999):
                跑到目标((392, 272), 识字)
                if 当前房间 != 上个房间 or 获取怪物坐标(识字) != (0, 0):
                    break
            if 当前房间 == (999, 999):
                continue
            # direction = (下个房间走法[0] - 当前房间[0], 下个房间走法[1] - 当前房间[1])

            if not 所有门坐标:
                key_press_release('right')
                按键.key_press('right')
                time.sleep(1)
                按键.release_all_keys()
                if 当前房间 != 上个房间 or 获取怪物坐标(识字) != (0, 0):
                    break
            if index == 1:
                index = index + 1
                key_press_release('right')
                按键.key_press('right')
                time.sleep(1)
                if 当前房间 != 上个房间 or 获取怪物坐标(识字) != (0, 0):
                    break
            所有门坐标 = 获取门坐标(识字)
            if 当前房间 == (4, 1) and 所有门坐标 != []:
                跑到目标(所有门坐标[0], 识字)
                if 当前房间 != 上个房间 or 获取怪物坐标(识字) != (0, 0):
                    break
            elif 所有门坐标:  # 右边或者上边都行
                w = 0
                best_door = None
                if len(所有门坐标) == 1:  # 一个门的话只可能是右边或者上边
                    跑到目标(所有门坐标[0], 识字)
                    if 当前房间 != 上个房间 or 获取怪物坐标(识字) != (0, 0):
                        break
                else:
                    # 往上边走
                    for 门坐标 in 所有门坐标:
                        if 门坐标[0] > w:
                            w = 门坐标[0]
                            best_door = 门坐标
                    跑到目标(best_door, 识字)
                    if 当前房间 != 上个房间 or 获取怪物坐标(识字) != (0, 0):
                        break

            # for 门坐标 in 所有门坐标:
            #     print(门坐标, 人物坐标, 下个房间走法, 当前房间)
            #     if direction == (0, 1) and 门坐标[0]+门坐标偏移 > 人物坐标[0]:  #右边
            #         distance = abs(门坐标[0] - 人物坐标[0])
            #         if distance > max_distance:
            #             max_distance = distance
            #             best_door = 门坐标
            #     elif direction == (0, -1) and 门坐标[0]-门坐标偏移 < 人物坐标[0]:  #左边
            #         distance = abs(门坐标[0] - 人物坐标[0])
            #         if distance > max_distance:
            #             max_distance = distance
            #             best_door = 门坐标
            #     elif direction == (1, 0) and 门坐标[1]+门坐标偏移 >人物坐标[1]:  #下边
            #         distance = abs(门坐标[0] - 人物坐标[0])
            #         if distance > max_distance:
            #             max_distance = distance
            #             best_door = 门坐标
            #     elif direction == (-1, 0) and 门坐标[1]-门坐标偏移 < 人物坐标[1]:  #上边
            #         distance = abs(门坐标[0] - 人物坐标[0])
            #         if distance > max_distance:
            #             max_distance = distance
            #             best_door = 门坐标
            # best_door = 所有门坐标[0]
            # print(best_door)
            # if best_door is None:
            #     按键.release_all_keys()
            #     按键.key_press('up')
            #     按键.key_press('right')
            #     # if direction == (0, 1):  # 右边
            #     #     按键.key_press('right')
            #     # elif direction == (0, -1):  # 左边
            #     #     按键.key_press('left')
            #     # elif direction == (1, 0):  # 下边
            #     #     按键.key_press('down')
            #     # elif direction == (-1, 0):  # 上边
            #     #     按键.key_press('up')
            # else:
            #     跑到目标(best_door)
            # 当前房间 = 取当前房间()

    按键.release_all_keys()


def 跑到目标(目的坐标, 识字, 横轴偏差=0, 纵轴偏差=0):
    当前时间 = 0
    上次坐标时间 = 0
    上次坐标 = (0, 0)
    实时坐标 = (0, 0)
    上次房间时间 = 0
    上次房间坐标 = (0, 0)
    实时房间坐标 = (0, 0)
    实时坐标 = 获取人物坐标(识字)
    print("本人坐标：", 实时坐标)
    print("目的坐标：", 目的坐标)
    上次房间坐标 = 取当前房间(识字)
    if 实时坐标 == (999, 999):
        按键.release_all_keys()
        按键.key_press('up')
        key_press_release('right')
        按键.key_press('right')
        return
    if 上次房间坐标 == (999, 999):
        return
    if is距离近(实时坐标, 目的坐标, 120, 40):
        print("走动模式")
        走到目标(目的坐标, 识字, 横轴偏差, 纵轴偏差)
        return
        # 向右走
    if 目的坐标[0] > 实时坐标[0] and 目的坐标[1] == 实时坐标[1]:
        print("向右走")
        按键.release_all_keys()
        key_press_release('right')
        按键.key_press('right')
        # 按键.key_release('up')
        # 按键.key_release('down')
        # 按键.key_release('left')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差:
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    # 向左走
    if 目的坐标[0] < 实时坐标[0] and 目的坐标[1] == 实时坐标[1]:
        print("向左走")
        按键.release_all_keys()
        key_press_release('left')
        按键.key_press('left')
        # 按键.key_release('up')
        # 按键.key_release('down')
        # 按键.key_release('right')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差:
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    # 向下走
    if 目的坐标[1] > 实时坐标[1] and 目的坐标[0] == 实时坐标[0]:
        print("向下走")
        按键.release_all_keys()
        按键.key_press('down')
        # 按键.key_release('up')
        # 按键.key_release('right')
        # 按键.key_release('left')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:  # 判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    # 向上走
    if 目的坐标[1] < 实时坐标[1] and 目的坐标[0] == 实时坐标[0]:
        print("向上走")
        按键.release_all_keys()
        按键.key_press('up')
        # 按键.key_release('right')
        # 按键.key_release('down')
        # 按键.key_release('left')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:  # 判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    # 向右上走
    if 目的坐标[0] > 实时坐标[0] and 目的坐标[1] < 实时坐标[1]:
        print("向右上走")
        按键.release_all_keys()
        按键.key_press('up')
        key_press_release('right')
        按键.key_press('right')
        # 按键.key_release('down')
        # 按键.key_release('left')

        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差:
        #         按键.key_release('right')
        #
        #     if 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:
        #         按键.key_release('up')
        #
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差 and 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:  # 判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.key_release('right')
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.key_release('up')
        #         if 实时坐标[0] == 上次坐标[0] and 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    # 向右下走
    if 目的坐标[0] > 实时坐标[0] and 目的坐标[1] > 实时坐标[1]:
        print("向右下走")
        按键.release_all_keys()
        按键.key_press('down')
        key_press_release('right')
        按键.key_press('right')
        # 按键.key_release('up')
        # 按键.key_release('left')

        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差:
        #         按键.key_release('right')
        #
        #     if 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:
        #         按键.key_release('down')
        #
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差 and 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:  # 判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.key_release('right')
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.key_release('down')
        #         if 实时坐标[0] == 上次坐标[0] and 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    # 向左上走
    if 目的坐标[0] < 实时坐标[0] and 目的坐标[1] < 实时坐标[1]:
        print("向左上走")
        按键.release_all_keys()
        按键.key_press('up')
        key_press_release('left')
        按键.key_press('left')
        # 按键.key_release('down')
        # 按键.key_release('right')

        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差:
        #         按键.key_release('left')
        #
        #     if 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:
        #         按键.key_release('up')
        #
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差 and 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:  # 判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.key_release('left')
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.key_release('up')
        #         if 实时坐标[0] == 上次坐标[0] and 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    # 向左下走
    if 目的坐标[0] < 实时坐标[0] and 目的坐标[1] > 实时坐标[1]:
        print("向左下走")
        按键.release_all_keys()
        按键.key_press('down')
        key_press_release('left')
        按键.key_press('left')
        # 按键.key_release('up')
        # 按键.key_release('right')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差:
        #         按键.key_release('left')
        #
        #     if 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:
        #         按键.key_release('down')
        #
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差 and 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:  # 判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.key_release('left')
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.key_release('down')
        #         if 实时坐标[0] == 上次坐标[0] and 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)


def 走到目标(目的坐标, 识字, 横轴偏差=0, 纵轴偏差=0):
    # 先声明一下
    当前时间 = 0
    上次坐标时间 = 0
    上次坐标 = (0, 0)
    实时坐标 = (0, 0)
    上次房间时间 = 0
    上次房间坐标 = (0, 0)
    实时房间坐标 = (0, 0)
    # 开始
    实时坐标 = 获取人物坐标(识字)
    上次房间坐标 = 取当前房间(识字)
    # 向右走
    if 目的坐标[0] > 实时坐标[0] and 目的坐标[1] == 实时坐标[1]:
        按键.release_all_keys()
        按键.key_press('right')
        # 按键.key_release('up')
        # 按键.key_release('down')
        # 按键.key_release('left')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差:
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  #判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  #判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    #向左走
    if 目的坐标[0] < 实时坐标[0] and 目的坐标[1] == 实时坐标[1]:
        按键.release_all_keys()
        按键.key_press('left')
        # 按键.key_release('up')
        # 按键.key_release('down')
        # 按键.key_release('right')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差:
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  #判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  #判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    #向下走
    if 目的坐标[1] > 实时坐标[1] and 目的坐标[0] == 实时坐标[0]:
        按键.release_all_keys()
        按键.key_press('down')
        按键.key_release('up')
        # 按键.key_release('right')
        # 按键.key_release('left')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:  #判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  #判断边缘
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  #判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    # 向上走
    if 目的坐标[1] < 实时坐标[1] and 目的坐标[0] == 实时坐标[0]:
        按键.release_all_keys()
        按键.key_press('up')
        按键.key_release('right')
        # 按键.key_release('down')
        # 按键.key_release('left')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:  # 判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  # 判断边缘
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  # 判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    #向右上走
    if 目的坐标[0] > 实时坐标[0] and 目的坐标[1] < 实时坐标[1]:
        按键.release_all_keys()
        按键.key_press('right')
        按键.key_press('up')
        # 按键.key_release('down')
        # 按键.key_release('left')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差:
        #         按键.key_release('right')
        #
        #     if 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:
        #         按键.key_release('up')
        #
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差 and 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:  #判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  #判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.key_release('right')
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.key_release('up')
        #         if 实时坐标[0] == 上次坐标[0] and 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  #判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    #向右下走
    if 目的坐标[0] > 实时坐标[0] and 目的坐标[1] > 实时坐标[1]:
        按键.release_all_keys()
        按键.key_press('right')
        按键.key_press('down')
        # 按键.key_release('up')
        # 按键.key_release('left')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差:
        #         按键.key_release('right')
        #
        #     if 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:
        #         按键.key_release('down')
        #
        #     if 目的坐标[0] <= 实时坐标[0] + 横轴偏差 and 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:  #判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  #判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.key_release('right')
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.key_release('down')
        #         if 实时坐标[0] == 上次坐标[0] and 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  #判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    #向左上走
    if 目的坐标[0] < 实时坐标[0] and 目的坐标[1] < 实时坐标[1]:
        按键.release_all_keys()
        按键.key_press('left')
        按键.key_press('up')
        # 按键.key_release('down')
        # 按键.key_release('right')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差:
        #         按键.key_release('left')
        #
        #     if 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:
        #         按键.key_release('up')
        #
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差 and 目的坐标[1] >= 实时坐标[1] - 纵轴偏差:  #判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  #判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.key_release('left')
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.key_release('up')
        #         if 实时坐标[0] == 上次坐标[0] and 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  #判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)
    #向左下走
    if 目的坐标[0] < 实时坐标[0] and 目的坐标[1] > 实时坐标[1]:
        按键.release_all_keys()
        按键.key_press('left')
        按键.key_press('down')
        # 按键.key_release('up')
        # 按键.key_release('right')
        # while True:
        #     当前时间 = time.time()
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差:
        #         按键.key_release('left')
        #
        #     if 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:
        #         按键.key_release('down')
        #
        #     if 目的坐标[0] >= 实时坐标[0] - 横轴偏差 and 目的坐标[1] <= 实时坐标[1] + 纵轴偏差:  #判断抵达
        #         按键.release_all_keys()
        #         return
        #     if 当前时间 - 上次坐标时间 > 500:  #判断边缘
        #         if 实时坐标[0] == 上次坐标[0]:
        #             按键.key_release('left')
        #         if 实时坐标[1] == 上次坐标[1]:
        #             按键.key_release('down')
        #         if 实时坐标[0] == 上次坐标[0] and 实时坐标[1] == 上次坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次坐标 = 实时坐标
        #         上次坐标时间 = 当前时间
        #     if 当前时间 - 上次房间时间 > 500:  #判断下个房间
        #         实时房间坐标 = 取当前房间(sct)
        #         if 实时房间坐标[0] != 上次房间坐标[0] or 实时房间坐标[1] != 上次房间坐标[1]:
        #             按键.release_all_keys()
        #             return
        #         上次房间坐标 = 实时房间坐标
        #         上次房间时间 = 当前时间
        #     实时坐标 = 获取人物坐标(model, sct)


def 获取人物坐标(识字):
    sct = 识字.get_sct()
    sct_img = sct.grab((0, 0, 800, 600))
    img = np.array(sct_img)[:, :, :3]
    img = img.astype(np.uint8)
    results = model(img)  # 对图像进行预测
    #
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        # img = r.plot(img=img)

        for box in boxes:
            if r.names[int(np.array(box.cls.cpu())[0])] == "Hero":
                loc = np.array(box.xyxy.cpu())[0]
                return (loc[2] + loc[0]) / 2, loc[3]
    return 999, 999


def 获取怪物坐标(识字):
    """Class可以为怪物，物品，门"""
    sct = 识字.get_sct()
    sct_img = sct.grab((0, 0, 800, 600))
    img = np.array(sct_img)[:, :, :3]
    img = img.astype(np.uint8)
    results = model(img)  # 对图像进行预测
    tmp = []
    loc = (0, 0)
    人物坐标 = (0, 0)
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        # img = r.plot(img=img)
        # #Boss,LittleBoss,Hero,Monster,Door,Object
        for box in boxes:
            if (r.names[int(np.array(box.cls.cpu())[0])] == "Boss"
                    or r.names[int(np.array(box.cls.cpu())[0])] == "LittleBoss"
                    or r.names[int(np.array(box.cls.cpu())[0])] == "Monster"):
                person = np.array(box.xyxy.cpu())[0]
                tmp.append(((person[2] + person[0]) / 2, person[3]))

    min_distance = float('inf')  # 初始化最小距离为无穷大

    if tmp != []:
        for (x, y) in tmp:
            distance = math.sqrt((x - 人物坐标[0]) ** 2 + (y - 人物坐标[1]) ** 2)  # 计算距离
            if distance < min_distance:
                min_distance = distance
                loc = (x, y)
    return loc


def 获取物品坐标(识字):
    """Class可以为怪物，物品，门"""
    sct = 识字.get_sct()
    sct_img = sct.grab((0, 0, 800, 600))
    img = np.array(sct_img)[:, :, :3]
    img = img.astype(np.uint8)
    results = model(img)  # 对图像进行预测
    tmp = []
    loc = (0, 0)
    人物坐标 = (0, 0)
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        # img = r.plot(img=img)
        # #Boss,LittleBoss,Hero,Monster,Door,Object
        for box in boxes:
            if r.names[int(np.array(box.cls.cpu())[0])] == "Object":
                person = np.array(box.xyxy.cpu())[0]
                tmp.append(((person[2] + person[0]) / 2, person[3]))

    min_distance = float('inf')  # 初始化最小距离为无穷大

    if tmp != []:
        for (x, y) in tmp:
            distance = math.sqrt((x - 人物坐标[0]) ** 2 + (y - 人物坐标[1]) ** 2)  # 计算距离
            if distance < min_distance:
                min_distance = distance
                loc = (x, y)
    return loc


def 获取门坐标(识字):
    sct = 识字.get_sct()
    sct_img = sct.grab((0, 0, 800, 600))
    img = np.array(sct_img)[:, :, :3]
    img = img.astype(np.uint8)
    results = model(img)  # 对图像进行预测
    tmp = []
    #
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        # img = r.plot(img=img)
        # #Boss,LittleBoss,Hero,Monster,Door,Object
        for box in boxes:
            if r.names[int(np.array(box.cls.cpu())[0])] == "Door":
                person = np.array(box.xyxy.cpu())[0]
                tmp.append(((person[2] + person[0]) / 2, person[3]))
    return tmp


def 取当前房间(识字):
    """先扫描颜色，再确定坐标，计算出房间号"""
    sct = 识字.get_sct()
    sct_img = sct.grab(小地图位置)
    img = Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb)

    # 加载图像的像素数据
    pixels = img.load()
    行数 = len(小地图路径.地图数据)
    列数 = len(小地图路径.地图数据[0])
    房间宽度 = (小地图位置[2] - 小地图位置[0]) / 列数
    房间高度 = (小地图位置[3] - 小地图位置[1]) / 行数

    # 遍历每个像素
    for x in range(0, img.width, 小地图遍历步长):
        for y in range(0, img.height, 小地图遍历步长):
            # 获取位于 (x, y) 的像素的 RGB 颜色值
            color = pixels[x, y]
            if 小地图角色颜色[0] > color[0] and color[1] > 小地图角色颜色[1] and color[2] > 小地图角色颜色[2]:
                # 向下取整
                返回值 = (int(y // 房间宽度), int(x // 房间高度))
                return 返回值
    返回值 = (999, 999)
    return 返回值


def 取Boss房间(识字):
    """先扫描颜色，再确定坐标，计算出房间号"""
    sct = 识字.get_sct()
    sct_img = sct.grab(小地图位置)
    img = Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb)

    # 加载图像的像素数据
    pixels = img.load()
    行数 = len(小地图路径.地图数据)
    列数 = len(小地图路径.地图数据[0])
    房间宽度 = (小地图位置[2] - 小地图位置[0]) / 列数
    房间高度 = (小地图位置[3] - 小地图位置[1]) / 行数

    # 遍历每个像素
    for x in range(0, img.width, 小地图遍历步长):
        for y in range(0, img.height, 小地图遍历步长):
            # 获取位于 (x, y) 的像素的 RGB 颜色值
            color = pixels[x, y]
            if color[0] > 小地图Boss颜色[0] and color[1] < 小地图Boss颜色[1] and color[2] < 小地图Boss颜色[2]:
                # 向下取整
                返回值 = (int(y // 房间宽度), int(x // 房间高度))
                return 返回值
    返回值 = (999, 999)
    return 返回值


def is距离近(人物坐标, 目的坐标, X距离, Y距离):
    x = abs(人物坐标[0] - 目的坐标[0])
    y = abs(人物坐标[1] - 目的坐标[1])
    if x > X距离 or y > Y距离:
        return False
    else:
        return True


def isBoss房间(识字):
    if 识字.识字(小地图名字) != "" and 取当前房间(识字) == (999, 999) and 取Boss房间(识字) != (999, 999):
        return True
    else:
        return False


def Boss房间处理(识字):
    while not 识字.is通关() or 取当前房间(识字) != (999, 999):
        技能列表 = 获取技能可用列表(识字)
        if 'ctrl' in 技能列表:
            key_press_release('ctrl')
        elif 'alt' in 技能列表:
            key_press_release('alt')
        else:
            释放技能(技能列表)
    key_press_release('v')
    time.sleep(0.5)
    key_press_release('esc')
    time.sleep(2)
    key_press_release('a')
    time.sleep(0.5)
    key_press_release('space')
    time.sleep(0.5)
    key_press_release('left')
    time.sleep(0.5)
    key_press_release('space')
    time.sleep(0.5)
    key_press_release('esc')
    time.sleep(0.5)
    if 有疲劳(识字):
        key_press_release('f10')
    else:
        key_press_release('f12')


def 有疲劳(识字):
    sct = 识字.get_sct()
    sct_img = sct.grab(疲劳位置)
    rgb = np.array(sct_img)
    color = rgb[0, 0]
    color = (color[2], color[1], color[0])
    if color == 疲劳颜色:
        return True
    else:
        return False


def 释放技能(技能列表):
    if 技能列表 is None or len(技能列表) == 0:
        key_press_release('x')
        return
    技能 = 'alt'
    while 技能 == 'alt' or 技能 == 'ctrl':
        技能 = random.choice(技能列表)
        continue
    key_press_release(技能)


def 获取技能可用列表(识字):
    """先扫描颜色，再确定坐标，计算出技能位置"""
    sct = 识字.get_sct()
    sct_img = sct.grab(技能位置)
    img = Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb)

    # 加载图像的像素数据qwerty ctl
    pixels = img.load()
    行数 = 2
    列数 = 7
    可用技能列表 = []
    技能宽度 = img.width / 列数
    技能高度 = img.height / 行数
    for x in range(0, img.width, 小地图遍历步长):
        for y in range(0, img.height, 小地图遍历步长):
            # 获取位于 (x, y) 的像素的 RGB 颜色值
            color = pixels[x, y]
            if color[0] == 技能颜色[0] and color[1] == 技能颜色[1]:  # 这里最好改成某个范围内
                可用技能列表.append(技能字典[int(y // 技能高度), int(x // 技能宽度)])
                continue

    return list(set(可用技能列表))  # 去重


# 调用函数
if __name__ == '__main__':
    # time.sleep(2)
    识字 = 识字初始化()
    print(isBoss房间(识字))
    # while not isBoss房间(识字):
    #     过图(识字)
    # Boss房间处理(识字)
