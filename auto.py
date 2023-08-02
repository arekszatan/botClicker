import sys
import time
import pyautogui
import pydirectinput





class AutoClicker:
    def __init__(self, name):
        self.name = name
        self.window = None
        print(f'Object {self.__class__} is creating')
        pyautogui.confirm(text='Window of Client cant be minimize!', title='Info', buttons=['OK'])

    def start(self):
        self.window = self.__get_window()
        counter_main = 0
        while True:
            self.login()
            use_quick_access_inventory()
            open_main_inventory()
            if counter_main % 6 == 0:
                for slots in sys.argv:
                    if slots == sys.argv[0]:
                        continue
                    use_main_inventory_slots(int(slots))
            logout()
            counter = 0
            print("Finish everything")
            counter_main += 1
            while counter < 31:
                time.sleep(60)
                counter += 1
                print(f'Time for next action is {31 - counter}')



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

