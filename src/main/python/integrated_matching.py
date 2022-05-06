#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Feb 20 11:58:01 CET 2019

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

# from PyQt5.QtCore import QSize

from pyui.integrated_matching_ui import (
    Ui_MainWindow,
)  # main ui window autogenerated by PyQt


import integrated_matching_formula
import open_pdf

msg_error = ""  # display nothing if error occurs


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        self.menuBar.setNativeMenuBar(True)

        self.action_Open_formulas.triggered.connect(
            self.Open_formulas_integrated_matching
        )
        self.action_Quit_IM.triggered.connect(self.close)

        self.Ic_input.setFocus()  # set focus on startup

        self.Lb_vs_Ic_button.setEnabled(False)

        self.Rs_input.editingFinished.connect(
            self.calculate_integrated_matching_button.click
        )
        self.ft_input.editingFinished.connect(
            self.calculate_integrated_matching_button.click
        )
        self.Ic_input.editingFinished.connect(
            self.calculate_integrated_matching_button.click
        )
        self.Vt_input.editingFinished.connect(
            self.calculate_integrated_matching_button.click
        )
        self.f0_input.editingFinished.connect(
            self.calculate_integrated_matching_button.click
        )

        self.Lb_vs_Ic_button.clicked.connect(self.plot_Lb_vs_Ic)

        self.calculate_integrated_matching_button.clicked.connect(
            self.calculate_integrated_matching
        )
        self.clean_integrated_matching_button.clicked.connect(
            self.clean_integrated_matching
        )

    def read_inputs(self):
        # read input coordinate as complex number
        try:
            Ic = eval(self.Ic_input.text())  # mA
        except Exception as e:
            Ic = msg_error

        try:
            Vt = eval(self.Vt_input.text())  # mV
        except Exception as e:
            Vt = msg_error

        try:
            ft = eval(self.ft_input.text())  # GHz
        except Exception as e:
            ft = msg_error

        try:
            f0 = eval(self.f0_input.text())  # GHz
        except Exception as e:
            f0 = msg_error

        try:
            Rs = eval(self.Rs_input.text())  # ohm
        except Exception as e:
            Rs = msg_error

        return Ic, Vt, ft, f0, Rs

    def calculate_integrated_matching(self):

        Ic, Vt, ft, f0, Rs = self.read_inputs()

        # compute
        try:
            gm = integrated_matching_formula.gm(Ic, Vt)  # S
            gm *= 1e3  # mS
        except Exception as e:
            gm = msg_error

        try:
            c_pi = integrated_matching_formula.c_pi(Ic, Vt, ft)  # F
            c_pi *= 1e15  # fF
        except Exception as e:
            c_pi = msg_error

        try:
            Le = integrated_matching_formula.Le(Rs, ft)  # H
            Le *= 1e12  # pH
        except Exception as e:
            Le = msg_error

        try:
            Lb = integrated_matching_formula.Lb(f0, Ic, Vt, ft, Rs)  # H
            Lb *= 1e9  # nH
        except Exception as e:
            Lb = msg_error

        # display

        self.gm_text_browser.setText("{}".format(gm))
        self.c_pi_text_browser.setText("{}".format(c_pi))
        self.Le_text_browser.setText("{}".format(Le))
        self.Lb_text_browser.setText("{}".format(Lb))

    def clean_integrated_matching(self):
        self.Ic_input.setText("")
        self.Vt_input.setText("")
        self.ft_input.setText("")
        self.f0_input.setText("")
        self.Rs_input.setText("")

        self.calculate_integrated_matching_button.click()
        self.Ic_input.setFocus()  # set focus on startup

    def Open_formulas_integrated_matching(self):
        open_pdf.open_pdf("doc/integrated_matching/integrated_matching.pdf")

    def plot_Lb_vs_Ic(self):

        Ic, Vt, ft, f0, Rs = self.read_inputs()

        import numpy as np
        import matplotlib.pyplot as plt

        ic = np.linspace(1e-7, 1e-4, 1e5)  # A
        try:
            Lb = integrated_matching_formula.Lb(f0 * 1e9, ic, Vt * 1e-3, ft * 1e9, Rs)
            Lb *= 1e9  # nH
        except Exception as e:
            pass

        try:
            Le = integrated_matching_formula.Le(Rs, ft * 1e9)
            Lb *= 1e12  # pH
        except Exception as e:
            pass

        try:
            fig, ax1 = plt.subplots(figsize=(10, 8))

            color = "tab:red"
            ax1.set_xlabel("$I_C$")
            ax1.set_ylabel("$L_B$", color=color)
            ax1.plot(ic, Lb, color=color)
            ax1.tick_params(axis="y", labelcolor=color)

            ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

            color = "tab:blue"
            ax2.set_ylabel(
                "$L_E$", color=color
            )  # we already handled the x-label with ax1
            ax2.axhline(y=Le, color=color)  # linestyle='-', label="$L_E$")
            ax2.tick_params(axis="y", labelcolor=color)

            plt.grid(True, which="both", ls="-")

            fig.tight_layout()  # otherwise the right y-label is slightly clipped
            plt.show()
        except Exception as e:
            pass

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
