import time
import clipboard
import pyautogui
import re
import keyboard

# Used to find the position of alts and item
def mouse_position():
    print('Press Ctrl-F2 to quit, for PyCharm.')
    while True:
        # Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

        print(positionStr, end='')
        time.sleep(0.01)
        print('\b' * len(positionStr), end='', flush=True)


def set_xy():
    print('Press q on the location of alts')
    while True:
        if keyboard.is_pressed('q'):
            x_alt, y_alt = pyautogui.position()
            positionStr = 'X: ' + str(x_alt).rjust(4) + ' Y: ' + str(y_alt).rjust(4)
            print(positionStr)
            break

    time.sleep(1)
    print('Press q on the location of the item')
    while True:
        if keyboard.is_pressed('q'):
            x_item, y_item = pyautogui.position()
            positionStr = 'X: ' + str(x_item).rjust(4) + ' Y: ' + str(y_item).rjust(4)
            print(positionStr)
            break

    return x_alt, y_alt, x_item, y_item



def alt_clicker():

    # Coordinates of alts and item for my pc
    #x_alt = 105
    #y_alt = 295
    #x_item = 322
    #y_item = 472

    x_alt, y_alt, x_item, y_item = set_xy()
    time.sleep(1)
    
    clip = ""  # item on clipboard
    mod = "blaaa"  # desired mod
    tries = 0

    # Grab initial alteration
    pyautogui.click(x_alt, y_alt, button='right')
    time.sleep(0.2)
    pyautogui.keyDown('shift')

    # While mod not found on clipboard keep using alts
    while not re.search(mod, clip):
        print('Try: ' + str(tries))

        pyautogui.click(x_item, y_item, button='left')  # use alt on item
        tries = tries + 1  # Increment tries
        time.sleep(0.2)

        # Copy item mods
        pyautogui.hotkey('ctrlleft', 'c')
        clip = clipboard.paste()
        print(clip)  # Prints item to screen for testing

        if tries == 3:  # Number of tries before the script stops
            pyautogui.keyUp('shift')
            print('mod not found')
            exit()

        # time.sleep(0.2)

    pyautogui.keyUp('shift')
    print('mod found, script ending')


#mouse_position()

alt_clicker()
