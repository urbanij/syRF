#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Apr 29 10:46:20 2018

@author(s)   : Francesco Urbani
@file        : microstrip_matching_tab.py
@descritpion : 

"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import cmath
from twoport.utils import find_nearest
import microstrip_matching.er_graphs_points as epsilon_function

msg_error = "" # display nothing if error occurs

c = 299792458.0 # speed of light

def get_abscissa_from_first_graph(er, z):
    if er == 2:
        f = epsilon_function.er2_1
    elif er == 4:
        f = epsilon_function.er4_1
    elif er == 6:
        f = epsilon_function.er6_1
    elif er == 8:
        f = epsilon_function.er8_1
    elif er == 10:
        f = epsilon_function.er10_1
    elif er == 12:
        f = epsilon_function.er12_1

    x = epsilon_function.x2_1 # 
    
    closest_to_z = find_nearest(f, z) # find the nearest value to z contained into f.
    if abs(closest_to_z - z) > 4:
        return # uncovered value
    ind_ = np.where(f==closest_to_z)[0][0] # get the index of that value into the array f
    x_point = x[ind_] # get the value on the x axis of the index above read.
    w_over_h = x_point
    return w_over_h



def get_ordinate_from_second_graph(er, x_point):
    if er == 2:
        f = epsilon_function.er2_2
    elif er == 4:
        f = epsilon_function.er4_2
    elif er == 6:
        f = epsilon_function.er6_2
    elif er == 8:
        f = epsilon_function.er8_2
    elif er == 10:
        f = epsilon_function.er10_2
    elif er == 12:
        f = epsilon_function.er12_2
    
    x = epsilon_function.x2_2

    closest_to_x_point = find_nearest(x, x_point)
    ind_ = np.where(x==closest_to_x_point)[0][0]
    y_point = f[ind_]


    lambda_over_lambda_TEM = y_point
    return lambda_over_lambda_TEM



def get_ordinate_from_first_graph(er, x_point):
    if er == 2:
        f = epsilon_function.er2_1
    elif er == 4:
        f = epsilon_function.er4_1
    elif er == 6:
        f = epsilon_function.er6_1
    elif er == 8:
        f = epsilon_function.er8_1
    elif er == 10:
        f = epsilon_function.er10_1
    elif er == 12:
        f = epsilon_function.er12_1

    x = epsilon_function.x2_1

    closest_to_x_point = find_nearest(x, x_point)
    ind_ = np.where(x==closest_to_x_point)[0][0]
    y_point = f[ind_]


    z0 = y_point
    return z0





