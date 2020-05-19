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
leftClick = []
leftClick.append(cv2.imread("pic/leftClick/accept_match.png"))
leftClick.append(cv2.imread("pic/leftClick/find_match.png"))
leftClick.append(cv2.imread("pic/leftClick/reconnect.png"))
leftClick.append(cv2.imread("pic/leftClick/replay.png"))
leftClick.append(cv2.imread("pic/leftClick/quit.png"))
leftClick.append(cv2.imread("pic/leftClick/OK.png"))

leftClick.append(cv2.imread("pic/leftClick/item7.png"))
leftClick.append(cv2.imread("pic/leftClick/item6.png"))
leftClick.append(cv2.imread("pic/leftClick/item5.png"))
leftClick.append(cv2.imread("pic/leftClick/item4.png"))
leftClick.append(cv2.imread("pic/leftClick/item3.png"))
leftClick.append(cv2.imread("pic/leftClick/item2.png"))
leftClick.append(cv2.imread("pic/leftClick/item1.png"))
threashLeft = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

rightClick = []
rightClick.append(cv2.imread("pic/rightClick/big_ball.png"))
rightClick.append(cv2.imread("pic/rightClick/mid_ball.png"))
# rightClick.append(cv2.imread("pic/rightClick/small_ball.png"))
threashRight = [0.13, 0.13, 0.2, 0.2, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]

leftClickDelay = []
# leftClickDelay.append(cv2.imread("pic/leftClickDelay/d.png"))
leftClickDelay.append(cv2.imread("pic/leftClickDelay/f.png"))
threashLeftDelay = [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35]

dragStartIcon = []
dragStartIcon.append(cv2.imread("pic/dragStart/item1.png"))
# dragStartIcon.append(cv2.imread("pic/dragStart/item2.png"))
# dragStartIcon.append(cv2.imread("pic/dragStart/item3.png"))
# dragStartIcon.append(cv2.imread("pic/dragStart/item4.png"))
dragEndIcon = []
dragEndIcon.append(cv2.imread("pic/dragEnd/hero1.png"))
dragEndIcon.append(cv2.imread("pic/dragEnd/hero2.png"))
dragEndIcon.append(cv2.imread("pic/dragEnd/hero3.png"))


def left(x, y):
    pyautogui.click(x, y, button='left')  # 左击发货日
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right(x, y):
    pyautogui.click(x, y, button='right')  # 左击发货日
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def drag(startx, starty, endx, endy):
    # m.move(startx, starty)
    pyautogui.click(startx, starty, button='left')  # 左击发货日
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    pyautogui.click(endx, endy, button='left')  # 左击发货日
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


print("作者:星†空")
print("推荐配置:游戏客户端1280x720; 屏幕1920x1080")
print("-----------------------------------------")
print("脚本已启动，请转到游戏界面")
count = 0
while True:
    pic = ImageGrab.grab()
    pic.save("target.jpg")
    target = cv2.imread("target.jpg")

    # 左键点击的图标
    for i in range(len(leftClick)):
        theight, twidth = leftClick[i].shape[:2]
        result = cv2.matchTemplate(target, leftClick[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashLeft[i]:
            left(min_loc[0] + twidth // 2, min_loc[1] + theight // 2)

    # 右键点击的图标
    for i in range(len(rightClick)):
        theight, twidth = rightClick[i].shape[:2]
        result = cv2.matchTemplate(target, rightClick[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashRight[i]:
            right(min_loc[0] + twidth // 2, min_loc[1] + theight // 2)

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

    count += 1
    if (count % 10 == 0):
        for i in range(len(leftClickDelay)):
            theight, twidth = leftClickDelay[i].shape[:2]
            result = cv2.matchTemplate(target, leftClickDelay[i], cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if min_val < threashLeftDelay[i]:
                left(min_loc[0] + twidth // 2, min_loc[1] + theight // 2)
    time.sleep(1)  # 延时两秒
