# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../ui/smith_chart.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 526)
        MainWindow.setWindowTitle("Smith Chart")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.label_103 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_103.sizePolicy().hasHeightForWidth())
        self.label_103.setSizePolicy(sizePolicy)
        self.label_103.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_103.setObjectName("label_103")
        self.horizontalLayout_8.addWidget(self.label_103)
        self.Z0_box2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.Z0_box2.setInputMask("")
        self.Z0_box2.setObjectName("Z0_box2")
        self.horizontalLayout_8.addWidget(self.Z0_box2)
        self.label_104 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_104.sizePolicy().hasHeightForWidth())
        self.label_104.setSizePolicy(sizePolicy)
        self.label_104.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_104.setObjectName("label_104")
        self.horizontalLayout_8.addWidget(self.label_104)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_17.addLayout(self.horizontalLayout_8)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_17.addItem(spacerItem2)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.line_8 = QtWidgets.QFrame(self.groupBox_6)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_10.addWidget(self.line_8, 0, 3, 3, 1)
        self.Z_in_box = QtWidgets.QLineEdit(self.groupBox_6)
        self.Z_in_box.setObjectName("Z_in_box")
        self.gridLayout_10.addWidget(self.Z_in_box, 1, 1, 1, 1)
        self.label_268 = QtWidgets.QLabel(self.groupBox_6)
        self.label_268.setEnabled(False)
        self.label_268.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_268.setObjectName("label_268")
        self.gridLayout_10.addWidget(self.label_268, 2, 6, 1, 1)
        self.label_269 = QtWidgets.QLabel(self.groupBox_6)
        self.label_269.setEnabled(False)
        self.label_269.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_269.setObjectName("label_269")
        self.gridLayout_10.addWidget(self.label_269, 2, 4, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_76.setObjectName("label_76")
        self.gridLayout_10.addWidget(self.label_76, 1, 0, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_91.sizePolicy().hasHeightForWidth())
        self.label_91.setSizePolicy(sizePolicy)
        self.label_91.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_91.setObjectName("label_91")
        self.gridLayout_10.addWidget(self.label_91, 1, 2, 1, 1)
        self.Z_out_box = QtWidgets.QLineEdit(self.groupBox_6)
        self.Z_out_box.setObjectName("Z_out_box")
        self.gridLayout_10.addWidget(self.Z_out_box, 2, 1, 1, 1)
        self.label_92 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_92.sizePolicy().hasHeightForWidth())
        self.label_92.setSizePolicy(sizePolicy)
        self.label_92.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_92.setObjectName("label_92")
        self.gridLayout_10.addWidget(self.label_92, 2, 2, 1, 1)
        self.ZS_box_8 = QtWidgets.QLineEdit(self.groupBox_6)
        self.ZS_box_8.setEnabled(False)
        self.ZS_box_8.setObjectName("ZS_box_8")
        self.gridLayout_10.addWidget(self.ZS_box_8, 2, 7, 1, 1)
        self.label_267 = QtWidgets.QLabel(self.groupBox_6)
        self.label_267.setEnabled(False)
        self.label_267.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_267.setObjectName("label_267")
        self.gridLayout_10.addWidget(self.label_267, 1, 4, 1, 1)
        self.label_266 = QtWidgets.QLabel(self.groupBox_6)
        self.label_266.setEnabled(False)
        self.label_266.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_266.setObjectName("label_266")
        self.gridLayout_10.addWidget(self.label_266, 1, 6, 1, 1)
        self.ZS_box_6 = QtWidgets.QLineEdit(self.groupBox_6)
        self.ZS_box_6.setEnabled(False)
        self.ZS_box_6.setObjectName("ZS_box_6")
        self.gridLayout_10.addWidget(self.ZS_box_6, 1, 7, 1, 1)
        self.ZS_box_9 = QtWidgets.QLineEdit(self.groupBox_6)
        self.ZS_box_9.setEnabled(False)
        self.ZS_box_9.setObjectName("ZS_box_9")
        self.gridLayout_10.addWidget(self.ZS_box_9, 1, 5, 1, 1)
        self.ZS_box_7 = QtWidgets.QLineEdit(self.groupBox_6)
        self.ZS_box_7.setEnabled(False)
        self.ZS_box_7.setObjectName("ZS_box_7")
        self.gridLayout_10.addWidget(self.ZS_box_7, 2, 5, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_75.setObjectName("label_75")
        self.gridLayout_10.addWidget(self.label_75, 2, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_10.addWidget(self.radioButton_2, 0, 5, 1, 3)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_10.addWidget(self.radioButton, 0, 1, 1, 2)
        self.verticalLayout_17.addLayout(self.gridLayout_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_17)
        self.verticalLayout_18.addWidget(self.groupBox_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_18.addItem(spacerItem3)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_99 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_99.sizePolicy().hasHeightForWidth())
        self.label_99.setSizePolicy(sizePolicy)
        self.label_99.setMaximumSize(QtCore.QSize(16777215, 21))
        self.label_99.setAlignment(QtCore.Qt.AlignCenter)
        self.label_99.setObjectName("label_99")
        self.gridLayout_11.addWidget(self.label_99, 0, 1, 1, 1)
        self.label_100 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_100.sizePolicy().hasHeightForWidth())
        self.label_100.setSizePolicy(sizePolicy)
        self.label_100.setMaximumSize(QtCore.QSize(16777215, 21))
        self.label_100.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100.setObjectName("label_100")
        self.gridLayout_11.addWidget(self.label_100, 0, 2, 1, 1)
        self.label_94 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_94.sizePolicy().hasHeightForWidth())
        self.label_94.setSizePolicy(sizePolicy)
        self.label_94.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_94.setObjectName("label_94")
        self.gridLayout_11.addWidget(self.label_94, 1, 0, 1, 1)
        self.z_in_box_2 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_in_box_2.sizePolicy().hasHeightForWidth())
        self.z_in_box_2.setSizePolicy(sizePolicy)
        self.z_in_box_2.setMaximumSize(QtCore.QSize(16777215, 21))
        self.z_in_box_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.z_in_box_2.setObjectName("z_in_box_2")
        self.gridLayout_11.addWidget(self.z_in_box_2, 1, 1, 1, 1)
        self.z_in_box_5 = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_in_box_5.sizePolicy().hasHeightForWidth())
        self.z_in_box_5.setSizePolicy(sizePolicy)
        self.z_in_box_5.setMaximumSize(QtCore.QSize(16777215, 21))
        self.z_in_box_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.z_in_box_5.setObjectName("z_in_box_5")
        self.gridLayout_11.addWidget(self.z_in_box_5, 1, 2, 1, 1)
        self.label_93 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_93.sizePolicy().hasHeightForWidth())
        self.label_93.setSizePolicy(sizePolicy)
        self.label_93.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_93.setObjectName("label_93")
        self.gridLayout_11.addWidget(self.label_93, 2, 0, 1, 1)
        self.z_in_box = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_in_box.sizePolicy().hasHeightForWidth())
        self.z_in_box.setSizePolicy(sizePolicy)
        self.z_in_box.setMaximumSize(QtCore.QSize(16777215, 21))
        self.z_in_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.z_in_box.setObjectName("z_in_box")
        self.gridLayout_11.addWidget(self.z_in_box, 2, 1, 1, 1)
        self.z_out_box = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.z_out_box.sizePolicy().hasHeightForWidth())
        self.z_out_box.setSizePolicy(sizePolicy)
        self.z_out_box.setMaximumSize(QtCore.QSize(16777215, 21))
        self.z_out_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.z_out_box.setObjectName("z_out_box")
        self.gridLayout_11.addWidget(self.z_out_box, 2, 2, 1, 1)
        self.label_96 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_96.sizePolicy().hasHeightForWidth())
        self.label_96.setSizePolicy(sizePolicy)
        self.label_96.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_96.setObjectName("label_96")
        self.gridLayout_11.addWidget(self.label_96, 3, 0, 1, 1)
        self.gamma_zin_box = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamma_zin_box.sizePolicy().hasHeightForWidth())
        self.gamma_zin_box.setSizePolicy(sizePolicy)
        self.gamma_zin_box.setMaximumSize(QtCore.QSize(16777215, 21))
        self.gamma_zin_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gamma_zin_box.setObjectName("gamma_zin_box")
        self.gridLayout_11.addWidget(self.gamma_zin_box, 3, 1, 1, 1)
        self.gamma_zout_box = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gamma_zout_box.sizePolicy().hasHeightForWidth())
        self.gamma_zout_box.setSizePolicy(sizePolicy)
        self.gamma_zout_box.setMaximumSize(QtCore.QSize(16777215, 21))
        self.gamma_zout_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.gamma_zout_box.setObjectName("gamma_zout_box")
        self.gridLayout_11.addWidget(self.gamma_zout_box, 3, 2, 1, 1)
        self.label_97 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_97.sizePolicy().hasHeightForWidth())
        self.label_97.setSizePolicy(sizePolicy)
        self.label_97.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_97.setObjectName("label_97")
        self.gridLayout_11.addWidget(self.label_97, 4, 0, 1, 1)
        self.lambda_tick_zin_box = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lambda_tick_zin_box.sizePolicy().hasHeightForWidth())
        self.lambda_tick_zin_box.setSizePolicy(sizePolicy)
        self.lambda_tick_zin_box.setMaximumSize(QtCore.QSize(16777215, 21))
        self.lambda_tick_zin_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lambda_tick_zin_box.setObjectName("lambda_tick_zin_box")
        self.gridLayout_11.addWidget(self.lambda_tick_zin_box, 4, 1, 1, 1)
        self.lambda_tick_zout_box = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lambda_tick_zout_box.sizePolicy().hasHeightForWidth())
        self.lambda_tick_zout_box.setSizePolicy(sizePolicy)
        self.lambda_tick_zout_box.setMaximumSize(QtCore.QSize(16777215, 21))
        self.lambda_tick_zout_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lambda_tick_zout_box.setObjectName("lambda_tick_zout_box")
        self.gridLayout_11.addWidget(self.lambda_tick_zout_box, 4, 2, 1, 1)
        self.verticalLayout_18.addLayout(self.gridLayout_11)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_18.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.Show_Smith = QtWidgets.QPushButton(self.centralwidget)
        self.Show_Smith.setObjectName("Show_Smith")
        self.horizontalLayout_5.addWidget(self.Show_Smith)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.clean_all_button213 = QtWidgets.QPushButton(self.centralwidget)
        self.clean_all_button213.setObjectName("clean_all_button213")
        self.horizontalLayout_5.addWidget(self.clean_all_button213)
        self.Calculate_quarter = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate_quarter.setDefault(True)
        self.Calculate_quarter.setObjectName("Calculate_quarter")
        self.horizontalLayout_5.addWidget(self.Calculate_quarter)
        self.verticalLayout_18.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_18, 0, 0, 1, 1)
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
        MainWindow.setTabOrder(self.Z_in_box, self.Z_out_box)
        MainWindow.setTabOrder(self.Z_out_box, self.ZS_box_9)
        MainWindow.setTabOrder(self.ZS_box_9, self.ZS_box_6)
        MainWindow.setTabOrder(self.ZS_box_6, self.ZS_box_7)
        MainWindow.setTabOrder(self.ZS_box_7, self.ZS_box_8)
        MainWindow.setTabOrder(self.ZS_box_8, self.Z0_box2)
        MainWindow.setTabOrder(self.Z0_box2, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.z_in_box_2)
        MainWindow.setTabOrder(self.z_in_box_2, self.z_in_box_5)
        MainWindow.setTabOrder(self.z_in_box_5, self.z_in_box)
        MainWindow.setTabOrder(self.z_in_box, self.z_out_box)
        MainWindow.setTabOrder(self.z_out_box, self.gamma_zin_box)
        MainWindow.setTabOrder(self.gamma_zin_box, self.gamma_zout_box)
        MainWindow.setTabOrder(self.gamma_zout_box, self.lambda_tick_zin_box)
        MainWindow.setTabOrder(self.lambda_tick_zin_box, self.lambda_tick_zout_box)
        MainWindow.setTabOrder(self.lambda_tick_zout_box, self.Show_Smith)
        MainWindow.setTabOrder(self.Show_Smith, self.clean_all_button213)
        MainWindow.setTabOrder(self.clean_all_button213, self.Calculate_quarter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_6.setTitle(_translate("MainWindow", "Input initial and final impedance as either Z or Γ"))
        self.label_103.setText(_translate("MainWindow", "<html><head/><body><p>Z<span style=\" vertical-align:sub;\">0</span></p></body></html>"))
        self.Z0_box2.setText(_translate("MainWindow", "50"))
        self.label_104.setText(_translate("MainWindow", "<html><head/><body><p>Ω</p></body></html>"))
        self.label_268.setText(_translate("MainWindow", "<html><head/><body><p>∠Γ(Z<span style=\" vertical-align:sub;\">L</span>\')</p></body></html>"))
        self.label_269.setText(_translate("MainWindow", "<html><head/><body><p>|Γ|(Z<span style=\" vertical-align:sub;\">L</span>\')</p></body></html>"))
        self.label_76.setText(_translate("MainWindow", "Input (Z<sub>L</sub>)"))
        self.label_91.setText(_translate("MainWindow", "<html><head/><body><p>Ω</p></body></html>"))
        self.label_92.setText(_translate("MainWindow", "<html><head/><body><p>Ω</p></body></html>"))
        self.label_267.setText(_translate("MainWindow", "<html><head/><body><p>|Γ|(Z<span style=\" vertical-align:sub;\">L</span>)</p></body></html>"))
        self.label_266.setText(_translate("MainWindow", "<html><head/><body><p>∠Γ(Z<span style=\" vertical-align:sub;\">L</span>)</p></body></html>"))
        self.label_75.setText(_translate("MainWindow", "<html><head/><body><p>Output (Z<span style=\" vertical-align:sub;\">L</span>\')</p></body></html>"))
        self.radioButton_2.setText(_translate("MainWindow", "Input as Γ"))
        self.radioButton.setText(_translate("MainWindow", "Input as Z"))
        self.label_99.setText(_translate("MainWindow", "<html><head/><body><p>Z<span style=\" vertical-align:sub;\">L</span></p></body></html>"))
        self.label_100.setText(_translate("MainWindow", "<html><head/><body><p>Z<span style=\" vertical-align:sub;\">L</span>\'</p></body></html>"))
        self.label_94.setText(_translate("MainWindow", "<html><head/><body><p>Actual impedance</p></body></html>"))
        self.label_93.setText(_translate("MainWindow", "<html><head/><body><p>Normalized impedance</p></body></html>"))
        self.label_96.setText(_translate("MainWindow", "<html><head/><body><p>Γ</p></body></html>"))
        self.label_97.setText(_translate("MainWindow", "<html><head/><body><p>corresponding λ tick</p></body></html>"))
        self.Show_Smith.setText(_translate("MainWindow", "Open Smith Chart"))
        self.clean_all_button213.setText(_translate("MainWindow", "Clean All"))
        self.Calculate_quarter.setText(_translate("MainWindow", "Calculate"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actiondsd.setText(_translate("MainWindow", "dsd"))

