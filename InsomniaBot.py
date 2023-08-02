import asyncio
import logging
import sys
import time

import pyautogui
import pydirectinput
import qasync
from PySide6 import QtWidgets, QtCore
from front import Ui_MainWindow


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


def logout():
    print("Logout")
    time.sleep(0.1)
    pydirectinput.leftClick(1264, 967)
    time.sleep(1)
    pydirectinput.leftClick(655, 573)


@qasync.asyncSlot()
async def terminate_spot(time_attack):
    pydirectinput.keyDown('1')
    await asyncio.sleep(0.1)
    pydirectinput.keyUp('1')
    await asyncio.sleep(0.1)
    pydirectinput.keyDown('space')
    await asyncio.sleep(time_attack)
    pydirectinput.keyUp('space')
    pydirectinput.keyDown('z')
    await asyncio.sleep(0.1)
    pydirectinput.keyUp('z')


@qasync.asyncSlot()
async def change_chanel(chanel, time_change):

    if chanel < 0 or chanel > 4:
        print(f'Chanel cant be {chanel}')
        return

    get_window("Insomnia Helper", False)
    get_window('InsomniaMT2', True)
    print(f'Chanel is changing to chanel {chanel}')

    if chanel == 1:
        await asyncio.sleep(0.1)
        pydirectinput.leftClick(1156, 81)
        await asyncio.sleep(time_change)
        return

    if chanel == 2:
        await asyncio.sleep(0.1)
        pydirectinput.leftClick(1154, 102)
        await asyncio.sleep(time_change)
        return

    if chanel == 3:
        await asyncio.sleep(0.1)
        pydirectinput.leftClick(1160, 127)
        await asyncio.sleep(time_change)
        return

    if chanel == 4:
        await asyncio.sleep(0.1)
        pydirectinput.leftClick(1174, 147)
        await asyncio.sleep(time_change)
        return


def use_main_inventory_slots(number):
    if number < 1 or number > 5:
        return False

    print(f'Use slot {number} of main inventory')

    if number == 1:
        time.sleep(0.1)
        pydirectinput.leftClick(1137, 645)
        return True

    if number == 2:
        time.sleep(0.1)
        pydirectinput.leftClick(1168, 645)
        return True

    if number == 3:
        time.sleep(0.1)
        pydirectinput.leftClick(1200, 645)
        return True

    if number == 4:
        time.sleep(0.1)
        pydirectinput.leftClick(1234, 645)
        return True

    if number == 5:
        time.sleep(0.1)
        pydirectinput.leftClick(1264, 645)
        return True


def open_main_inventory():
    print("Opening main inventory")
    time.sleep(0.1)
    pydirectinput.leftClick(1192, 970)


def get_window(title, client):
    while True:
        hwnd = pyautogui.getWindowsWithTitle(title)

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
                time.sleep(0.1)

        if len(hwnd) == 1:
            hwnd[0].activate()
            if client:
                hwnd[0].moveTo(0, 0)
            else:
                hwnd[0].moveTo(1280, 0)
            return hwnd


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Insomnia Helper")
        self.stackedWidget.setCurrentIndex(0)

        # Variable
        self.can_running = False
        self.counter_chanel = 1

        # Connect push button
        self.autoDropping.clicked.connect(self.auto_dropping)
        self.bossHelpper.clicked.connect(self.boss_helper)
        self.back_button.clicked.connect(self.back_start_page)
        self.back_button_1.clicked.connect(self.back_start_page)
        self.start_dropping.clicked.connect(self.start_dropping_fun)

    def auto_dropping(self):
        self.stackedWidget.setCurrentIndex(1)

    def boss_helper(self):
        self.stackedWidget.setCurrentIndex(2)

    def back_start_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def start_dropping_fun(self):
        print("button clicked")
        self.can_running = not self.can_running

        if self.can_running:
            self.main()

    def keyPressEvent(self, event):
        key = event.key()

        # if key == 61:
        #     self.can_running = True
        #     print("Key started is clicked")
        #     self.main()
        #     return
        #
        # if key == 45:
        #     print("Key stopped is clicked")
        #     self.can_running = False
        #     return

        print(f"Found key {key} --> dont have action for this key")

    @qasync.asyncSlot()
    async def main(self):
        print("Dropping is started")
        try:
            while True:
                print(self.can_running)
                if not self.can_running:
                    print("Dropping is stopped")
                    break
                await self.auto_dropping_fun()
        except:
            print("Error with dropping, try again")

    @qasync.asyncSlot()
    async def auto_dropping_fun(self):

        if not self.ch1_check_box.isChecked() and self.counter_chanel == 1:
            self.counter_chanel += 1

        if not self.ch2_check_box.isChecked() and self.counter_chanel == 2:
            self.counter_chanel += 1

        if not self.ch3_check_box.isChecked() and self.counter_chanel == 3:
            self.counter_chanel += 1

        if not self.ch4_check_box.isChecked() and self.counter_chanel == 4:
            self.counter_chanel += 1

        if self.counter_chanel > 4:
            self.counter_chanel = 1
            await asyncio.sleep(0.1)
            return

        await terminate_spot(self.atact_time.value())
        await change_chanel(self.counter_chanel, self.change_chanel_time.value())
        self.counter_chanel += 1


def start_application():  # Start Application with qasync
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    logging.info("Starting application Insomnia bot ...")
    with loop:
        loop.run_forever()


start_application()
