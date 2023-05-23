from keyboard import is_pressed
from pyautogui import pixel
from win32api import SetCursorPos, mouse_event
from win32con import MOUSEEVENTF_LEFTDOWN as mouse_down
from win32con import MOUSEEVENTF_LEFTUP as mouse_up

#  here comes da spaghetti code
#  600X 160Y upper left, 180 each 600-1320X 160-880Y
tiles = ((690, 250),
         (880, 250),
         (1060, 250),
         (1240, 250),
         (690, 430),
         (880, 430),
         (1060, 430),
         (1240, 430),
         (690, 610),
         (880, 610),
         (1060, 610),
         (1240, 610),
         (690, 790),
         (880, 790),
         (1060, 790),
         (1240, 790))


def click(pog, gers):
    SetCursorPos((pog, gers))
    mouse_event(mouse_down, 0, 0)
    mouse_event(mouse_up, 0, 0)


print('Для запуска нажмите \'n\'.')
print('Для выхода нажмите \'m\'')

while True:
    if is_pressed('n'):
        while True:
            for i in range(len(tiles)):
                if is_pressed('m'):
                    exit()
                x, y = tiles[i][0], tiles[i][1]
                if pixel(x, y)[1] == 0:
                    click(x, y)
