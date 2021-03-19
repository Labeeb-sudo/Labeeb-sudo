from PIL import Image, ImageGrab
import time
import os

def takeScreenshot():
    image = ImageGrab.grab()
    image.show()
    # image.save("Screenshort.jpg")
    image.save("wpm=45")
if __name__ == '__main__':
    # you can set the timer as your wish
    time.sleep(2) 
    
    takeScreenshot()
