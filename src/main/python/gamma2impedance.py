#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Nov 14 17:37:36 CET 2019

@author(s)   : Francesco Urbani
@file        : impedance_at_distance.py
@descritpion : computes the impedance seen at a distance d from the load, along the (non dissipative) TL.
               
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from pyui.gamma2impedance_ui import Ui_MainWindow

import math

msg_error = "" # display nothing if error occurs


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        

        self.gamma_lineedit.setFocus()  # set focus on startup
        
        self.gamma_lineedit.editingFinished.connect(self.calculate65_button.click)
        self.Z0input.editingFinished.connect(self.calculate65_button.click)
        
        self.calculate65_button.clicked.connect(self.compute)
        self.clean_all65_button.clicked.connect(self.clean)



    def compute(self):
        
        # read input coordinate as complex number
        try:
            gamma = complex(self.gamma_lineedit.text())
        except Exception as e:
            gamma = msg_error

        try:
            Z0 = complex(self.Z0input.text())
        except Exception as e:
            Z0 = msg_error

        # compute
        try:
            z = (1+gamma)/(1-gamma)
        except Exception as e:
            z = msg_error

        
        # display
        try:
            self.norm_impedance_text_browser.setText(f"{z:.4g}")
        except Exception as e:
            self.norm_impedance_text_browser.setText(msg_error)

        try:
            self.impedance_text_browser.setText(f"{z*Z0:.4g}")
        except Exception as e:
            self.impedance_text_browser.setText(msg_error)

            

    def clean(self):
        self.gamma_lineedit.setText("")
        self.norm_impedance_text_browser.setText("")
        self.gamma_lineedit.setFocus()

    # A key has been pressed!
    def keyPressEvent(self, event):
        # Did the user press the Escape key?
        if event.key() == QtCore.Qt.Key_Escape or event.key() == QtCore.Qt.Key_W:
            self.close()

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())
