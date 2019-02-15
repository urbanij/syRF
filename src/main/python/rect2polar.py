#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Feb 14 17:06:16 CET 2019

@author(s)   : Francesco Urbani
@file        : rect2polar
@descritpion : converts rectangular coordinates into 
               polar (magnitude + angle in degrees) coordinates

               Can be either run as standalone app (python rect2polar.py) 
               or withing syRF (open rect2polar button into S tab)
               
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from rect2polar_ui import Ui_MainWindow

import math
import cmath


msg_error = "" # display nothing if error occurs


class utilProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(utilProgram, self).__init__(parent)
        self.setupUi(self)
        

        self.P_coord_lineedit.setFocus()  # set focus on startup
        
        self.P_coord_lineedit.editingFinished.connect(self.calculate12_button.click)

        self.calculate12_button.clicked.connect(self.calc_polar)
        self.clean_all12_button.clicked.connect(self.clean_polar)



    def calc_polar(self):
        
        # read input coordinate as complex number
        try:
            P_coord = complex(self.P_coord_lineedit.text())
        except Exception as e:
            P_coord = msg_error
        

        # compute
        try:
            mag = abs(P_coord)
        except Exception as e:
            mag = msg_error

        try:
            phase = math.degrees(cmath.phase(P_coord))
        except Exception as e:
            phase = msg_error


        # display
        self.mag_text_browser.setText("{}".format(mag))
        self.phase_text_browser.setText("{}".format(phase))

        # keep focus on input P_coord_lineedit
        self.P_coord_lineedit.setFocus() 

    

    def clean_polar(self):
        self.P_coord_lineedit.setText("")
        self.calculate12_button.click()
        self.P_coord_lineedit.setFocus()



if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = utilProgram()
    nextGui.show()
    sys.exit(app.exec_())
