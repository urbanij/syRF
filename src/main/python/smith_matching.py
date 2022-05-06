#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue May  8 14:08:45 CEST 2018

@author(s)   : Francesco Urbani
@file        : smith_matching.py
@descritpion : Design matching network -- either w/ lumped parameter or TL -- with the aid 
               of the Smith Chart.

"""



import numpy as np
import matplotlib.pyplot as plt
import cmath
import math

from twoport.utils import find_nearest
import intersections
import S_functions

from S_functions import calculate_gamma, calculate_Z_from_gamma, calculate_vswr_from_gamma
from smith_matching_utils import round_of_rating, lambda_tick_map

msg_error = "" # display nothing if error occurs



"""

TODO:

    results can be inconsistent: distance lambda1 not referred to zL 1 and vice versa. fix that!

    
"""


def normalize_impedance(z, z0):
    return z/z0 
    # return (z/z0).real if (z/z0).imag == 0 else z/z0 



LAMBDA_TICK_MAP = lambda_tick_map()

def calculate_tab_quarter_wave_im(self):

    # --------------
    # read inputs
    # --------------

    try:
        Z0 = complex(self.Z0_box2.text())
    except ValueError:
        Z0 = msg_error



    if self.radioButton.isChecked(): # INPUT SOURCE/LOAD AS Z

        try:
            Z_in = complex(self.Z_in_box.text())
        except Exception as e:
            Z_in = msg_error

        try:
            Z_out = complex(self.Z_out_box.text())
        except Exception as e:
            Z_out = msg_error

        # --------------
        # calculate
        # --------------

        try:
            gamma_zin = calculate_gamma(Z_in, Z0)
        except Exception as e:
            gamma_zin = msg_error

        # convert gamma_zin to polar form to better read the angle
        try:
            gamma_zin_polar = cmath.polar(gamma_zin)
        except Exception as e:
            gamma_zin_polar = msg_error

        try:
            gamma_zout = calculate_gamma(Z_out, Z0)
        except Exception as e:
            gamma_zout = msg_error

        # convert gamma_zout to polar form to better read the angle
        try:
            gamma_zout_polar = cmath.polar(gamma_zout)
        except Exception as e:
            gamma_zout_polar = msg_error



    else: # INPUT SOURCE/LOAD AS GAMMA
        
        # read inputs

        # gamma_zin
        try:
            abs_gamma_zin = float(self.ZS_box_9.text())
        except Exception as e:
            abs_gamma_zin = msg_error

        try:
            arg_gamma_zin = float(self.ZS_box_6.text())
        except Exception as e:
            arg_gamma_zin = msg_error

        # gamma_zout
        try:
            abs_gamma_zout = float(self.ZS_box_7.text())
        except Exception as e:
            abs_gamma_zout = msg_error

        try:
            arg_gamma_zout = float(self.ZS_box_8.text())
        except Exception as e:
            arg_gamma_zout = msg_error

        

        # --------------
        # calculate
        # --------------

        # convert gamma_zin and gamma_zout to rectangular form
        try:
            gamma_zin = cmath.rect(abs_gamma_zin, math.radians(arg_gamma_zin))
        except Exception as e:
            gamma_zin = msg_error

        try:
            gamma_zout = cmath.rect(abs_gamma_zout, math.radians(arg_gamma_zout))
        except Exception as e:
            gamma_zout = msg_error
        # --

        # calculate Z from gamma
        try:
            Z_in = calculate_Z_from_gamma(gamma_zin, Z0)
            Z_in = 0 if abs(Z_in) <= 1e-4 else Z_in  # cuts some calculations
        except Exception as e:
            Z_in = msg_error

        try:
            Z_out = calculate_Z_from_gamma(gamma_zout, Z0)
            Z_out = 0 if abs(Z_out) <= 1e-4 else Z_out  # cuts some calculations
        except Exception as e:
            Z_out = msg_error


    # common part:
    try:
        z_in = normalize_impedance(Z_in, Z0)
    except Exception as e:
        z_in = msg_error

    try:
        z_out = normalize_impedance(Z_out, Z0)
    except Exception as e:
        z_out = msg_error

    try:
        vswr_zin = calculate_vswr_from_gamma(gamma_zin)
    except Exception as e:
        vswr_zin = msg_error

    try:
        vswr_zout = calculate_vswr_from_gamma(gamma_zout)
    except Exception as e:
        vswr_zout = msg_error


    try:
        zin_constant_r_intersection = intersections.find_intersection_points(c1=0.5, r1=0.5, c2=0, r2=abs(gamma_zin))
        zin_constant_r_intersection = S_functions.calculate_Z_from_gamma(gamma=zin_constant_r_intersection[0], z0=1)
    except Exception as e:
        zin_constant_r_intersection = msg_error

    try:
        zout_constant_r_intersection = intersections.find_intersection_points(c1=0.5, r1=0.5, c2=0, r2=abs(gamma_zout))
        zout_constant_r_intersection = S_functions.calculate_Z_from_gamma(gamma=zout_constant_r_intersection[0], z0=1)
    except Exception as e:
        zout_constant_r_intersection = msg_error

    


    # --------------
    # displaying
    # --------------

    try:
        # self.z_in_box_2.setText("+∞" if Z_in == math.inf else f"{Z_in:.4g}")
        self.z_in_box_2.setText(f"{Z_in:.4g}")
    except Exception as e: # thrown if Z_in is not a number hence the significat digits cannot be evaluated
        self.z_in_box_2.setText(msg_error)
    try:
        self.z_in_box_5.setText(f"{Z_out:.4g}")
    except Exception as e:
        self.z_in_box_5.setText(msg_error)

    try:
        self.z_in_box.setText(f"{z_in:.4g}")
    except Exception as e:
        self.z_in_box.setText(msg_error)
    try:
        self.z_out_box.setText(f"{z_out:.4g}")
    except Exception as e:
        self.z_out_box.setText(msg_error)
    
    try:
        self.gamma_zin_actual_box.setText(f"{gamma_zin:.4g}")
    except Exception as e:
        self.gamma_zin_actual_box.setText(msg_error)
    try:
        self.gamma_zin_box.setText(f"{abs(gamma_zin):.4g} ∠ {math.degrees(cmath.phase(gamma_zin)):.4g} deg")
    except Exception as e:
        self.gamma_zin_box.setText(msg_error)

    try:
        self.gamma_zout_actual_box.setText(f"{gamma_zout:.4g}")
    except Exception as e:
        self.gamma_zout_actual_box.setText(msg_error)
    try:
        self.gamma_zout_box.setText(f"{abs(gamma_zout):.4g} ∠ {math.degrees(cmath.phase(gamma_zout)):.4g} deg")
    except Exception as e:
        self.gamma_zout_box.setText(msg_error)

    try:
        self.vswr_zin_box.setText(f"{vswr_zin:.4g}")
    except Exception as e:
        self.vswr_zin_box.setText(msg_error)
    try:
        self.vswr_zout_box.setText(f"{vswr_zout:.4g}")
    except Exception as e:
        self.vswr_zout_box.setText(msg_error)


    
    try:
        phase_zin = round_of_rating(math.degrees(cmath.phase(gamma_zin)))
        lambda_zin = LAMBDA_TICK_MAP[round_of_rating(phase_zin)]
    except Exception as e:
        lambda_zin = msg_error

    try:
        phase_zout = round_of_rating(math.degrees(cmath.phase(gamma_zout)))
        lambda_zout = LAMBDA_TICK_MAP[round_of_rating(phase_zout)]
    except Exception as e:
        lambda_zout = msg_error    


    # printing lambdas to the right boxes
    try:
        self.lambda_tick_zin_box.setText(f"{lambda_zin:.4g}")
    except Exception as e:
        self.lambda_tick_zin_box.setText(msg_error)
    try:
        self.lambda_tick_zout_box.setText(f"{lambda_zout:.4g}")
    except Exception as e:
        self.lambda_tick_zout_box.setText(msg_error)

    
    try:
        self.zin_constant_r_int1_box.setText(f"{zin_constant_r_intersection:.4g}")
    except Exception as e:
        self.zin_constant_r_int1_box.setText(msg_error)
    try:
        self.zin_constant_r_int2_box.setText(f"{zin_constant_r_intersection.conjugate():.4g}")
    except Exception as e:
        self.zin_constant_r_int2_box.setText(msg_error)
    
    try:
        self.zout_constant_r_int1_box.setText(f"{zout_constant_r_intersection:.4g}")
    except Exception as e:
        self.zout_constant_r_int1_box.setText(msg_error)
    try:
        self.zout_constant_r_int2_box.setText(f"{zout_constant_r_intersection.conjugate():.4g}")
    except Exception as e:
        self.zout_constant_r_int2_box.setText(msg_error)
    

    return Z0, Z_in, Z_out, gamma_zin, gamma_zout
    


def showSmithPlot(self):
    Z0, Z_in, Z_out, gamma_zin, gamma_zout = calculate_tab_quarter_wave_im(self)


    try:
        import twoport.smithplot
        twoport.smithplot.plot_Smith_smith_matching(Z0, Z_in, Z_out, gamma_zin, gamma_zout)
    except Exception as e:
        # raise e
        print(e)
        pass


def disable_boxes_quarter_wave_im(self):
    if self.radioButton.isChecked():
        self.label_267.setEnabled(False)
        self.ZS_box_9.setEnabled(False)
        self.label_266.setEnabled(False)
        self.ZS_box_6.setEnabled(False)
        self.label_269.setEnabled(False)
        self.ZS_box_7.setEnabled(False)
        self.label_268.setEnabled(False)
        self.ZS_box_8.setEnabled(False)

        self.label_76.setEnabled(True)
        self.Z_in_box.setEnabled(True)
        self.label_91.setEnabled(True)
        self.label_75.setEnabled(True)
        self.Z_out_box.setEnabled(True)
        self.label_92.setEnabled(True)
        self.Z_in_box.setFocus()
    else:
        self.label_267.setEnabled(True)
        self.ZS_box_9.setEnabled(True)
        self.label_266.setEnabled(True)
        self.ZS_box_6.setEnabled(True)
        self.label_269.setEnabled(True)
        self.ZS_box_7.setEnabled(True)
        self.label_268.setEnabled(True)
        self.ZS_box_8.setEnabled(True)

        self.label_76.setEnabled(False)
        self.Z_in_box.setEnabled(False)
        self.label_91.setEnabled(False)
        self.label_75.setEnabled(False)
        self.Z_out_box.setEnabled(False)
        self.label_92.setEnabled(False)
        self.ZS_box_9.setFocus()

