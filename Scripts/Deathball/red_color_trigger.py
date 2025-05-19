import pyautogui as pg
from PIL import ImageGrab
import time

from settings import TARGET_COLOR, COLOR_TOLERANCE


stop_threads = False

def check_color_trigger():
    global stop_threads
    center_x, center_y = pg.size()[0] // 2, pg.size()[1] // 2
    # center_x, center_y = 780, 620
    while not stop_threads:
        screenshot = ImageGrab.grab(bbox=(center_x, center_y, center_x + 1, center_y + 1))
        pixel = screenshot.getpixel((0, 0))
        
        if all(abs(pixel[i] - TARGET_COLOR[i]) <= COLOR_TOLERANCE for i in range(3)):
            return True  
        
        time.sleep(0.001)
    
    return False  