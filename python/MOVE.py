# mouse move automation

import pyautogui
import time

print("Moving mouse in 3 seconds... switch to your Notepad!")
time.sleep(3)

# This will move your mouse in a square, like your paddle logic
pyautogui.moveRel(-100, 0, duration=0.5)
pyautogui.moveRel(0, 100, duration=0.5)
pyautogui.moveRel(100, 0, duration=0.5)
pyautogui.moveRel(0, -100, duration=0.5)

#pyautogui.displayMousePosition()

#pyautogui.screenshot('c:/users/siddhu303/desktop/new.jpg')

print("Done!")