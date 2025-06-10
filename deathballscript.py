import pyautogui as pg
from pynput import mouse
import threading

clicking = False
click_thread = None

def auto_click():
    while clicking:
        pg.click(clicks=1)  # Один клик за раз
        pg.PAUSE = 0.05    # Небольшая задержка между кликами

def on_click(x, y, button, pressed):
    global clicking, click_thread

    if str(button) == "Button.x2":  # Проверяем боковую кнопку мыши (обычно это "вперёд")
        if pressed:
            if not clicking:  # Если ещё не кликаем
                clicking = True
                click_thread = threading.Thread(target=auto_click, daemon=True)
                click_thread.start()
        else:  # Если кнопку отпустили
            clicking = False  # Останавливаем цикл в auto_click()

if __name__ == "__main__":
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()