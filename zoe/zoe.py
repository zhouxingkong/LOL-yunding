import os
import time

import cv2
import pyautogui
import win32api
import win32con
from PIL import ImageGrab
from pykeyboard import *
from pymouse import *
from pynput.mouse import Controller

mouse = Controller()
m = PyMouse()
k = PyKeyboard()

x1 = [290, 328, 306, 344, 320, 334, 401, 380, 390, 440]
y1 = [755, 722, 691, 664, 633, 595, 663, 634, 595, 633]
x2 = [963, 898, 1017, 964, 1092]
y2 = [645, 563, 571, 492, 636]

leftClickIcon = []
for filename in os.listdir(r'pic/leftClick'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        leftClickIcon.append(cv2.imread('pic/leftClick/' + filename))
threashLeft = [0.2]

rightClickIcon = []
for filename in os.listdir(r'pic/rightClick'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        rightClickIcon.append(cv2.imread('pic/rightClick/' + filename))
threashRight = [0.13]

leftClickDelayIcon = []
for filename in os.listdir(r'pic/leftClickDelay'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        leftClickDelayIcon.append(cv2.imread('pic/leftClickDelay/' + filename))
threashLeftDelay = [0.3]

dragStartIcon = []
for filename in os.listdir(r'pic/dragStart'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        dragStartIcon.append(cv2.imread('pic/dragStart/' + filename))
dragEndIcon = []
for filename in os.listdir(r'pic/dragEnd'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        dragEndIcon.append(cv2.imread('pic/dragEnd/' + filename))

flags = []
flags.append(cv2.imread('pic/flags/in_game_flag.png'))


def leftClick(x, y):
    pyautogui.click(x, y, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def rightClick(x, y):
    pyautogui.click(x, y, button='right')
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

def drag(startx, starty, endx, endy):
    # m.move(startx, starty)
    pyautogui.click(startx, starty, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    pyautogui.click(endx, endy, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

print("作者:星†空")
print("推荐配置:游戏客户端1280x720; 屏幕1920x1080")
print("-----------------------------------------")
print("脚本已启动，请转到游戏界面")
count = 0
index = 0
while True:
    pic = ImageGrab.grab()
    pic.save("target.jpg")
    target = cv2.imread("target.jpg")

    # 左键点击的图标
    for i in range(len(leftClickIcon)):
        theight, twidth = leftClickIcon[i].shape[:2]
        result = cv2.matchTemplate(target, leftClickIcon[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashLeft[0]:
            leftClick(min_loc[0] + twidth // 2, min_loc[1] + theight // 2)

    # 右键点击的图标
    for i in range(len(rightClickIcon)):
        theight, twidth = rightClickIcon[i].shape[:2]
        result = cv2.matchTemplate(target, rightClickIcon[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashRight[0]:
            rightClick(min_loc[0] + twidth // 2, min_loc[1] + theight // 2)

    # for i in range(len(dragStartIcon)):
    #     theight_start, twidth_start = dragStartIcon[i].shape[:2]
    #     result = cv2.matchTemplate(target, dragStartIcon[i], cv2.TM_SQDIFF_NORMED)
    #     min_val_start, max_val_start, min_loc_start, max_loc_start = cv2.minMaxLoc(result)
    #     if min_val_start < 0.15:
    #         print("drag start")
    #         for i in range(len(dragEndIcon)):
    #             theight_end, twidth_end = dragEndIcon[i].shape[:2]
    #             result = cv2.matchTemplate(target, dragEndIcon[i], cv2.TM_SQDIFF_NORMED)
    #             min_val_end, max_val_end, min_loc_end, max_loc_end = cv2.minMaxLoc(result)
    #             if min_val_end < 0.25 and min_loc_end[1]<900 :
    #                 drag(min_loc_start[0] + twidth_start // 2, min_loc_start[1] + theight_start // 2,min_loc_end[0] + twidth_end // 2, min_loc_end[1] + theight_end // 2)
    #                 print("do drag",min_loc_start[0] + twidth_start // 2, min_loc_start[1] + theight_start // 2,min_loc_end[0] + twidth_end // 2, min_loc_end[1] + theight_end // 2)
    #                 break

    # 自动上装备
    count += 1
    if (count % 3 == 0):
        theight, twidth = flags[0].shape[:2]
        result = cv2.matchTemplate(target, flags[0], cv2.TM_SQDIFF_NORMED)  # 检测是否在游戏中
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        # 确认在游戏中再拖拽装备
        if min_val < 0.25:
            drag(x1[index % len(x1)], y1[index % len(y1)], x2[index % len(x2)], y2[index % len(y2)])
        index += 1

    if (count % 10 == 0):
        for i in range(len(leftClickDelayIcon)):
            theight, twidth = leftClickDelayIcon[i].shape[:2]
            result = cv2.matchTemplate(target, leftClickDelayIcon[i], cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if min_val < threashLeftDelay[0]:
                leftClick(min_loc[0] + twidth // 2, min_loc[1] + theight // 2)
    time.sleep(1)  # 延时两秒
