import pyautogui
from pywinauto import Application
import pyperclip
import time
import subprocess
import os
import re
from io import BytesIO
import win32clipboard
from PIL import Image


def GPT4V(filepath, os_string="WIN"):
    def send_to_clipboard(filepath):
        image = Image.open(filepath)

        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        try:
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        finally:
            win32clipboard.CloseClipboard()
        print("Image copied to clipboard")

    def tab(tabCnt=1):
        pyautogui.keyDown('ctrl')   # Use ctrl instead of command for Windows
        for i in range(tabCnt):
            pyautogui.keyDown('tab')
            pyautogui.keyUp('tab')
        pyautogui.keyUp('ctrl')

    def copy():
        pyautogui.hotkey('ctrl', 'c')   # Simpler way to send a combination of keys

    def paste():
        pyautogui.hotkey('ctrl', 'v')

    def all():
        pyautogui.hotkey('ctrl', 'a')

    def handleImage(files, os_string):
        # Switch to browser
        if os_string == "MAC":
            subprocess.run(['open', '-a', "Google Chrome"])
        elif os_string == "WIN":
            # chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
            app = Application(backend="uia").connect(title_re=".*Chrome.*")
            chrome_window = app.window(title_re=".*Chrome.*")
            if chrome_window.exists():
                chrome_window.set_focus()
            else:
                print("Chrome window not found!")

        # Open new tab
        pyautogui.moveTo(100, 165)
        pyautogui.click()
        time.sleep(2)

        # Click text box, paste, write prompt
        # Copy to clipboard
        for file in files:
            if os_string == "MAC":
                subprocess.run(['osascript', '-e', 'set the clipboard to (read (POSIX file \"' + file + '\") as TIFF picture)'])
            elif os_string == "WIN":
                send_to_clipboard(file)
            pyautogui.moveTo(1060, 960)
            pyautogui.click()
            time.sleep(1)
            paste()
        time.sleep(5)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        time.sleep(10)
        pyautogui.write("You are looking at photos of a graded assignment. There are comments on top of the assignment in boxes, I need you to extract the comments and summarize them, also include what marks were taken off. Do not mention what could've been done better, only what you see. Do this for every picture in order. END_OF_PROMPT")
        time.sleep(5)
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        # Click off, select all
        pyautogui.moveTo(1600, 600)
        pyautogui.click()
        time.sleep(35)
        all()
        time.sleep(1)
        copy()

        text = pyperclip.paste()

        if os_string == "MAC":
            match = re.search(r'ChatGPT(.*?)Regenerate', text, re.DOTALL).group(1)
        elif os_string == "WIN":
            start_index = text.find("ChatGPT") + len("ChatGPT")
            end_index = text.find("END_OF_PROMPT")
            match = text[start_index:end_index].strip()
            print(match)

        if match:
            return match
        else:
            print("Pattern not found!")

    def list_files(directory):
        absolute_paths = []
        for foldername, subfolders, filenames in os.walk(directory):
            for filename in filenames:
                absolute_path = os.path.abspath(os.path.join(foldername, filename))
                absolute_paths.append(str(absolute_path))

        return absolute_paths

    absolute_path = os.path.abspath(os.path.dirname(__file__))

    all_files = list_files(os.path.join(absolute_path, filepath))

    matched_text = handleImage(all_files, os_string)
    with open("marked_text.txt", "w", encoding="utf-8") as outfile:
        outfile.write(matched_text)
    return matched_text
