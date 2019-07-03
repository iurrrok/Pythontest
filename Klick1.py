# -*- coding: utf-8 -*-

import pyautogui
import time

print("Через 6 секунд запустится АвтоКликер!!!")
for x in range(6):
    print(x+1)
    time.sleep(1)
else:
    print("============================")
    print("АвтоКликер запустился!")


def action():
    pyautogui.moveTo(500, 650, duration=2)
    pyautogui.click(interval=10)  # waiting 10 seconds
    pyautogui.click()
    time.sleep(1)  # waiting 1 sec
    pyautogui.hotkey('ctrl', 'w')  # close window


action()
print("Fin!")