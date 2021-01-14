from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

'''while keyboard.is_pressed('q') == False:
    while 1:
        if pyautogui.locateOnScreen('stuckman.png', confidece=0.8) != None:
            print("i can see it!")
            time.sleep(0.05)
        else:
            print("i can't see it")
            time.sleep(0.05)'''
time.sleep(2)

#target color (255, 219, 195)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(584,406,749,524))

    width, height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if b == 195:
                click(x+584, y+406)
                time.sleep(0.1)
                break