def compute_matching_microstrip(self):
    


    # ---------------
    # FIRST COLUMN
    # ---------------

    # ---------------
    # reading inputs:
    # ---------------


    try:
        l_of_lambda_1 = float(self.l_lambda_box.text())
    except Exception as e:
        l_of_lambda_1 = msg_error


    try:
        z0_1 = float(self.z0box.text())
    except Exception as e:
        z0_1 = msg_error

    
    try:
        epsilon_r_1 = float(self.epsilon_r_box.text())
    except Exception as e:
        epsilon_r_1 = msg_error

    
    try:
        h = float(self.h_box.text())
        h *= 1e-3 # now h is in meters
    except Exception as e:
        h = msg_error

    try:
        f = float(self.f_box_3.text())
        f *= 1e6 # f is now in Hz (read in MHz)
    except Exception as e:
        f = msg_error

    # ---------------


    # ---------------
    # calculate I col:
    # ---------------

    try:
        w_over_h_1 = get_abscissa_from_first_graph(epsilon_r_1, z0_1)
    except Exception as e:
        w_over_h_1 = msg_error


    try:
        w = h * w_over_h_1
    except Exception as e:
        w = msg_error


    try:
        lambda_TEM = c/(f*(epsilon_r_1)**0.5)
    except Exception as e:
        lambda_TEM = msg_error

    try:
        lambda_over_lambda_TEM = get_ordinate_from_second_graph(epsilon_r_1, w_over_h_1)
    except Exception as e:
        lambda_over_lambda_TEM = msg_error

    try:
        Lambda = lambda_TEM * lambda_over_lambda_TEM
    except Exception as e:
        Lambda = msg_error

    
    try:
        microstrip_actual_length = Lambda * l_of_lambda_1
    except Exception as e:
        microstrip_actual_length = msg_error



    # -------------------------------------------------
    # -------------------------------------------------
    # -------------------------------------------------





    # ---------------
    # SECOND COLUMN
    # ---------------
    try:
        length2 = float(self.length_box_2.text())
        length2 *= 1e-3 # from mm to meters
    except Exception as e:
        length2 = msg_error

    try:
        w2 = float(self.w_box_2.text())
    except Exception as e:
        w2 = msg_error

    try:
        h2 = float(self.h_box_2.text())
    except Exception as e:
        h2 = msg_error


    try:
        epsilon_r_2 = float(self.epsilon_r_box_2.text())
    except Exception as e:
        epsilon_r_2 = msg_error


    try:
        f2 = float(self.f_box_4.text())
        f2 *= 1e6 # f2 is now in Hz (read in MHz)
    except Exception as e:
        f2 = msg_error


    # ---------------


    # ---------------
    # calculate II col:
    # ---------------

    try:
        w_over_h_2 = w2/h2
    except Exception as e:
        w_over_h_2 = msg_error

    try:
        z0_2 = get_ordinate_from_first_graph(epsilon_r_2, w_over_h_2)
    except Exception as e:
        z0_2 = msg_error


    try:
        lambda_TEM2 = c/(f2*(epsilon_r_2)**0.5)
    except Exception as e:
        lambda_TEM2 = msg_error

    try:
        lambda_over_lambda_TEM2 = get_ordinate_from_second_graph(epsilon_r_2, w_over_h_2)
    except Exception as e:
        lambda_over_lambda_TEM2 = msg_error

    try:
        lambda2 = lambda_over_lambda_TEM2 * lambda_TEM2
    except Exception as e:
        lambda2 = msg_error

    try:
        l_of_lambda_2 = length2/lambda2
    except Exception as e:
        l_of_lambda_2 = msg_error











    # ---------------
    # display:
    # ---------------

    # -------------
    # I col
    # -------------

    if w_over_h_1 == None:
        # self.w_over_h_box.setText("<font color='red'>Uncovered value</font>")
        self.w_over_h_box.setText("Uncovered value")
    else:
        self.w_over_h_box.setText(str(w_over_h_1))

    try:
        self.w_box.setText(str(w*1e3)) # to mm
    except Exception as e:
        self.w_box.setText(msg_error)

    try:
        self.lambda_tem_box.setText(str(lambda_TEM*1e2)) # to cm
    except Exception as e:
        self.lambda_tem_box.setText(msg_error)

    self.lambda_over_lambda_tem_box.setText(str(lambda_over_lambda_TEM))

    try:
        self.lambda_box.setText(str(Lambda*1e2)) # to cm
    except Exception as e:
        self.lambda_box.setText(msg_error)

    try:
        self.length_box.setText(str(microstrip_actual_length*1e3)) # to mm
    except Exception as e:
        self.length_box.setText(msg_error)


    # -------------
    # II column
    # -------------
    try:
        self.w_over_h_box_2.setText(str(w_over_h_2))
    except Exception as e:
        self.w_over_h_box_2.setText(msg_error)


    try:
        self.z0box_2.setText(str(z0_2))
    except Exception as e:
        self.z0box_2.setText(msg_error)
    
    try:
        self.lambda_over_lambda_tem_box_2.setText(str(lambda_over_lambda_TEM2))
    except Exception as e:
        self.lambda_over_lambda_tem_box_2.setText(msg_error)

    try:
        self.lambda_tem_box_2.setText(str(lambda_TEM2*1e2)) # to cm
    except Exception as e:
        self.lambda_tem_box_2.setText(msg_error)

    try:
        self.lambda_box_2.setText(str(lambda2*1e2)) # to cm
    except Exception as e:
        self.lambda_box_2.setText(msg_error)


    try:
        self.l_lambda_box_2.setText(str(l_of_lambda_2))
    except Exception as e:
        self.l_lambda_box_2.setText(msg_error)



def show_plots(self):
    import microstrip_matching.plot_epsilon_r_graphs as pl
    x1, er1, x2, er2, x4, er4, x6, er6, x8, er8, x10, er10, x12, er12, x16, er16     = pl.calculate_epsilon_r_1()
    x2_2, er2_2, x4_2, er4_2, x6_2, er6_2, x8_2, er8_2, x10_2, er10_2, x12_2, er12_2 = pl.calculate_epsilon_r_2()

    pl.visualize_z0_over_whratio(x1, er1, x2, er2, x4, er4, x6, er6, x8, er8, x10, er10, x12, er12, x16, er16, x2_2, er2_2, x4_2, er4_2, x6_2, er6_2, x8_2, er8_2, x10_2, er10_2, x12_2, er12_2)





def clean_all_microstrip_tab(self):
    self.l_lambda_box.setText("")
    self.z0box.setText("")
    self.epsilon_r_box.setText("")
    self.h_box.setText("")
    self.f_box_3.setText("")
    self.calculate_button_6.click()
    self.l_lambda_box.setFocus()
    
    
