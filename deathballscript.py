import pyautogui as pg
import keyboard as kb
import time



def main():
    while True:
        if kb.is_pressed('v'):
            pg.click(clicks=10, duration=0.01)
        time.sleep(0.01)    


if __name__ == "__main__":
    main()