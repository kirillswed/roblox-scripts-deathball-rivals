import pyautogui as pg
import keyboard as kb
import time
from PIL import ImageGrab
import threading

stop_threads = False

def spam_f_loop():
    global stop_threads
    while not stop_threads:
        kb.press('F')
        time.sleep(0.01)

def main():
    global stop_threads
    print("Скрипт запущен. Нажмите 'q' для выхода.")
    
    # Запускаем все потоки
    threads = [
        threading.Thread(target=spam_f_loop)
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