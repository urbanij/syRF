#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Feb 20 17:23:29 CET 2019

@author(s)   : Francesco Urbani
@file        : integrated_matching.py
@descritpion : 

"""

from PyQt5.QtWidgets import (
    QMainWindow,
    QAction,
    QStatusBar,
    QToolBar,
    QMenuBar,
    QMessageBox,
)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets

from pyui.check_update_ui import Ui_MainWindow  # main ui window autogenerated by PyQt

import check_update


TEXT1 = "<b>You’re up-to-date!</b>"


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        flags = (
            QtCore.Qt.Window
            | QtCore.Qt.CustomizeWindowHint
            | QtCore.Qt.WindowTitleHint
            | QtCore.Qt.WindowStaysOnTopHint
        )

        self.setWindowFlags(flags)

        self.ok_button_update.clicked.connect(self.close)

        self.label1.setText(TEXT1)
        self.label2.setText(
            "syRF {} is currently the newest version available.".format(
                check_update.get_version()
            )
        )


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())
