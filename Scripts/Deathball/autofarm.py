import pyautogui as pg
import keyboard as kb
import time
from PIL import ImageGrab
import threading

from settings import TARGET_COLOR, COLOR_TOLERANCE, W_HOLD_TIME, NUMBERS_INTERVAL
from game_status import check_game_status



# Флаг для остановки потоков
stop_threads = False

def hold_w_loop():
    global stop_threads
    while not stop_threads:
        if not check_game_status():
            kb.press('w')
            time.sleep(W_HOLD_TIME)
            kb.release('w')
        time.sleep(0.01)

def check_color_trigger():
    global stop_threads
    center_x, center_y = pg.size()[0] // 2, pg.size()[1] // 2
    # center_x, center_y = 780, 620
    while not stop_threads:
        screenshot = ImageGrab.grab(bbox=(center_x, center_y, center_x + 1, center_y + 1))
        pixel = screenshot.getpixel((0, 0))
        
        if all(abs(pixel[i] - TARGET_COLOR[i]) <= COLOR_TOLERANCE for i in range(3)):
            pg.click()
            time.sleep(0.1)
        
        time.sleep(0.01)


 
def press_numbers_loop():
    """Каждые 5 сек нажимает 1,1,1, 2,2,2, 3,3,3. Для спеллов, за них дают опытц1"""
    global stop_threads
    while not stop_threads:
        if check_game_status():
            for number in [1, 1, 1, 2, 2, 2, 3, 3, 3]:
                if stop_threads:
                    break
                kb.press(str(number))
                time.sleep(0.05)
                kb.release(str(number)) 
                time.sleep(0.05)
        time.sleep(NUMBERS_INTERVAL)
def main():
    global stop_threads
    print("Скрипт запущен. Нажмите 'q' для выхода.")
    
    # Запускаем все потоки
    threads = [
        threading.Thread(target=hold_w_loop),
        threading.Thread(target=check_color_trigger),
        threading.Thread(target=press_numbers_loop)
    ]
    
    for thread in threads:
        thread.start()
    
    # Остановка по 'q'
    while not stop_threads:
        if kb.is_pressed('q'):
            stop_threads = True
            print("Завершение работы...")
        time.sleep(0.1)
    
    for thread in threads:
        thread.join()
    print("Скрипт остановлен.")

if __name__ == "__main__":
    main()