import keyboard
import time
import pyautogui as p


def on_shift_press(event):
    if event.name == 'shift' and event.event_type == keyboard.KEY_DOWN:
        keyboard.press('ctrl')
        time.sleep(0.015)  # небольшая задержка для надежности
        keyboard.press('space')
        time.sleep(0.015)  # небольшая задержка для нцадежности
        keyboard.release('ctrl')
        time.sleep(0.015)  # небольшая задержка для надежности
        keyboard.release('space')
        time.sleep(0.1)

def f_scythe(event):
    if event.name == 'f' and event.event_type == keyboard.KEY_DOWN:
        time.sleep(0.15)
        p.click(button='right')
        p.click()

        
# Регистрируем обработчик нажатия Shift
keyboard.hook_key('shift', on_shift_press)
keyboard.hook_key('f', f_scythe)

# Оставляем программу работающей
print("Скрипт запущен. Нажмите Shift для эмуляции Ctrl+Space.")
print("Для выхода нажмите Ctrl+C")

try:
    keyboard.wait()  # ждем, пока пользователь не прервет программу
except KeyboardInterrupt:
    print("\nСкрипт остановлен.")