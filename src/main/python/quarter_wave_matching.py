#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue May  8 14:08:45 CEST 2018

@author(s)   : Francesco Urbani
@file        : quarter_wave_matching.py
@descritpion : 

"""



import numpy as np
import matplotlib.pyplot as plt
import cmath
import math

from twoport.utils import find_nearest
from S_functions import calculate_gamma, calculate_Z_from_gamma
from ImprovedComplex import ImprovedComplex

msg_error = "" # display nothing if error occurs


def normalize_impedance(z, z0):
    return z/z0 
    # return (z/z0).real if (z/z0).imag == 0 else z/z0 


def calculate_tab_quarter_wave_im(self):

    # --------------
    # read inputs
    # --------------

    try:
        Z0 = float(self.Z0_box2.text())
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
            # Z_in = Z_in.real if Z_in.imag == 0 else Z_in
        except Exception as e:
            Z_in = msg_error

        try:
            Z_out = calculate_Z_from_gamma(gamma_zout, Z0)
            # Z_out = Z_out.real if Z_out.imag == 0 else Z_out
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

    # --------------
    # displaying
    # --------------

    try:
        # self.z_in_box_2.setText(f"{ImprovedComplex(Z_in)}")       # FIX
        self.z_in_box_2.setText(f"{Z_in:.4g}")
    except Exception as e: # thrown if Z_in is not a number hence the significat digits cannot be evaluated
        self.z_in_box_2.setText(msg_error)
    try:
        # self.z_in_box_5.setText(f"{ImprovedComplex(Z_out)}")      # FIX
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
        self.gamma_zin_box.setText(f"{abs(gamma_zin):.4g} ∠ {math.degrees(cmath.phase(gamma_zin)):.4g}")
    except Exception as e:
        self.gamma_zin_box.setText(msg_error)
    try:
        self.gamma_zout_box.setText(f"{abs(gamma_zout):.4g} ∠ {math.degrees(cmath.phase(gamma_zout)):.4g}")
    except Exception as e:
        self.gamma_zout_box.setText(msg_error)






    # mapping the angles with the lambda scale
    num_points = 10001 # 10k points + 1, if num_points is odd some relevant points such as 0.125 or 0.375 won't be screwed up
    angle_map  = np.linspace(np.pi, -np.pi, num_points)
    lambda_map = np.linspace(0    , 0.5   , num_points)

    try:
        # getting the lambda of gamma_zin
        phase_zin = cmath.phase(gamma_zin)
        phase_zin_approx = find_nearest(angle_map, phase_zin)
        ind_ = np.where(angle_map==phase_zin_approx)[0][0] # get the index of that value into the array angle_map
        lambda_zin = lambda_map[ind_] # get the value on the lambda_map array corresponding to angle
    except Exception as e:
        lambda_zin = msg_error
    

    try:
        # getting the lambda of gamma_zout
        phase_zout = cmath.phase(gamma_zout)
        phase_zout_approx = find_nearest(angle_map, phase_zout)
        ind_ = np.where(angle_map==phase_zout_approx)[0][0] # get the index of that value into the array angle_map
        lambda_zout = lambda_map[ind_] # get the value on the lambda_map array corresponding to angle   
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

    return Z0, Z_in, Z_out, gamma_zin, gamma_zout



def showSmithPlot(self):
    Z0, Z_in, Z_out, gamma_zin, gamma_zout = calculate_tab_quarter_wave_im(self)


    try:
        import twoport.smithplot
        twoport.smithplot.plot_Smith_quarter_wave_matching(Z0, Z_in, Z_out, gamma_zin, gamma_zout)
    except Exception as e:
        # raise e
        print(e)


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


def clean_all_quarter_wave(self):
    self.Z_in_box.setText("")
    self.Z_out_box.setText("")
    self.ZS_box_9.setText("")
    self.ZS_box_6.setText("")
    self.ZS_box_7.setText("")
    self.ZS_box_8.setText("")
    self.Calculate_quarter.click()



    