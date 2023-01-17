import sys
import win32api
import time

import win32con
import win32gui
import xlwt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Calculating_Window import Ui_Calculate_Window
from utils import *


class CalculateWindow(QMainWindow, Ui_Calculate_Window):
    def __init__(self):
        super(CalculateWindow, self).__init__()
        self.setupUi(self)


class Thread(QThread):
    sinout = pyqtSignal(int)

    def __init__(self, threadFuc):
        super(Thread, self).__init__()
        self.threadFuc = threadFuc

    def run(self):
        # 需要执行的内容
        result = self.threadFuc()
        # 发出信号
        self.sinout.emit(result)


class WindowCtl:
    def __init__(self):
        self.threadRuning = False
        self.calculateWindow = CalculateWindow()
        self.iniSlots()

    def iniWindow(self):
        self.calculateWindow.show()
        self.calculateWindow.hint.setText('')

    def iniSlots(self):
        self.calculateWindow.collect.clicked.connect(self.startCollect)

    def startCollect(self):
        if self.threadRuning is False:
            self.calculateWindow.timeThread = Thread(self.collectImf)
            # self.calculateWindow.timeThread.sinout.connect(self.collectComplete)  # 设置线程结束函数
            self.calculateWindow.timeThread.start()  # 开启线程

    def collectImf(self):
        print('成功进入线程')
        self.threadRuning = True

        # 查找指定窗口
        window_title = 'ShellShock Live'
        # window_title = 'test.txt - 记事本'
        hwnd = findTitle(window_title)
        # print(hwnd)
        if hwnd != -1:
            # win32gui.BringWindowToTop(hwnd)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 1280, 1024, win32con.SWP_SHOWWINDOW)
            hwnd = findTitle(window_title)
            x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
            self.calculateWindow.hint.setText('找到窗口，3s后开始收集坐标')
        else:
            self.calculateWindow.hint.setText('未找到游戏窗口')
            self.threadRuning = False
            return 0

        loc = [0.45, 0.06]
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(hwnd, x=int(x1 + (x2-x1)*loc[0]), y=int(y1 + (y2-y1)*loc[1]), width=107, height=45).toImage()
        # img = screen.grabWindow(hwnd).toImage()
        img.save('test.jpg')
        self.calculateWindow.windPower.setText(str(getWindPower()))

        self.threadRuning = False

        # curPoint = 1
        # while 1:
        #     print(curPoint)
        #     time.sleep(3)
        #     p = win32api.GetCursorPos()
        #     if x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
        #         if curPoint == 1:
        #             self.calculateWindow.point_1.setText(
        #                 '(%d, %d)' % (p[0], p[1]))
        #             self.calculateWindow.hint.setText('成功收集第%d个坐标\n3s后收集下一个' % curPoint)
        #             curPoint = curPoint + 1
        #         elif curPoint == 2:
        #             self.calculateWindow.point_2.setText(
        #                 '(%d, %d)' % (p[0], p[1]))
        #             self.calculateWindow.hint.setText('成功收集第%d个坐标\n3s后收集下一个' % curPoint)
        #             curPoint = curPoint + 1
        #         else:
        #             self.calculateWindow.point_3.setText(
        #                 '(%d, %d)' % (p[0], p[1]))
        #             self.calculateWindow.hint.setText('成功收集所有坐标')
        #             self.threadRuning = False
        #             break
        #     else:
        #         self.calculateWindow.hint.setText('鼠标不在游戏窗口内')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ctl = WindowCtl()
    ctl.iniWindow()
    sys.exit(app.exec_())
