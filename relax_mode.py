import pyautogui
from keyboard import is_pressed

print('Нажмите \'n\' для запуска.')
print('Нажмите \'m\' чтобы выйти.')


while True:
    if is_pressed('n'):
        while True:
            if is_pressed('m'):
                exit()
            x, y = pyautogui.position()
            if pyautogui.pixel(x, y)[1] == 0:
                pyautogui.click(x, y)
