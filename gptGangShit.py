import pyautogui
import time
from pyperclip import paste
import subprocess
import xerox
import re
import os
from PIL import Image, ImageGrab
import pyperclip
import base64
import io

def image_to_clipboard(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Copy the image to the clipboard
    img.convert('RGB').toclipboard()

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



def handleImage(path, os_string):
    # copy the image

    # copy the image to the clipboard
    if(os_string == "MAC"):
        subprocess.run(['osascript', '-e', 'set the clipboard to (read (POSIX file \"' + path + '\") as TIFF picture)'])
    elif(os_string == "WIN"):
        image_to_clipboard(path)

    # switch to chrome
    if(os_string == "MAC"):
        subprocess.run(['open', '-a', "Google Chrome"])
    elif(os_string == "WIN"):
        chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        subprocess.Popen(chrome_path)

    # POSITION OF NEW CHAT BUTTON
    pyautogui.moveTo(100, 150)
    pyautogui.click()
    time.sleep(5)

    # POSITION OF TEXT ENTRY BOX
    pyautogui.moveTo(700, 1050)
    pyautogui.click()
    time.sleep(1)
    paste()
    pyautogui.write("you are looking at a photo of a graded assignment can you describe all the text of the questions and answers labelling each indepentently and describe any images. Be sure to also label what are comments left by the TA who graded the work and the grading result (marks added or taken away).")

    time.sleep(5)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    # MIDDLE OF SCREEN
    pyautogui.moveTo(900, 600)
    pyautogui.click()
    time.sleep(30) #adjust to match the length of time it takes to generate the output
    all()
    time.sleep(1)
    copy()

    text = xerox.paste()
    print(text)

    match = re.search(r'ChatGPT(.*?)Regenerate', text, re.DOTALL)

    if match:
        extracted_text = match.group(1)
        return extracted_text
    else:
        print("Pattern not found!")




def list_files(directory):
    absolute_paths = []
    
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            absolute_path = os.path.abspath(os.path.join(foldername, filename))
            absolute_paths.append(str(absolute_path))

    return absolute_paths

# Example usage:
directory = "/Users/ethan/Documents/GitHub/DoNotFail/marked_png"
all_files = list_files(directory)
for file in all_files:
    handleImage(file, "MAC")
    exit()



# tab to chrome
# print("tab to chrome")
# keyboard.send("windows+tab")
# time.sleep(1)

# print("paste")
# # paste the image
# keyboard.send("windows+9")


# type the prompt

