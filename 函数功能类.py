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


def 选图(地图名):
    识字 = 识字初始化()
    while 识字.获取所选地图名称() != 地图名:
        key_press_release('down')
    key_press_release('space')


def 打怪():
    pass


def 捡物():
    pass


def 过图():
    pass


def 跑到目标(目的坐标, model, sct, 识字, 横轴偏差=0, 纵轴偏差=0):
    人物坐标 = 获取人物坐标(model, sct)
    if 人物坐标 == (0, 0):
        return
    上次房间坐标 = 取当前房间(sct)
    if 上次房间坐标 == (0, 0):
        return
    if is距离近(人物坐标, 目的坐标, 120, 40):
        pass


def 走到目标(目的坐标, model, sct, 按键, 横轴偏差=0, 纵轴偏差=0):
    实时坐标 = 获取人物坐标(model, sct)
    上次房间坐标 = 取当前房间(sct)
    #向右走
    if 目的坐标[0]>实时坐标[0] and 目的坐标[1] == 实时坐标[1]:
        按键.key_press('right')
        while True:
            当前时间 = time.time()
            if 目的坐标[0] <= 实时坐标[0] + 横轴偏差:
                按键.release_all_keys()



def 获取人物坐标(model, sct):
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
    return 0, 0


def 取当前房间(sct):
    """先扫描颜色，再确定坐标，计算出房间号"""
    门开 = False
    sct_img = sct.grab(小地图位置)
    img = Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb)

    # 加载图像的像素数据
    pixels = img.load()
    行数 = len(小地图路径.地图数据)
    列数 = len(小地图路径.地图数据[0])
    房间宽度 = (小地图位置[2] - 小地图位置[0]) / 列数
    房间高度 = (小地图位置[3] - 小地图位置[1]) / 行数
    for x in range(行数):
        for y in range(列数):
            房间起始 = 小地图位置[0]
    # 遍历每个像素
    for x in range(0, img.width, 小地图遍历步长):
        for y in range(0, img.height, 小地图遍历步长):
            # 获取位于 (x, y) 的像素的 RGB 颜色值
            color = pixels[x, y]
            if color == 小地图角色颜色:
                # 向下取整
                返回值 = ((x - 小地图位置[0]) // 房间宽度, (y - 小地图位置[1]) // 房间高度)
                return 返回值
    返回值 = (0, 0)
    return 返回值


def is距离近(人物坐标, 目的坐标, X距离, Y距离):
    x = abs(人物坐标[0] - 目的坐标[0])
    y = abs(人物坐标[1] - 目的坐标[1])
    if x > X距离 or y > Y距离:
        return False
    else:
        return True


# 调用函数
if __name__ == '__main__':
    with mss.mss() as sct:
        取当前房间(sct)
