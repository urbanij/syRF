#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Feb 14 19:14:33 CET 2019

@author(s)   : Francesco Urbani
@file        : quarter-wave-matching.py
@descritpion : lambda 4 calculation

               Can be either run as standalone app (python rect2polar.py) 
               or withing syRF (open rect2polar button into S tab)
               
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from pyui.lambda4_ui import Ui_MainWindow

msg_error = "" # display nothing if error occurs


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)
        

        self.z1_box.setFocus()  # set focus on startup
        
        self.z1_box.editingFinished.connect(self.Calculate_lambda4.click)
        self.z2_box.editingFinished.connect(self.Calculate_lambda4.click)

        self.Calculate_lambda4.clicked.connect(self.calculate_z_lambda4)
        self.clean_lambda4_button.clicked.connect(self.clean_polar)



        

    def calculate_z_lambda4(self):

        # read inputs
        try:
            z_norm_1 = float(self.z1_box.text())
        except Exception as e:
            z_norm_1 = msg_error

        try:
            z_norm_2 = float(self.z2_box.text())
        except Exception as e:
            z_norm_2 = msg_error
        
        try:
            z0 = float(self.Z0_box2_2.text())
        except Exception as e:
            z0 = msg_error



        # compute
        try:
            z = (z_norm_1*z_norm_2)**0.5
        except Exception as e:
            z = msg_error

        try:
            Z = z*z0
        except Exception as e:
            Z = msg_error



        # display
        self.zbox111.setText(str(z))
        self.Zbox111.setText(str(Z))


    

    def clean_polar(self):
        self.z1_box.setText("")
        self.z2_box.setText("")
        self.Calculate_lambda4.click()
        self.z1_box.setFocus()

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

