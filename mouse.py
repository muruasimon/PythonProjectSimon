import pyautogui
import time

while True:
    pyautogui.moveTo(300, 500)
    pyautogui.click()
    time.sleep(60)
    pyautogui.moveTo(300, 600)
    pyautogui.click()
    time.sleep(60)