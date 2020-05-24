import os
import random
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
x2 = [963, 898, 964, 1092, 1017, 1084, 1225, 1152]
y2 = [645, 563, 492, 636, 571, 488, 631, 555]

# 场上英雄坐标(加入部分观众席英雄坐标)
heroPosX = [963, 898, 964, 1092, 1017, 1084, 1225, 1152] + [446, 555, 674, 790, 906, 1022]
heroPosY = [645, 563, 492, 636, 571, 488, 631, 555] + [744, 739, 742, 743, 743, 744]
# 观众席坐标
watcherPosX = [446, 555, 674, 790, 906, 1022, 1137, 1253, 1366]
watcherPosY = [744, 739, 742, 743, 743, 744, 743, 744, 743]
# 英雄是否就位
isPosReady = [True, False, False, False, False, False, False, False]
isHeroInPlace = [False, False, False, False, False, False, False, False]
placeNum = 1
inPlaceHeroNum = 0

heroItem = [0, 4, 5]

X_START = 240
X_END = 1700
Y_START = 200
Y_END = 1080
size = (X_START, Y_START, X_END, Y_END)

index = 0
lastFTime = time.time()  # 上一次上人口的时间
lastJudgeHeroTime = time.time()  # 上一次判断英雄的时间
lastItemTime = time.time()  # 上一次上装备的时间

needJudgeHero = False
needJudgeWatcher = False
judgeHeroIndex = 0
judgeWatcherIndex = 0

# --------------------------加载图片资源----------------------

