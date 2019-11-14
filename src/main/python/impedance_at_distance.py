#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Nov 14 17:37:36 CET 2019

@author(s)   : Francesco Urbani
@file        : impedance_at_distance.py
@descritpion : computes the impedance seen at a distance d from the load, along the (non dissipative) TL.
               
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from pyui.impedance_at_distance_ui import Ui_MainWindow

import math

msg_error = "" # display nothing if error occurs


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        

        self.zL_input.setFocus()  # set focus on startup
        
        self.zL_input.editingFinished.connect(self.calculate14_button.click)
        self.d_input.editingFinished.connect(self.calculate14_button.click)

        self.calculate14_button.clicked.connect(self.compute)
        self.clean_all14_button.clicked.connect(self.clean_polar)



    def compute(self):
        
        # read input coordinate as complex number
        try:
            zl_init = complex(self.zL_input.text())
        except Exception as e:
            zl_init = msg_error

        try:
            d = eval(self.d_input.text())
        except Exception as e:
            d = msg_error

        # some fancyness... reupdates the field, in case the user writes something like 2+3+1+5+3j  ==> 11+3j
        try:
            self.d_input.setText(str(eval(self.d_input.text()))) # updates d_input
        except SyntaxError as e:
            self.d_input.setText(msg_error)

        try:
            R0 = float(self.R0input.text())
        except Exception as e:
            R0 = msg_error
        



        # compute
        try:
            # -d because I'm moving from the load to the generator
            zl_final = (zl_init - 1j*math.tan(2*math.pi*-d))/(1-1j*zl_init*math.tan(2*math.pi*-d))
        except Exception as e:
            zl_final = msg_error

        

        # display
        try:
            self.zl2_outputbox.setText(f"{zl_final:.5g}")
        except Exception as e:
            self.zl2_outputbox.setText(msg_error)

        try:
            self.zl_actual_outputbox.setText(f"{R0*zl_final:.5g}")
        except Exception as e:
            self.zl_actual_outputbox.setText(msg_error)
            

        # keep focus on input P_coord_lineedit
        # self.P_coord_lineedit.setFocus() # if on does not allow drag and drop! (wtf)

    

    def clean_polar(self):
        self.zL_input.setText("")
        self.d_input.setText("")
        self.R0input.setText("")
        self.calculate14_button.click()
        self.zL_input.setFocus()

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
