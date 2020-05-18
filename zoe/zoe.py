import time

import cv2
import pyautogui
import win32api
import win32con
from PIL import ImageGrab
from pykeyboard import *
from pymouse import *
from pynput.mouse import Controller

key_map = {
    "0": 49, "1": 50, "2": 51, "3": 52, "4": 53, "5": 54, "6": 55, "7": 56, "8": 57, "9": 58,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90
}

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

leftClick.append(cv2.imread("pic/leftClick/item1.png"))
leftClick.append(cv2.imread("pic/leftClick/item2.png"))
leftClick.append(cv2.imread("pic/leftClick/item3.png"))
leftClick.append(cv2.imread("pic/leftClick/item4.png"))
leftClick.append(cv2.imread("pic/leftClick/item5.png"))
leftClick.append(cv2.imread("pic/leftClick/item6.png"))
leftClick.append(cv2.imread("pic/leftClick/item7.png"))
threashLeft = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]

rightClick = []
rightClick.append(cv2.imread("pic/rightClick/mid_ball.png"))
# rightClick.append(cv2.imread("pic/rightClick/small_ball.png"))
threashRight = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]

leftClickDelay = []
# leftClickDelay.append(cv2.imread("pic/leftClickDelay/d.png"))
leftClickDelay.append(cv2.imread("pic/leftClickDelay/f.png"))
threashLeftDelay = [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35]

print("作者:星†空")
print("脚本已启动，请转到游戏界面")
count = 0
while True:
    pic = ImageGrab.grab()
    pic.save("target.jpg")
    target = cv2.imread("target.jpg")
    for i in range(len(leftClick)):
        theight, twidth = leftClick[i].shape[:2]
        result = cv2.matchTemplate(target, leftClick[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashLeft[i]:
            pyautogui.click(min_loc[0] + twidth // 2, min_loc[1] + theight // 2, button='left')  # 左击发货日
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    for i in range(len(rightClick)):
        theight, twidth = rightClick[i].shape[:2]
        result = cv2.matchTemplate(target, rightClick[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashRight[i]:
            pyautogui.click(min_loc[0] + twidth // 2, min_loc[1] + theight // 2, button='right')  # 左击发货日
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

    count += 1
    if (count % 10 == 0):
        for i in range(len(leftClickDelay)):
            theight, twidth = leftClickDelay[i].shape[:2]
            result = cv2.matchTemplate(target, leftClickDelay[i], cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if min_val < threashLeftDelay[i]:
                pyautogui.click(min_loc[0] + twidth // 2, min_loc[1] + theight // 2, button='left')  # 左击发货日
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(1)  # 延时两秒
