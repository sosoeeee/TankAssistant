# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculating_Window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calculate_Window(object):
    def setupUi(self, Calculate_Window):
        Calculate_Window.setObjectName("Calculate_Window")
        Calculate_Window.setEnabled(True)
        Calculate_Window.resize(558, 399)
        Calculate_Window.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(Calculate_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 441, 71))
        self.label.setStyleSheet("font: 87 28pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(266, 90, 20, 171))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 80, 491, 251))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 270, 471, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.collect = QtWidgets.QPushButton(self.layoutWidget)
        self.collect.setObjectName("collect")
        self.horizontalLayout.addWidget(self.collect)
        self.predict = QtWidgets.QPushButton(self.layoutWidget)
        self.predict.setObjectName("predict")
        self.horizontalLayout.addWidget(self.predict)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 90, 221, 171))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.point_label_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.point_label_1.setStyleSheet("font: 14pt \"Adobe Heiti Std\";")
        self.point_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.point_label_1.setObjectName("point_label_1")
        self.verticalLayout.addWidget(self.point_label_1)
        self.point_label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.point_label_2.setStyleSheet("font: 14pt \"Adobe Heiti Std\";")
        self.point_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.point_label_2.setObjectName("point_label_2")
        self.verticalLayout.addWidget(self.point_label_2)
        self.point_label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.point_label_3.setStyleSheet("font: 14pt \"Adobe Heiti Std\";")
        self.point_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.point_label_3.setObjectName("point_label_3")
        self.verticalLayout.addWidget(self.point_label_3)
        self.wind_power_label = QtWidgets.QLabel(self.layoutWidget1)
        self.wind_power_label.setStyleSheet("font: 14pt \"Adobe Heiti Std\";")
        self.wind_power_label.setAlignment(QtCore.Qt.AlignCenter)
        self.wind_power_label.setObjectName("wind_power_label")
        self.verticalLayout.addWidget(self.wind_power_label)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.point_1 = QtWidgets.QLabel(self.layoutWidget1)
        self.point_1.setStyleSheet("font: 10pt \"Adobe Heiti Std\";")
        self.point_1.setObjectName("point_1")
        self.verticalLayout_2.addWidget(self.point_1)
        self.point_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.point_2.setStyleSheet("font: 10pt \"Adobe Heiti Std\";")
        self.point_2.setObjectName("point_2")
        self.verticalLayout_2.addWidget(self.point_2)
        self.point_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.point_3.setStyleSheet("font: 14pt \"Adobe Heiti Std\";\n"
"font: 10pt \"Adobe Heiti Std\";")
        self.point_3.setObjectName("point_3")
        self.verticalLayout_2.addWidget(self.point_3)
        self.windPower = QtWidgets.QLabel(self.layoutWidget1)
        self.windPower.setStyleSheet("font: 14pt \"Adobe Heiti Std\";")
        self.windPower.setAlignment(QtCore.Qt.AlignCenter)
        self.windPower.setObjectName("windPower")
        self.verticalLayout_2.addWidget(self.windPower)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(290, 90, 221, 171))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setStyleSheet("font: 14pt \"Adobe Heiti Std\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.angle = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.angle.setObjectName("angle")
        self.gridLayout_2.addWidget(self.angle, 1, 1, 1, 1)
        self.power = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.power.setObjectName("power")
        self.gridLayout_2.addWidget(self.power, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setStyleSheet("font: 14pt \"Adobe Heiti Std\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.hint = QtWidgets.QLabel(self.layoutWidget2)
        self.hint.setMinimumSize(QtCore.QSize(211, 80))
        self.hint.setStyleSheet("font: 14pt \"Adobe Heiti Std\";\n"
"font: 9pt \"Adobe Heiti Std\";")
        self.hint.setFrameShape(QtWidgets.QFrame.Panel)
        self.hint.setAlignment(QtCore.Qt.AlignCenter)
        self.hint.setObjectName("hint")
        self.gridLayout_3.addWidget(self.hint, 1, 0, 1, 1)
        Calculate_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculate_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Calculate_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculate_Window)
        self.statusbar.setObjectName("statusbar")
        Calculate_Window.setStatusBar(self.statusbar)
        self.actionComputing = QtWidgets.QAction(Calculate_Window)
        self.actionComputing.setObjectName("actionComputing")
        self.action_Collecting = QtWidgets.QAction(Calculate_Window)
        self.action_Collecting.setObjectName("action_Collecting")
        self.menu.addAction(self.actionComputing)
        self.menu.addAction(self.action_Collecting)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(Calculate_Window)
        QtCore.QMetaObject.connectSlotsByName(Calculate_Window)

    def retranslateUi(self, Calculate_Window):
        _translate = QtCore.QCoreApplication.translate
        Calculate_Window.setWindowTitle(_translate("Calculate_Window", "Calculating"))
        self.label.setText(_translate("Calculate_Window", "Tank Assistant"))
        self.collect.setText(_translate("Calculate_Window", "Collect"))
        self.predict.setText(_translate("Calculate_Window", "Predict"))
        self.point_label_1.setText(_translate("Calculate_Window", "Point_1"))
        self.point_label_2.setText(_translate("Calculate_Window", "Point_2"))
        self.point_label_3.setText(_translate("Calculate_Window", "Point_3"))
        self.wind_power_label.setText(_translate("Calculate_Window", "Wind Power"))
        self.point_1.setText(_translate("Calculate_Window", "X:      Y:"))
        self.point_2.setText(_translate("Calculate_Window", "X:      Y:"))
        self.point_3.setText(_translate("Calculate_Window", "X:      Y:"))
        self.windPower.setText(_translate("Calculate_Window", "WP"))
        self.label_10.setText(_translate("Calculate_Window", "POWER"))
        self.label_11.setText(_translate("Calculate_Window", "ANGLE"))
        self.hint.setText(_translate("Calculate_Window", "[HINT]"))
        self.menu.setTitle(_translate("Calculate_Window", "model"))
        self.actionComputing.setText(_translate("Calculate_Window", "Calculating"))
        self.action_Collecting.setText(_translate("Calculate_Window", " Collecting"))

