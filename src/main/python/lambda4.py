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

import math
import cmath

from S_functions import calculate_gamma
from smith_matching_utils import round_of_rating, lambda_tick_map

msg_error = ""  # display nothing if error occurs


LAMBDA_TICK_MAP = lambda_tick_map()


def compute_distance(lambda_tick_Zl):

    return (0.25 - lambda_tick_Zl % 0.5, 0.5 - lambda_tick_Zl % 0.5)


def compute_Z0_TL(*, Z0, gamma_l):
    ## r is the radius of the circle centered in (0,0), with radius gamma
    r = abs(gamma_l)

    ## returns - in order - the point on the right intersection with the x-axis first and then
    ## the left point, i.e. bigger value first and smaller after.
    return ((Z0 * Z0 * (1 + r) / (1 - r)) ** 0.5, (Z0 * Z0 * (1 - r) / (1 + r)) ** 0.5)


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        self.zl_input.setFocus()  # set focus on startup

        self.zl_input.editingFinished.connect(self.Calculate_lambda4.click)
        self.Z0_input.editingFinished.connect(self.Calculate_lambda4.click)

        self.label_125.setToolTip("Distance from load to λ/4-length TL")
        self.label_126.setToolTip("Distance from load to λ/4-length TL")
        self.label_127.setToolTip("Impedance value of λ/4-length TL")
        self.label_128.setToolTip("Impedance value of λ/4-length TL")

        self.Calculate_lambda4.clicked.connect(self.calculate_z_lambda4)

    def calculate_z_lambda4(self):

        # read inputs
        try:
            zl = complex(self.zl_input.text())
        except Exception as e:
            zl = msg_error

        try:
            z0 = complex(self.Z0_input.text())
        except Exception as e:
            z0 = msg_error

        try:
            gamma_zl = calculate_gamma(zl, z0)
            phase_zl = round_of_rating(math.degrees(cmath.phase(gamma_zl)))
            lambda_zl = LAMBDA_TICK_MAP[round_of_rating(phase_zl)]
        except Exception as e:
            pass

        # compute
        try:
            d1 = compute_distance(lambda_zl)[0]
        except Exception as e:
            d1 = msg_error

        try:
            d2 = compute_distance(lambda_zl)[1]
        except Exception as e:
            d2 = msg_error

        try:
            z1_TL_out = compute_Z0_TL(Z0=z0, gamma_l=gamma_zl)[0].real
        except Exception as e:
            z1_TL_out = msg_error

        try:
            z2_TL_out = compute_Z0_TL(Z0=z0, gamma_l=gamma_zl)[1].real
        except Exception as e:
            z2_TL_out = msg_error

        # display
        try:
            self.d1_out.setText("{:.4g}".format(d1))
        except:
            self.d1_out.setText(msg_error)
        try:
            self.d2_out.setText("{:.4g}".format(d2))
        except:
            self.d2_out.setText(msg_error)
        try:
            self.z1_TL_out.setText("{:.4g}".format(z1_TL_out))
        except:
            self.z1_TL_out.setText(msg_error)
        try:
            self.z2_TL_out.setText("{:.4g}".format(z2_TL_out))
        except:
            self.z2_TL_out.setText(msg_error)

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
