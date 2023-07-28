import logging
import time
from datetime import datetime
import pyautogui
import pydirectinput


def test():
    all_widows = pyautogui.getAllTitles()
    hwnd = pyautogui.getWindowsWithTitle('InsomniaMT2')
    return hwnd
    for window in all_widows:
        if window.startswith("InsomniaMT2") and not window.startswith("InsomniaMT2 Klient"):
            return window

def infinite():
    window = test()
    # print(window)
    #
    # # pyautogui.click(window[0].show())
    # time.sleep(1)
    # pydirectinput.keyDown('z')
    # time.sleep(0.2)
    # pydirectinput.keyUp('z')

    # window[0].minimize()
    counter = 0
    while True:
        print("Number of action >>>> ", counter)
        window[0].activate()
        time.sleep(0.1)
        pydirectinput.keyDown('z')
        time.sleep(0.1)
        pydirectinput.keyUp('z')
        pydirectinput.keyDown('1')
        time.sleep(0.1)
        pydirectinput.keyUp('1')
        pydirectinput.keyDown('space')
        # pyautogui.getWindowsWithTitle(window)[0].minimize()
        counter += 1
        if counter % 3 == 0:
            pydirectinput.keyDown('a')
            time.sleep(0.2)
            pydirectinput.keyUp('a')
            print("Obrót w lewo")
        if counter % 4 == 0:
            pydirectinput.keyDown('w')
            time.sleep(0.2)
            pydirectinput.keyUp('w')
            print("Obrót w przód")

        time.sleep(30)
        # pyautogui.alert(text='Idziemy w to ?', title='Uwaga', button='Wchodzimy')
        time.sleep(0.1)


if __name__ == "__main__":
    logName = datetime.today().strftime('log/%Y_%m_%d_logging.log')
    logging.basicConfig(level=logging.INFO, filename=logName, filemode='w',
                        format='%(asctime)s::%(levelname)s >>> %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.info('Starting main ...')
    infinite()
