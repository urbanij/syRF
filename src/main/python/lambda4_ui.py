# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../ui/lambda4.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(317, 309)
        MainWindow.setWindowTitle("λ/4")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.z1_box = QtWidgets.QLineEdit(self.centralwidget)
        self.z1_box.setObjectName("z1_box")
        self.gridLayout_18.addWidget(self.z1_box, 1, 1, 1, 1)
        self.z2_box = QtWidgets.QLineEdit(self.centralwidget)
        self.z2_box.setObjectName("z2_box")
        self.gridLayout_18.addWidget(self.z2_box, 2, 1, 1, 1)
        self.label_122 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_122.sizePolicy().hasHeightForWidth())
        self.label_122.setSizePolicy(sizePolicy)
        self.label_122.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_122.setObjectName("label_122")
        self.gridLayout_18.addWidget(self.label_122, 0, 2, 1, 1)
        self.Z0_box2_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Z0_box2_2.setInputMask("")
        self.Z0_box2_2.setObjectName("Z0_box2_2")
        self.gridLayout_18.addWidget(self.Z0_box2_2, 0, 1, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_77.setObjectName("label_77")
        self.gridLayout_18.addWidget(self.label_77, 2, 0, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy)
        self.label_82.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_82.setObjectName("label_82")
        self.gridLayout_18.addWidget(self.label_82, 1, 0, 1, 1)
        self.label_105 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_105.sizePolicy().hasHeightForWidth())
        self.label_105.setSizePolicy(sizePolicy)
        self.label_105.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_105.setObjectName("label_105")
        self.gridLayout_18.addWidget(self.label_105, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_18)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_123 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy)
        self.label_123.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_123.setObjectName("label_123")
        self.gridLayout.addWidget(self.label_123, 1, 3, 1, 1)
        self.Zbox111 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Zbox111.setMaximumSize(QtCore.QSize(16777215, 21))
        self.Zbox111.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Zbox111.setObjectName("Zbox111")
        self.gridLayout.addWidget(self.Zbox111, 1, 1, 1, 2)
        self.label_124 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_124.sizePolicy().hasHeightForWidth())
        self.label_124.setSizePolicy(sizePolicy)
        self.label_124.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_124.setObjectName("label_124")
        self.gridLayout.addWidget(self.label_124, 1, 0, 1, 1)
        self.Calculate_lambda4 = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate_lambda4.setDefault(True)
        self.Calculate_lambda4.setObjectName("Calculate_lambda4")
        self.gridLayout.addWidget(self.Calculate_lambda4, 2, 2, 1, 1)
        self.clean_lambda4_button = QtWidgets.QPushButton(self.centralwidget)
        self.clean_lambda4_button.setObjectName("clean_lambda4_button")
        self.gridLayout.addWidget(self.clean_lambda4_button, 2, 1, 1, 1)
        self.zbox111 = QtWidgets.QTextBrowser(self.centralwidget)
        self.zbox111.setMaximumSize(QtCore.QSize(16777215, 21))
        self.zbox111.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.zbox111.setObjectName("zbox111")
        self.gridLayout.addWidget(self.zbox111, 0, 1, 1, 2)
        self.label_125 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_125.sizePolicy().hasHeightForWidth())
        self.label_125.setSizePolicy(sizePolicy)
        self.label_125.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_125.setObjectName("label_125")
        self.gridLayout.addWidget(self.label_125, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actiondsd = QtWidgets.QAction(MainWindow)
        self.actiondsd.setObjectName("actiondsd")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_122.setText(_translate("MainWindow", "<html><head/><body><p>Ω</p></body></html>"))
        self.Z0_box2_2.setText(_translate("MainWindow", "50"))
        self.label_77.setText(_translate("MainWindow", "<html><head/><body><p>Output (z<span style=\" vertical-align:sub;\">L</span>\')</p></body></html>"))
        self.label_82.setText(_translate("MainWindow", "<html><head/><body><p>Input (z<span style=\" vertical-align:sub;\">L</span>)</p></body></html>"))
        self.label_105.setText(_translate("MainWindow", "<html><head/><body><p>Z<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.label_123.setText(_translate("MainWindow", "<html><head/><body><p>Ω</p></body></html>"))
        self.label_124.setText(_translate("MainWindow", "<html><head/><body><p>Z</p></body></html>"))
        self.Calculate_lambda4.setText(_translate("MainWindow", "Calculate"))
        self.clean_lambda4_button.setText(_translate("MainWindow", "Clean All"))
        self.label_125.setText(_translate("MainWindow", "<html><head/><body><p>z</p></body></html>"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actiondsd.setText(_translate("MainWindow", "dsd"))

