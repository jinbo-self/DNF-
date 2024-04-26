import ctypes
from ctypes import wintypes
import time

import keyboard
import pyautogui
import win32api
import win32con

KEY_MAP = {
    'backspace': 0x08, 'tab': 0x09, 'clear': 0x0C, 'enter': 0x0D,
    'shift': 0x10, 'ctrl': 0x11, 'alt': 0x12, 'pause': 0x13, 'caps_lock': 0x14,
    'esc': 0x1B, ' ': 0x20, 'page_up': 0x21, 'page_down': 0x22,
    'end': 0x23, 'home': 0x24, 'left': 0x25, 'up': 0x26,
    'right': 0x27, 'down': 0x28, 'select': 0x29, 'print': 0x2A,
    'execute': 0x2B, 'print_screen': 0x2C, 'insert': 0x2D, 'delete': 0x2E,
    'help': 0x2F, '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34,
    '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39,
    'a': 0x41, 'b': 0x42, 'c': 0x43, 'd': 0x44, 'e': 0x45, 'f': 0x46,
    'g': 0x47, 'h': 0x48, 'i': 0x49, 'j': 0x4A, 'k': 0x4B, 'l': 0x4C,
    'm': 0x4D, 'n': 0x4E, 'o': 0x4F, 'p': 0x50, 'q': 0x51, 'r': 0x52,
    's': 0x53, 't': 0x54, 'u': 0x55, 'v': 0x56, 'w': 0x57, 'x': 0x58,
    'y': 0x59, 'z': 0x5A, 'left_window': 0x5B, 'right_window': 0x5C,
    'applications': 0x5D, 'sleep': 0x5F, 'numpad_0': 0x60, 'numpad_1': 0x61,
    'numpad_2': 0x62, 'numpad_3': 0x63, 'numpad_4': 0x64, 'numpad_5': 0x65,
    'numpad_6': 0x66, 'numpad_7': 0x67, 'numpad_8': 0x68, 'numpad_9': 0x69,
    'multiply_key': 0x6A, 'add_key': 0x6B, 'separator_key': 0x6C,
    'subtract_key': 0x6D, 'decimal_key': 0x6E, 'divide_key': 0x6F,
    'F1': 0x70, 'F2': 0x71, 'F3': 0x72, 'F4': 0x73, 'F5': 0x74,
    'F6': 0x75, 'F7': 0x76, 'F8': 0x77, 'F9': 0x78, 'F10': 0x79,
    'F11': 0x7A, 'F12': 0x7B, 'F13': 0x7C, 'F14': 0x7D, 'F15': 0x7E,
    'F16': 0x7F, 'F17': 0x80, 'F18': 0x81, 'F19': 0x82, 'F20': 0x83,
    'F21': 0x84, 'F22': 0x85, 'F23': 0x86, 'F24': 0x87,
    'num_lock': 0x90, 'scroll_lock': 0x91,
    'left_shift': 0xA0, 'right_shift ': 0xA1, 'left_control': 0xA2,
    'right_control': 0xA3, 'left_menu': 0xA4, 'right_menu': 0xA5,
    'browser_back': 0xA6, 'browser_forward': 0xA7, 'browser_refresh': 0xA8,
    'browser_stop': 0xA9, 'browser_search': 0xAA, 'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC, 'volume_mute': 0xAD, 'volume_down': 0xAE,
    'volume_up': 0xAF, 'next_track': 0xB0, 'previous_track': 0xB1,
    'stop_media': 0xB2, 'play/pause_media': 0xB3, 'start_mail': 0xB4,
    'select_media': 0xB5, 'start_application_1': 0xB6, 'start_application_2': 0xB7,
    'attn_key': 0xF6, 'crsel_key': 0xF7, 'exsel_key': 0xF8, 'play_key': 0xFA,
    'zoom_key': 0xFB, 'clear_key': 0xFE
}

def mouse_move(x, y):
    """
    移动鼠标到指定的(x, y)坐标位置。
    """
    win32api.SetCursorPos((x, y))


def mouse_click():
    """
    模拟鼠标点击。默认为左键点击，可以通过 'button' 参数指定 'left', 'right', 或 'middle'。
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.05)  # 点击持续时间
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def key_press_release(key_name, delay=0.01):
    """
    模拟按键的长按功能，持续按下指定的键'key_code'，持续时间为'delay'秒。
    """
    key_code = KEY_MAP[key_name]
    hard_keydb = win32api.MapVirtualKey(key_code, 0)
    # 开始时间
    start_time = time.time()

    # 按下按键
    while (time.time() - start_time) < delay:
        win32api.keybd_event(key_code, hard_keydb, 0, 0)
        time.sleep(0.01)  # 微小延时

    # 释放按键
    win32api.keybd_event(key_code, hard_keydb, win32con.KEYEVENTF_KEYUP, 0)

# 使用示例
if __name__ == "__main__":
    time.sleep(2)  # 延时2秒，给你时间准备切换到一个可以接收输入的地方

    key_press_release('down',3)
