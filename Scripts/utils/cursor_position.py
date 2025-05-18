import pyautogui as pd
import time

def get_cursor_position():
    counter = 0
    while counter < 30:
        x_y_position = pd.position()
        print(x_y_position)
        counter += 1
        time.sleep(0.5)
get_cursor_position()

