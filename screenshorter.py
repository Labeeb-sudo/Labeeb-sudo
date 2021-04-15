import pyautogui
import time

def takeScreenshot():
    
    img = pyautogui.screenshot()
    time.sleep(2)
    # Apne hisaab se Location daalna aur apne hisaab se naam bhi rakhna
    img.save(r'C:\\Users\\alhaq\\Desktop\\FALTU PYTHON\\ScreenShort using PYTHON\\3rdScreenshot.jpg')
