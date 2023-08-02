import sys
import time
import pyautogui
import pydirectinput


def use_quick_access_inventory():
    print("Use quick access of inventory")
    pydirectinput.keyDown('1')
    time.sleep(0.1)
    pydirectinput.keyUp('1')
    pydirectinput.keyDown('2')
    time.sleep(0.1)
    pydirectinput.keyUp('2')
    pydirectinput.keyDown('3')
    time.sleep(0.1)
    pydirectinput.keyUp('3')
    pydirectinput.keyDown('4')
    time.sleep(0.1)
    pydirectinput.keyUp('4')


def terminate_spot():
    pydirectinput.keyDown('1')
    time.sleep(0.1)
    pydirectinput.keyUp('1')
    time.sleep(0.1)
    pydirectinput.keyDown('space')
    time.sleep(10)
    pydirectinput.keyUp('space')
    pydirectinput.keyDown('z')
    time.sleep(0.1)
    pydirectinput.keyUp('z')


def logout():
    print("Logout")
    time.sleep(0.1)
    pydirectinput.leftClick(1264, 967)
    time.sleep(1)
    pydirectinput.leftClick(655, 573)


def open_main_inventory():
    print("Opening main inventory")
    time.sleep(0.1)
    pydirectinput.leftClick(1192, 970)


def change_chanel(chanel):
    if chanel == 1:
        time.sleep(0.1)
        pydirectinput.leftClick(1156, 81)
        time.sleep(4)
        return

    if chanel == 2:
        time.sleep(0.1)
        pydirectinput.leftClick(1154, 102)
        time.sleep(4)
        return

    if chanel == 3:
        time.sleep(0.1)
        pydirectinput.leftClick(1160, 127)
        time.sleep(4)
        return

    if chanel == 4:
        time.sleep(0.1)
        pydirectinput.leftClick(1174, 147)
        time.sleep(4)
        return


def use_main_inventory_slots(number):
    if number < 1 or number > 5:
        return False

    print(f'Use slot {number} of main inventory')

    if number == 1:
        time.sleep(0.1)
        pydirectinput.rightClick(1137, 645)
        return True

    if number == 2:
        time.sleep(0.1)
        pydirectinput.rightClick(1168, 645)
        return True

    if number == 3:
        time.sleep(0.1)
        pydirectinput.rightClick(1200, 645)
        return True

    if number == 4:
        time.sleep(0.1)
        pydirectinput.rightClick(1234, 645)
        return True

    if number == 5:
        time.sleep(0.1)
        pydirectinput.rightClick(1264, 645)
        return True


class AutoClicker:
    def __init__(self, name):
        self.name = name
        self.window = None
        print(f'Object {self.__class__} is creating')
        pyautogui.confirm(text='Window of Client cant be minimize!', title='Info', buttons=['OK'])

    def start(self):
        self.window = self.__get_window()
        # self.login()
        self.window[0].activate()
        time.sleep(0.1)
        self.window[0].moveTo(0, 0)
        counter_main = 1
        while True:
            # while True:
            #     print(pydirectinput.position())
            #     time.sleep(0.3)
            open_main_inventory()
            i = 1
            # while i <= 5:
            #     use_main_inventory_slots(i)
            #     i += 1
            for slots in sys.argv:
                if slots == sys.argv[0]:
                    continue
                use_main_inventory_slots(int(slots))

            terminate_spot()
            change_chanel(counter_main)
            print("Finish everything")
            counter_main += 1
            if counter_main == 5:
                counter_main = 1

    def __get_window(self):
        while True:
            hwnd = pyautogui.getWindowsWithTitle(self.name)

            if len(hwnd) <= 0:
                return None

            if len(hwnd) >= 2:
                print(f'Number of finding windows is {len(hwnd)}')
                window_to_remove = pyautogui.getWindowsWithTitle("InsomniaMT2 Klient")
                window_to_remove[0].maximize()
                decison = pyautogui.confirm(text='Remove this window?', title='Remove', buttons=['OK', 'Cancel'])
                if decison == 'Cancel':
                    return None

                if decison == 'OK':
                    window_to_remove[0].close()
                    time.sleep(0.5)

            if len(hwnd) == 1:
                hwnd[0].activate()
                return hwnd

    def login(self):
        print("Login")
        self.window[0].activate()
        time.sleep(0.1)
        self.window[0].moveTo(0, 0)
        time.sleep(0.1)
        pydirectinput.leftClick(874, 640)
        time.sleep(10)
        pydirectinput.leftClick(215, 648)
        time.sleep(10)


if __name__ == "__main__":
    Auto = AutoClicker("InsomniaMT2")
    Auto.start()

