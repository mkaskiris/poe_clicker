import time
import clipboard
import pyautogui
import re
import keyboard


def set_xy():
    print('Press q on the location of alts')
    while True:
        if keyboard.is_pressed('q'):
            x_alt, y_alt = pyautogui.position()
            break

    time.sleep(1)
    print('Press q on the location of augs')
    while True:
        if keyboard.is_pressed('q'):
            x_aug, y_aug = pyautogui.position()
            break

    time.sleep(1)
    print('Press q on the location of the item')
    while True:
        if keyboard.is_pressed('q'):
            x_item, y_item = pyautogui.position()
            break

    return x_alt, y_alt, x_aug, y_aug, x_item, y_item


def test_clicker():
    clip = ''
    mod = 'Spiny'
    base = ['Destiny', 'Leather']
    prefix = True
    suffix = False

    # x_alt, y_alt, x_aug, y_aug, x_item, y_item = set_xy()
    # time.sleep(0.5)

    x_alt = 118
    y_alt = 289
    x_aug = 235
    y_aug = 343
    x_item = 330
    y_item = 424

    alt_click(x_alt, y_alt)

    while not re.search(mod, clip):

        clip = item_click(x_item, y_item)
        print(clip)
        affix = strip_affix(clip.splitlines()[1].split(), base)
        if affix == 2:  # item full
            continue
        elif (affix == -1 and suffix) or (affix == 1 and prefix):    # Item has prefix and we are looking for suffix
            aug_click(x_aug, y_aug)
            clip = item_click(x_item, y_item)
            alt_click(x_alt, y_alt)

    pyautogui.keyUp('shift')
    print(clip)
    print("Mod Achieved")


def item_click(x_item, y_item):
    pyautogui.click(x_item, y_item, button='left', duration=0.2)
    time.sleep(0.2)
    pyautogui.hotkey('ctrlleft', 'c')
    time.sleep(0.1)
    clip = clipboard.paste()
    return clip


def aug_click(x, y):
    pyautogui.keyUp('shift')
    time.sleep(0.1)
    pyautogui.click(x, y, button='right', duration=0.3)


def alt_click(x, y):
    pyautogui.keyDown('shift')
    time.sleep(0.1)
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.rightClick()


def strip_affix(clip, base):
    for x in base:
        clip.remove(x)

    try:
        if clip.index("of") > 0:
            # print("suffix and prefix")
            return 2
        else:
            # print("suffix only")
            return 1
    except ValueError:
        # print("prefix only")
        return -1


test_clicker()