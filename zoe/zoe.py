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

heroPosX = [963, 898, 1017, 964, 1092, 1157, 1225]
heroPosY = [645, 563, 571, 492, 636, 561, 631]
watcherPosX = [446, 555, 674, 790, 906, 1022, 1137, 1253, 1366]
watcherPosY = [744, 739, 742, 743, 743, 744, 743, 744, 743]

# heroPosX = heroPosX + watcherPosX
# heroPosY = heroPosY + watcherPosY

X_START = 240
X_END = 1700
Y_START = 100
Y_END = 1080

leftClickIcon = []
for filename in os.listdir(r'pic/leftClick'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        leftClickIcon.append(cv2.imread('pic/leftClick/' + filename))
threashLeft = [0.21]

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

judgeHeroIcon = []
for filename in os.listdir(r'pic/judge'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        judgeHeroIcon.append(cv2.imread('pic/judge/' + filename))
threashjudgeHero = [0.15]

flags = []
flags.append(cv2.imread('pic/flags/in_game_flag.png'))
flags.append(cv2.imread('pic/flags/heroInfoFlag.png'))
flags.append(cv2.imread('pic/flags/fighting_flag.png'))


# --------------------------------动作-------------------------------------

def moveTo(x, y):
    pyautogui.click(x, y, button='left')


def leftClick(x, y):
    pyautogui.click(x, y, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def rightClick(x, y):
    pyautogui.click(x, y, button='right')
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def drag(startx, starty, endx, endy):
    # m.move(startx, starty)
    pyautogui.click(startx, starty, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    pyautogui.click(endx, endy, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def judgeInGame():
    # theight, twidth = flags[0].shape[:2]
    result = cv2.matchTemplate(target, flags[0], cv2.TM_SQDIFF_NORMED)  # 检测是否在游戏中
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 确认在游戏中再拖拽装备
    return min_val < 0.25


print("作者:星†空")
print("推荐配置:游戏客户端1280x720; 屏幕1920x1080")
print("-----------------------------------------")
print("脚本已启动，请转到游戏界面")
count = 0
index = 0
lastFTime = time.time()
lastJudgeHeroTime = time.time()
needJudgeHero = False
needJudgeWatcher = False
judgeHeroIndex = 0
judgeWatcherIndex = 0

while True:
    pic = ImageGrab.grab()
    pic.save("target.jpg")
    target = cv2.imread("target.jpg")

    target = target[Y_START:Y_END, X_START:X_END]

    if needJudgeHero or needJudgeWatcher:
        result = cv2.matchTemplate(target, flags[1], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < 0.25:
            needCell = True
            for i in range(len(judgeHeroIcon)):
                result = cv2.matchTemplate(target, judgeHeroIcon[i], cv2.TM_SQDIFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                if min_val < threashjudgeHero[0]:
                    needCell = False
            if needCell:
                if needJudgeHero: drag(heroPosX[judgeHeroIndex], heroPosY[judgeHeroIndex], 940, 993)
                if needJudgeWatcher: drag(watcherPosX[judgeWatcherIndex], watcherPosY[judgeWatcherIndex], 940, 993)
            needJudgeHero = False
            needJudgeWatcher = False

    # 左键点击的图标
    for i in range(len(leftClickIcon)):
        theight, twidth = leftClickIcon[i].shape[:2]
        result = cv2.matchTemplate(target, leftClickIcon[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashLeft[0]:
            leftClick(min_loc[0] + twidth // 2 + X_START, min_loc[1] + theight // 2 + Y_START)

    if judgeInGame():  # 判断是否在游戏中
        # 右键点击的图标
        for i in range(len(rightClickIcon)):
            theight, twidth = rightClickIcon[i].shape[:2]
            result = cv2.matchTemplate(target, rightClickIcon[i], cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if min_val < threashRight[0]:
                rightClick(min_loc[0] + twidth // 2 + X_START, min_loc[1] + theight // 2 + Y_START)

        # 自动上装备
        count += 1
        if count % 3 == 0:
            drag(x1[index % len(x1)], y1[index % len(y1)], x2[index % len(x2)], y2[index % len(y2)])
            index += 1

        t = time.time()
        if t - lastFTime > 42:  # 30秒钟F一次
            for i in range(len(leftClickDelayIcon)):
                theight, twidth = leftClickDelayIcon[i].shape[:2]
                result = cv2.matchTemplate(target, leftClickDelayIcon[i], cv2.TM_SQDIFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                if min_val < threashLeftDelay[0]:
                    leftClick(min_loc[0] + twidth // 2 + X_START, min_loc[1] + theight // 2 + Y_START)
                    time.sleep(0.1)
                    moveTo(500, 500)
            lastFTime = t

        # 查看英雄信息必须放到每个循环最后
        t = time.time()
        if t - lastJudgeHeroTime > 6:  # 30秒钟查看一次英雄
            target2 = target[660 - Y_START:1080, :]
            result = cv2.matchTemplate(target2, flags[2], cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if min_val < 0.25:
                judgeHeroIndex = (judgeHeroIndex + 1) % len(heroPosX)
                rightClick(heroPosX[judgeHeroIndex], heroPosY[judgeHeroIndex])
                needJudgeHero = True
                lastJudgeHeroTime = t
            else:
                judgeWatcherIndex = (judgeWatcherIndex + 1) % len(watcherPosX)
                rightClick(watcherPosX[judgeWatcherIndex], watcherPosY[judgeWatcherIndex])
                needJudgeWatcher = True
                lastJudgeHeroTime = t
    time.sleep(0.2)  # 延时两秒
