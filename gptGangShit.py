import pyautogui
import time
from pyperclip import paste
import subprocess
import xerox
import re

def tab(tabCnt=1):
    pyautogui.keyDown('command')
    for i in range(tabCnt):
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
    pyautogui.keyUp('command')

def copy():
    pyautogui.keyDown('command')
    pyautogui.keyDown('c')
    pyautogui.keyUp('command')
    pyautogui.keyUp('c')

def paste():
    pyautogui.keyDown('command')
    pyautogui.keyDown('v')
    pyautogui.keyUp('command')
    pyautogui.keyUp('v')

def all():
    pyautogui.keyDown('command')
    pyautogui.keyDown('a')
    pyautogui.keyUp('command')
    pyautogui.keyUp('a')




# copy the image
subprocess.run(['osascript', '-e', 'set the clipboard to (read (POSIX file \"/Users/ethan/Documents/GitHub/DoNotFail/images/test.jpeg\") as TIFF picture)'])
subprocess.run(['open', '-a', "Google Chrome"])

pyautogui.moveTo(100, 150)
pyautogui.click()
time.sleep(5)

pyautogui.moveTo(700, 1050)
pyautogui.click()
time.sleep(1)
paste()
pyautogui.write("describe to me the contents of the photo")

time.sleep(5)
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

pyautogui.moveTo(900, 600)
pyautogui.click()
time.sleep(15)
all()
time.sleep(1)
copy()


text = xerox.paste()
print(text)

match = re.search(r'ChatGPT(.*?)Regenerate', text, re.DOTALL)

if match:
    extracted_text = match.group(1)
    print(extracted_text)
else:
    print("Pattern not found!")







# tab to chrome
# print("tab to chrome")
# keyboard.send("windows+tab")
# time.sleep(1)

# print("paste")
# # paste the image
# keyboard.send("windows+9")


# type the prompt

