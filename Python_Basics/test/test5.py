import pyautogui
import time

time.sleep(5)
words = 'Zdravei'

for word in range(10):
    pyautogui.typewrite(words)
    pyautogui.press('enter')
