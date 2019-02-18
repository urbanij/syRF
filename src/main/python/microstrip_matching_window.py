#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Feb 18 19:09:32 CET 2019

@author(s)   : Francesco Urbani
@file        : main.py
@descritpion : The main file

"""

from PyQt5.QtWidgets import QMainWindow, QAction, QStatusBar, QToolBar, QMenuBar, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QSize

from microstrip_matching_window_ui import Ui_MainWindow # main ui window autogenerated by PyQt



import microstrip_matching_tab
import open_pdf


msg_error = "" # display nothing if error occurs



class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)




        # microstrip_matching
        # first col
        self.l_lambda_box.editingFinished.connect(self.calculate_button_6.click)
        self.z0box.editingFinished.connect(self.calculate_button_6.click)
        self.epsilon_r_box.editingFinished.connect(self.calculate_button_6.click)
        self.h_box.editingFinished.connect(self.calculate_button_6.click)
        self.f_box_3.editingFinished.connect(self.calculate_button_6.click)

        # second col
        self.length_box_2.editingFinished.connect(self.calculate_button_6.click)
        self.w_box_2.editingFinished.connect(self.calculate_button_6.click)
        self.h_box_2.editingFinished.connect(self.calculate_button_6.click)
        self.epsilon_r_box_2.editingFinished.connect(self.calculate_button_6.click)
        self.f_box_4.editingFinished.connect(self.calculate_button_6.click)

        self.calculate_button_6.clicked.connect(self.compute_matching_microstrip)
        self.clean_all_button4.clicked.connect(self.clean_all_microstrip_tab)
        self.open_plot_button.clicked.connect(self.open_plots)
        self.show_er_plots_button.clicked.connect(self.show_plots)
        
        

        
        



    def compute_matching_microstrip(self):
        microstrip_matching_tab.compute_matching_microstrip(self)

    def open_plots(self):
        open_pdf.open_pdf("microstrip_matching/epsilon_r_graphs.pdf")


    def show_plots(self):
        microstrip_matching_tab.show_plots(self)

    def clean_all_microstrip_tab(self):
        microstrip_matching_tab.clean_all_microstrip_tab(self)


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
