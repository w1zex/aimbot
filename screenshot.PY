import pyautogui
import time

time.sleep(2)

img = pyautogui.screenshot(region=(584,406,749,524))
img.save(r'D:\python\projects\aimbot_pic.png')
