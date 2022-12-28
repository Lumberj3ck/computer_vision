import time
import keyboard
import pyautogui
import win32api
import win32con

# X:  507 Y:  862 RGB: (161, 165, 232)
# X:  625 Y:  856 RGB: (154, 161, 230)
# X:  725 Y:  843 RGB: (165, 170, 232)
# X:  836 Y:  843 RGB: (253,  18,   1)
coords = [(507, 400), (625, 400), (725, 400), (836, 400)]
Y = 410

# coords = [(507, 862), (625, 856), (725, 843), (836, 843)]
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while True:
    if keyboard.is_pressed('s') == False:
        continue
    while keyboard.is_pressed('q') == False:
        if pyautogui.pixel(507, 400)[0] == 0:
            click(507, Y)
        if pyautogui.pixel(625, 400)[0] == 0:
            click(625, Y)
        if pyautogui.pixel(725, 400)[0] == 0:
            click(725, Y)
        if pyautogui.pixel(836, 400)[0] == 0:
            click(836, Y)
    break
print('Script finished!')
# print(pyautogui.displayMousePosition())
# click(148, 1045)
