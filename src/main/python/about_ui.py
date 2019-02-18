# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../ui/about.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(277, 250)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowTitle("About syRF")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_description = QtWidgets.QLabel(self.centralwidget)
        self.label_description.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_description.setObjectName("label_description")
        self.gridLayout_2.addWidget(self.label_description, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_links = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_links.setFont(font)
        self.label_links.setAlignment(QtCore.Qt.AlignCenter)
        self.label_links.setObjectName("label_links")
        self.gridLayout_2.addWidget(self.label_links, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_version.setFont(font)
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName("label_version")
        self.gridLayout_2.addWidget(self.label_version, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actiondsd = QtWidgets.QAction(MainWindow)
        self.actiondsd.setObjectName("actiondsd")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_description.setText(_translate("MainWindow", "syRF bla bla bla"))
        self.label.setText(_translate("MainWindow", "syRF"))
        self.label_links.setText(_translate("MainWindow", "Hope Page"))
        self.label_version.setText(_translate("MainWindow", "version"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actiondsd.setText(_translate("MainWindow", "dsd"))

