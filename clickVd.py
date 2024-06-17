import pyautogui
import time


for _ in range(60):
    pyautogui.press("enter")
    time.sleep(15)
    pyautogui.leftClick()
    time.sleep(10)
