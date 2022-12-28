import time
import cv2
import keyboard
import numpy as np
import pyautogui
import win32api
import win32con
from PIL import ImageGrab, ImageOps

replay_button = (956, 549)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def jump():
    keyboard.press('space')


def get_image_sum():
    # img = pyautogui.screenshot(region=(663, 565, 100, 50))
    # img.show() 667, 561, 733,  598
    bbox = [663, 561, 818, 598]
    img = ImageGrab.grab(bbox=bbox)
    gray_image = ImageOps.grayscale(img)
    array = np.array(gray_image.getcolors())
    return array.sum()


def pause_before_run():
    for i in range(3):
        print(i)
        time.sleep(1)


def get_img():
    img = pyautogui.screenshot('screeen.png', region=(667, 561, 70, 40))
    img = cv2.imread('screeen.png')
    cv2.imshow('app', img)
    cv2.waitKey(1)
# click(replay_button[0], replay_button[1])\
# X:  800 Y:  609
# 663 Y:  565
pause_before_run()
while not keyboard.is_pressed('q'):
    sum = get_image_sum()
    print(sum)
    if sum != 5982:
        print('Obstacle')
        jump()
# for i in range(100):
#     get_img()