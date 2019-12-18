#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Dec 18 13:15:45 CET 2019

@author(s)   : Francesco Urbani
@file        : parallel_stub_matching.py
@descritpion :

"""

from PyQt5.QtWidgets import QMainWindow, QAction, QStatusBar, QToolBar, QMenuBar, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import math

from pyui.parallel_stub_matching_ui import Ui_MainWindow # main ui window autogenerated by PyQt


msg_error = ""
SPINBOX_STEP = 0.0001
SPINBOX_DECIMALS = 6


def parallel(z1, z2):
    return (z1*z2)/(z1+z2)



class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)


        self.Z0_lineedit.editingFinished.connect(self.Calculate_button.click)
        self.ZL_lineedit.editingFinished.connect(self.Calculate_button.click)
        self.ZL_stub_lineedit.editingFinished.connect(self.Calculate_button.click)
        self.distance_doubleSpinBox.valueChanged.connect(self.Calculate_button.click)
        self.length_doubleSpinBox.valueChanged.connect(self.Calculate_button.click)

        self.distance_horizontalScrollBar.valueChanged.connect(self.Calculate_button.click)


        self.distance_doubleSpinBox.setDecimals(SPINBOX_DECIMALS)
        self.distance_doubleSpinBox.setSingleStep(SPINBOX_STEP)
        self.distance_doubleSpinBox.setRange(0, 0.5)
        self.length_doubleSpinBox.setDecimals(SPINBOX_DECIMALS)
        self.length_doubleSpinBox.setSingleStep(SPINBOX_STEP)
        self.length_doubleSpinBox.setRange(0, 0.5)


        self.Calculate_button.clicked.connect(self.calculate_matching)

    def calculate_matching(self):

        # reading
        try:
            ZL = complex(self.ZL_lineedit.text())
        except Exception as e:
            ZL = msg_error
        
        try:
            Z0 = complex(self.Z0_lineedit.text())
        except Exception as e:
            Z0 = msg_error

        try:
            ZL_stub = complex(self.ZL_stub_lineedit.text())
        except Exception as e:
            ZL_stub = msg_error

        d = float(self.distance_horizontalScrollBar.value())*0.5/500
        print(d)
        l = float(self.length_doubleSpinBox.value())




        # computing
        try:
            Zv1 = Z0* (ZL - 1j*Z0*math.tan(2*math.pi*-d))/(Z0-1j*ZL*math.tan(2*math.pi*-d))
        except Exception as e:
            Zv1 = msg_error

        try:
            Z0_stub = Z0 # for semplicity

            Zstub = Z0_stub* (ZL_stub - 1j*Z0_stub*math.tan(2*math.pi*-l))/(Z0_stub-1j*ZL_stub*math.tan(2*math.pi*-l))
        except Exception as e:
            Zstub = msg_error


        try:
            Zv2 = parallel(Zv1, Zstub)
        except Exception as e:
            Zv2 = msg_error



        # displaying

        try:
            self.Zv1_lineedit.setText("{:.4g}".format(Zv1))
        except Exception:
            self.Zv1_lineedit.setText(msg_error)

        try:
            self.zv1_lineedit.setText("{:.4g}".format(Zv1/Z0))
        except Exception:
            self.zv1_lineedit.setText(msg_error)


        try:
            self.Yv1_lineedit.setText("{:.4g}".format(1/Zv1))
        except Exception:
            self.Yv1_lineedit.setText(msg_error)

        try:
            yv1 = 1/(Zv1/Z0)
            if (yv1.real >= 0.98 and yv1.real <= 1.02):
                self.yv1_lineedit.setStyleSheet("color: green")
            else:
                self.yv1_lineedit.setStyleSheet("color: red")

            self.yv1_lineedit.setText("{:.4g}".format(yv1))
        except Exception as e:
            print(e) 
            self.yv1_lineedit.setText(msg_error)




        try:
            if (Zv2.real >= 0.98*Z0.real and Zv2.real <= 1.02*Z0.real):
                self.Zv2_lineedit.setStyleSheet("color: green")
            else:
                self.Zv2_lineedit.setStyleSheet("color: red")

            self.Zv2_lineedit.setText("{:.4g}".format(Zv2))
        except Exception:
            self.Zv2_lineedit.setText(msg_error)

        try:
            self.zv2_lineedit.setText("{:.4g}".format(Zv2/Z0))
        except Exception:
            self.zv2_lineedit.setText(msg_error)


    # A key has been pressed!
    def keyPressEvent(self, event):
        # Did the user press the Escape key?
        if event.key() == QtCore.Qt.Key_W:
            self.close()


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())