#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Feb 18 18:44:30 CET 2019

@author(s)   : Francesco Urbani
@file        : lumped_matching.py
@descritpion : Lumped parameters matching network

               
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from lumped_matching_ui import Ui_MainWindow

import LC_matching_tab
import plot_reflection_coefficient
import open_pdf


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)



        # LC_matching
        self.f0_box.editingFinished.connect(self.Calculate_button_3.click)
        self.input_box.editingFinished.connect(self.Calculate_button_3.click)
        self.output_box.editingFinished.connect(self.Calculate_button_3.click)
        self.comboBox.currentIndexChanged['QString'].connect(self.Calculate_button_3.click)
        self.comboBox_2.currentIndexChanged['QString'].connect(self.Calculate_button_3.click)
        self.open_pdf_sketch_button.clicked.connect(self.open_pdf_sketch_matching)
        # self.comboBox_3.currentIndexChanged['QString'].connect(self.Calculate_button_3.click)

        self.Calculate_button_3.clicked.connect(self.compute_LC_matching)
        self.Clean_all_button_3.clicked.connect(self.clean_all_LC_matching)
        self.Clean_all_button_3.clicked.connect(self.Calculate_button_3.click)
        self.plot.clicked.connect(self.plot_reflection_coefficient)



    def compute_LC_matching(self):
        LC_matching_tab.compute_LC_matching(self)

    def clean_all_LC_matching(self):
        LC_matching_tab.clean_all_LC_matching(self)

    def plot_reflection_coefficient(self):
        plot_reflection_coefficient.plot_gamma( LC_matching_tab.compute_LC_matching(self) )

    def open_pdf_sketch_matching(self):
        open_pdf.open_pdf("../../../aux/matching_network.pdf")


    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.close()



# can run stand alone
if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())
