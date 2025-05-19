import pyautogui as pg
import keyboard as kb
import time
from settings import TARGET_COLOR, COLOR_TOLERANCE

from game_status import check_game_status
from red_color_trigger import check_color_trigger

stop_threads = False

def hold_w_loop():
    global stop_threads
    while not stop_threads:
        game_status = check_game_status()
        if not game_status and check_color_trigger():
            pass
