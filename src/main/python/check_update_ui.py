# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../ui/check_update.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(420, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(420, 130))
        MainWindow.setMaximumSize(QtCore.QSize(420, 130))
        MainWindow.setWindowTitle("")
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(90, 20, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(90, 50, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.ok_button_update = QtWidgets.QPushButton(self.centralwidget)
        self.ok_button_update.setGeometry(QtCore.QRect(312, 80, 91, 32))
        self.ok_button_update.setAutoDefault(True)
        self.ok_button_update.setDefault(True)
        self.ok_button_update.setObjectName("ok_button_update")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actiondsd = QtWidgets.QAction(MainWindow)
        self.actiondsd.setObjectName("actiondsd")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label1.setText(_translate("MainWindow", "TextLabel"))
        self.label2.setText(_translate("MainWindow", "TextLabel"))
        self.ok_button_update.setText(_translate("MainWindow", "OK"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actiondsd.setText(_translate("MainWindow", "dsd"))

