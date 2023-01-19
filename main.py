import sys
import win32api
import time
from parse import parse
import win32con
import win32gui
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Calculating_Window import Ui_Calculate_Window
from Collect_Window import Ui_Collect_Window
from utils import *


class CalculateWindow(QMainWindow, Ui_Calculate_Window):
    def __init__(self):
        super(CalculateWindow, self).__init__()
        self.setupUi(self)
        self.iniText()

    def iniText(self):
        self.hint.setText('')
        self.point_1.setText('')
        self.point_2.setText('')
        self.point_3.setText('')
        self.windPower.setText('')


class CollectWindow(QMainWindow, Ui_Collect_Window):
    def __init__(self):
        super(CollectWindow, self).__init__()
        self.setupUi(self)
        self.iniText()

    def iniText(self):
        self.hint.setText('')
        self.point_1.setText('')
        self.point_2.setText('')
        self.point_3.setText('')
        self.windPower.setText('')


class Thread(QThread):
    sinout = pyqtSignal(int)

    def __init__(self, threadFuc, para):
        super(Thread, self).__init__()
        self.threadFuc = threadFuc
        self.para = para

    def run(self):
        # 需要执行的内容
        result = self.threadFuc(self.para)
        # 发出信号
        self.sinout.emit(result)


class WindowCtl:
    def __init__(self):
        self.threadRuning = False
        self.calculateWindow = CalculateWindow()
        self.collectWindow = CollectWindow()
        self.iniSlots()

    def iniWindow(self):
        self.calculateWindow.show()
        self.collectWindow.hide()

    def iniSlots(self):
        self.calculateWindow.collect.clicked.connect(lambda: self.startCollect(window=0))
        self.calculateWindow.actionComputing.triggered.connect(self.calculateMode)
        self.calculateWindow.action_Collecting.triggered.connect(self.collectMode)

        self.collectWindow.collect.clicked.connect(lambda: self.startCollect(window=1))
        self.collectWindow.store.clicked.connect(self.storeImf)
        self.collectWindow.actionCollecting.triggered.connect(self.collectMode)
        self.collectWindow.actionCalculating.triggered.connect(self.calculateMode)

    def calculateMode(self):
        self.collectWindow.hide()
        self.calculateWindow.show()

    def collectMode(self):
        self.calculateWindow.hide()
        self.collectWindow.show()

    def startCollect(self, window):
        if self.threadRuning is False:
            self.calculateWindow.timeThread = Thread(self.collectImf, window)
            # self.calculateWindow.timeThread.sinout.connect(self.collectComplete)  # 设置线程结束函数
            self.calculateWindow.timeThread.start()  # 开启线程

    def collectImf(self, window):
        print('成功进入线程')
        self.threadRuning = True

        # 查找指定窗口
        # window_title = 'ShellShock Live'
        window_title = 'test.txt - 记事本'
        hwnd = findTitle(window_title)
        # print(hwnd)
        if hwnd != -1:
            # win32gui.BringWindowToTop(hwnd)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 1280, 1024, win32con.SWP_SHOWWINDOW)
            hwnd = findTitle(window_title)
            x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
            if window:
                self.collectWindow.hint.setText('找到窗口，3s后开始收集坐标')
            else:
                self.calculateWindow.hint.setText('找到窗口，3s后开始收集坐标')
        else:
            if window:
                self.collectWindow.hint.setText('未找到游戏窗口')
            else:
                self.calculateWindow.hint.setText('未找到游戏窗口')
            self.threadRuning = False
            return 0

        loc = [0.45, 0.06]
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(hwnd, x=int(x1 + (x2 - x1) * loc[0]), y=int(y1 + (y2 - y1) * loc[1]), width=107,
                                height=45).toImage()
        # img = screen.grabWindow(hwnd).toImage()
        img.save('test.jpg')
        if window:
            self.collectWindow.windPower.setText(str(getWindPower()))
        else:
            self.calculateWindow.windPower.setText(str(getWindPower()))


        self.threadRuning = False

        curPoint = 1
        while 1:
            print(curPoint)
            time.sleep(3)
            p = win32api.GetCursorPos()
            if x1 <= p[0] <= x2 and y1 <= p[1] <= y2:
                if curPoint == 1:
                    if window:
                        self.collectWindow.point_1.setText(
                            '(%.2f, %.2f)' % (
                                round(float(p[0] - x1) / (x2 - x1), 3), round(float(p[1] - y1) / (y2 - y1), 3)))
                        self.collectWindow.hint.setText('成功收集第%d个坐标\n3s后收集下一个' % curPoint)
                    else:
                        self.calculateWindow.point_1.setText(
                            '(%.2f, %.2f)' % (
                                round(float(p[0] - x1) / (x2 - x1), 3), round(float(p[1] - y1) / (y2 - y1), 3)))
                        self.calculateWindow.hint.setText('成功收集第%d个坐标\n3s后收集下一个' % curPoint)
                    curPoint = curPoint + 1
                elif curPoint == 2:
                    if window:
                        self.collectWindow.point_2.setText(
                            '(%.2f, %.2f)' % (
                                round(float(p[0] - x1) / (x2 - x1), 3), round(float(p[1] - y1) / (y2 - y1), 3)))
                        self.collectWindow.hint.setText('成功收集第%d个坐标\n3s后收集下一个' % curPoint)
                    else:
                        self.calculateWindow.point_2.setText(
                            '(%.2f, %.2f)' % (
                                round(float(p[0] - x1) / (x2 - x1), 3), round(float(p[1] - y1) / (y2 - y1), 3)))
                        self.calculateWindow.hint.setText('成功收集第%d个坐标\n3s后收集下一个' % curPoint)
                    curPoint = curPoint + 1
                else:
                    if window:
                        self.collectWindow.point_3.setText(
                            '(%.2f, %.2f)' % (
                                round(float(p[0] - x1) / (x2 - x1), 3), round(float(p[1] - y1) / (y2 - y1), 3)))
                        self.collectWindow.hint.setText('成功收集所有坐标')
                    else:
                        self.calculateWindow.point_3.setText(
                            '(%.2f, %.2f)' % (
                                round(float(p[0] - x1) / (x2 - x1), 3), round(float(p[1] - y1) / (y2 - y1), 3)))
                        self.calculateWindow.hint.setText('成功收集所有坐标')
                    self.threadRuning = False
                    break
            else:
                if window:
                    self.collectWindow.hint.setText('鼠标不在游戏窗口内')
                else:
                    self.calculateWindow.hint.setText('鼠标不在游戏窗口内')

    def storeImf(self):
        dataList = []
        strPoint = self.collectWindow.point_1.text()
        point = parse('({}, {})', strPoint)
        x = float(point[0])
        y = float(point[1])
        dataList.append(x)
        dataList.append(y)

        strPoint = self.collectWindow.point_2.text()
        point = parse('({}, {})', strPoint)
        x = float(point[0])
        y = float(point[1])
        dataList.append(x)
        dataList.append(y)

        strPoint = self.collectWindow.point_3.text()
        point = parse('({}, {})', strPoint)
        x = float(point[0])
        y = float(point[1])
        dataList.append(x)
        dataList.append(y)

        strWP = self.collectWindow.windPower.text()
        dataList.append(int(strWP))

        strPower = self.collectWindow.powerEdit.text()
        dataList.append(int(strPower))
        strAngle = self.collectWindow.angleEdit.text()
        dataList.append(int(strAngle))

        df = pd.DataFrame(dataList).T
        df.to_csv('data.csv', mode='a', index=False, header=False, sep=',')
        print(dataList)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ctl = WindowCtl()
    ctl.iniWindow()
    sys.exit(app.exec_())