leftClickIcon = []
for filename in os.listdir(r'pic/leftClick/start'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        leftClickIcon.append(cv2.imread('pic/leftClick/start/' + filename))
for filename in os.listdir(r'pic/leftClick/end'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        leftClickIcon.append(cv2.imread('pic/leftClick/end/' + filename))
for filename in os.listdir(r'pic/leftClick/heros'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        leftClickIcon.append(cv2.imread('pic/leftClick/heros/' + filename))
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
flags.append(cv2.imread('pic/flags/in_game_flag2.png'))
flags.append(cv2.imread('pic/flags/heroInfoFlag.png'))
flags.append(cv2.imread('pic/flags/fighting_flag.png'))


# --------------------------------动作-------------------------------------

def moveTo(x, y):
    m.move(x, y)


def moveToSpace():
    moveTo(500, 500)

#左击
def leftClick(x, y):
    pyautogui.click(x, y, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

#右击
def rightClick(x, y):
    pyautogui.click(x, y, button='right')
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

#拖拽
def drag(startx, starty, endx, endy):
    pyautogui.click(startx, starty, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    pyautogui.click(endx, endy, button='left')
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# --------------------------------------------------------

def judgeInGame():
    result = cv2.matchTemplate(target, flags[0], cv2.TM_SQDIFF_NORMED)  # 检测是否在游戏中
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if min_val < 0.25: return min_val < 0.25
    result = cv2.matchTemplate(target, flags[1], cv2.TM_SQDIFF_NORMED)  # 检测是否在游戏中
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return min_val < 0.25


# 判断选中的是哪个英雄
def judgeHero():
    hero = -1
    for i in range(len(judgeHeroIcon)):
        result = cv2.matchTemplate(target, judgeHeroIcon[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashjudgeHero[0]:
            hero = i
    return hero


def startNewGame():
    for i in range(len(isHeroInPlace)):
        isHeroInPlace[i] = False
        isPosReady[i] = False
    inPlaceHeroNum = 0
    placeNum = 1
    print("新的一局")


print(" ________  _____ ")
print("|__  / _ \| ____|")
print("  / / | | |  _|  ")
print(" / /| |_| | |___ ")
print("/____\___/|_____|")
print("")
print("----作者:星†空----")
print("免费软件，切勿用作商业目的!!!!!!")
print("网址: github.com/zhouxingkong/LOL-yunding")
print("-----------------------------------------")
print("脚本已启动，请转到游戏界面")

while True:
    pic = ImageGrab.grab(size)
    pic.save("target.jpg")
    target = cv2.imread("target.jpg")

    if needJudgeHero or needJudgeWatcher:
        result = cv2.matchTemplate(target, flags[2], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < 0.25:
            if judgeHeroIndex < len(isPosReady) and not isPosReady[judgeHeroIndex]:
                isPosReady[judgeHeroIndex] = True
                placeNum += 1
            hero = judgeHero()
            if hero < 0 and needJudgeHero:  # 这个英雄不能要
                drag(heroPosX[judgeHeroIndex], heroPosY[judgeHeroIndex], 940, 993)
                if judgeHeroIndex < len(isHeroInPlace) and isHeroInPlace[judgeHeroIndex]:
                    isHeroInPlace[judgeHeroIndex] = False
                    inPlaceHeroNum -= 1
                if needJudgeWatcher: drag(watcherPosX[judgeWatcherIndex], watcherPosY[judgeWatcherIndex], 940, 993)
            elif needJudgeHero and judgeHeroIndex < len(isHeroInPlace) and isHeroInPlace[
                judgeHeroIndex]:  # 该位置的英雄已经标记就位
                if judgeHeroIndex != hero:  # 标记错了，清除标记
                    isHeroInPlace[judgeHeroIndex] = False
                    inPlaceHeroNum -= 1
            elif not isHeroInPlace[hero]:  # 如果该英雄还没就位
                if needJudgeHero and isPosReady[hero]:
                    drag(heroPosX[judgeHeroIndex], heroPosY[judgeHeroIndex], heroPosX[hero], heroPosY[hero])
                    isHeroInPlace[hero] = True
                    inPlaceHeroNum+=1
            needJudgeHero = False
            needJudgeWatcher = False

    # 左键点击的图标
    for i in range(len(leftClickIcon)):
        theight, twidth = leftClickIcon[i].shape[:2]
        result = cv2.matchTemplate(target, leftClickIcon[i], cv2.TM_SQDIFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if min_val < threashLeft[0]:
            leftClick(min_loc[0] + twidth // 2 + X_START, min_loc[1] + theight // 2 + Y_START)
            if i < 1: startNewGame()  #判断是否开启一局新游戏

    if judgeInGame():  # 判断是否在游戏中
        # 右键点击的图标
        for i in range(len(rightClickIcon)):
            theight, twidth = rightClickIcon[i].shape[:2]
            result = cv2.matchTemplate(target, rightClickIcon[i], cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if min_val < threashRight[0]:
                rightClick(min_loc[0] + twidth // 2 + X_START, min_loc[1] + theight // 2 + Y_START)
                time.sleep(0.1)
                moveToSpace()

        # 自动上装备
        t = time.time()
        if t - lastItemTime > 10:
            dst = random.randint(0, len(heroItem) - 1)
            drag(x1[index % len(x1)], y1[index % len(y1)], x2[heroItem[dst]], y2[heroItem[dst]])
            time.sleep(0.1)
            moveToSpace()
            index += 1
            lastItemTime = t

        t = time.time()
        if t - lastFTime > 42:  # 42秒钟F一次
            for i in range(len(leftClickDelayIcon)):
                theight, twidth = leftClickDelayIcon[i].shape[:2]
                result = cv2.matchTemplate(target, leftClickDelayIcon[i], cv2.TM_SQDIFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                if min_val < threashLeftDelay[0]:
                    leftClick(min_loc[0] + twidth // 2 + X_START, min_loc[1] + theight // 2 + Y_START)
                    time.sleep(0.1)
                    moveToSpace()
            lastFTime = t

        # 查看英雄信息必须放到每个循环最后
        t = time.time()
        if t - lastJudgeHeroTime > 4:  # 4秒钟查看一次英雄
            target2 = target[660 - Y_START:1080, :]
            result = cv2.matchTemplate(target2, flags[3], cv2.TM_SQDIFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if min_val < 0.25 and inPlaceHeroNum < len(isHeroInPlace):
                judgeHeroIndex = (judgeHeroIndex + 1) % len(heroPosX)
                while judgeHeroIndex < len(isHeroInPlace) and judgeHeroIndex > placeNum:
                    judgeHeroIndex = (judgeHeroIndex + 1) % len(isHeroInPlace)

                rightClick(heroPosX[judgeHeroIndex], heroPosY[judgeHeroIndex])
                needJudgeHero = True
                lastJudgeHeroTime = t
            else:
                judgeWatcherIndex = (judgeWatcherIndex + 1) % len(watcherPosX)
                rightClick(watcherPosX[judgeWatcherIndex], watcherPosY[judgeWatcherIndex])
                needJudgeWatcher = True
                lastJudgeHeroTime = t
    time.sleep(0.2)  # 延时两秒
