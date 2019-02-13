#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 19 15:38:35 2018

@author(s)   : Francesco Urbani
@file        : Y_tab.py
@descritpion : 

"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import cmath
import math

import Y_functions as Y # import all the functions from Y_functions, used to compute Y related parameters.
from twoport.utils import db as to_dB
from twoport.utils import find_nearest

msg_error = "" # displays nothing if error occurs


def retrieve_Y_parameters(self, f0_):

    # current bjt configuration CE/CB
    if self.radioButton_CE.isChecked():
        self.checkBox.setText("2N4957 (Common Emitter config.)")
        import CE_param_2N4957
        f1, gie, f2, bie, f3, gfe, f4, bfe, f5, goe, f6, boe, f7, gre, f8, bre = CE_param_2N4957.Y_CE_parameters()
        

        # now retrieve data from CE_param_2N4957
        # given f0_ get the closest value to f0_ from the numpy arrays called f* (* from 1 to 8). then get their indices and get
        # eventually get the value from the corresponding numpy array (gie, gfe, etc...)


        # retrieving y_ie
        closest_to_f0_ = find_nearest(f1, f0_)
        ind, = np.where(f1==closest_to_f0_)[0]
        gie_ = gie[ind]
        closest_to_f0_ = find_nearest(f2, f0_)
        ind, = np.where(f2==closest_to_f0_)[0]
        bie_ = bie[ind]
        yi_ = gie_+1j*bie_
        

        # retrieving y_fe
        closest_to_f0_ = find_nearest(f3, f0_)
        ind, = np.where(f3==closest_to_f0_)[0]
        gfe_ = gfe[ind]
        closest_to_f0_ = find_nearest(f4, f0_)
        ind, = np.where(f4==closest_to_f0_)[0]
        bfe_ = -bfe[ind] # SIGN IS NEGATIVE!
        yf_ = gfe_+1j*bfe_
        

        # retrieving y_oe
        closest_to_f0_ = find_nearest(f5, f0_)
        ind, = np.where(f5==closest_to_f0_)[0]
        goe_ = goe[ind]
        closest_to_f0_ = find_nearest(f6, f0_)
        ind, = np.where(f6==closest_to_f0_)[0]
        boe_ = boe[ind]
        yo_ = goe_+1j*boe_
        

        # retrieving y_fe
        closest_to_f0_ = find_nearest(f7, f0_)
        ind, = np.where(f7==closest_to_f0_)[0]
        gre_ = -gre[ind] # SIGN IS NEGATIVE!
        closest_to_f0_ = find_nearest(f8, f0_)
        ind, = np.where(f8==closest_to_f0_)[0]
        bre_ = -bre[ind] # SIGN IS NEGATIVE!
        yr_ = gre_+1j*bre_
        

    else:
        self.checkBox.setText("2N4957 (Common Base config.)")
        import CB_param_2N4957
        f1, gib, f2, bib, f3, gfb, f4, bfb, f5, gob, f6, bob, f7, grb, f8, brb = CB_param_2N4957.Y_CB_parameters_fitted()
        

        # now retrieve data from CB_param_2N4957
        # given f0_ get the closest value to f0_ from the numpy arrays called f* (* from 1 to 8). then get their indices and get
        # eventually get the value from the corresponding numpy array (gib, gfb, etc...)


        # retrieving y_ib
        closest_to_f0_ = find_nearest(f1, f0_)
        ind, = np.where(f1==closest_to_f0_)[0]
        gib_ = gib[ind]
        closest_to_f0_ = find_nearest(f2, f0_)
        ind, = np.where(f2==closest_to_f0_)[0]
        bib_ = -bib[ind] # SIGN IS NEGATIVE!
        yi_ = gib_+1j*bib_
        

        # retrieving y_fe
        closest_to_f0_ = find_nearest(f3, f0_)
        ind, = np.where(f3==closest_to_f0_)[0]
        gfb_ = -gfb[ind] # SIGN IS NEGATIVE!
        closest_to_f0_ = find_nearest(f4, f0_)
        ind, = np.where(f4==closest_to_f0_)[0]
        bfb_ = bfb[ind]
        yf_ = gfb_+1j*bfb_
        

        # retrieving y_oe
        closest_to_f0_ = find_nearest(f5, f0_)
        ind, = np.where(f5==closest_to_f0_)[0]
        gob_ = gob[ind]
        closest_to_f0_ = find_nearest(f6, f0_)
        ind, = np.where(f6==closest_to_f0_)[0]
        bob_ = bob[ind]
        yo_ = gob_+1j*bob_
        

        # retrieving y_fe
        closest_to_f0_ = find_nearest(f7, f0_)
        ind, = np.where(f7==closest_to_f0_)[0]
        grb_ = -grb[ind] # SIGN IS NEGATIVE!
        closest_to_f0_ = find_nearest(f8, f0_)
        ind, = np.where(f8==closest_to_f0_)[0]
        brb_ = -brb[ind] # SIGN IS NEGATIVE!
        yr_ = grb_+1j*brb_

    return yi_, yf_, yo_, yr_







def fill_Y_boxes(self):
    """
    when pressed check f0 and the configuration (whether CE or CB),
    then retrieve the Y parameters and eventually fills the 4 y parameters boxes.
    """

    # change button text according to the selected radioButton:
    if self.radioButton_CE.isChecked():
        self.show_plots_button.setText("Show C.E. Y parameters plots")
        self.label_20.setText("Y<sub>ie</sub>")
        self.label_81.setText("Y<sub>fe</sub>")
        self.label_79.setText("Y<sub>oe</sub>")
        self.label_78.setText("Y<sub>re</sub>")
        self.label_165.setText("V<sub>CE</sub>")
    else:
        self.show_plots_button.setText("Show C.B. Y parameters plots")
        self.label_20.setText("Y<sub>ib</sub>")
        self.label_81.setText("Y<sub>fb</sub>")
        self.label_79.setText("Y<sub>ob</sub>")
        self.label_78.setText("Y<sub>rb</sub>")
        self.label_165.setText("V<sub>CB</sub>")


    # read frequency and check if the range is correct.
    # if not write a feedback into label label_21.

    try:
        f0_ = float(self.f0_box_2.text())
        if f0_ > 1500 or f0_ < 45:
            # frequency out of range
            self.label_21.setText("<font color='red'>Frequency out of range. Enter a frequency within the 45 - 1500 MHz range.</font>")
        else:
            self.label_21.setText("")
    except Exception as e:
        f0_ = 0


    yi_, yf_, yo_, yr_ = retrieve_Y_parameters(self, f0_)
    
    
    if f0_ > 1500 or f0_ < 45:
        self.y_i_box_2.setText("")
        self.y_f_box_2.setText("")
        self.y_o_box_2.setText("")
        self.y_r_box_2.setText("")
    else: 
        self.y_i_box_2.setText(str(yi_))
        self.y_f_box_2.setText(str(yf_))
        self.y_o_box_2.setText(str(yo_))
        self.y_r_box_2.setText(str(yr_))
        # self.f0_box.setText(str(f0_))






def compute_Y_2N4957(self):
    
    # --------------------------------------------------------------------------------
    # actual computation begins here
    # --------------------------------------------------------------------------------

    # read inputs
    try:
        y_i = complex(self.y_i_box_2.text())
    except Exception as e:
        y_i = msg_error
    
    try:
        y_f = complex(self.y_f_box_2.text())
    except Exception as e:
        y_f = msg_error

    try:
        y_r = complex(self.y_r_box_2.text())
    except Exception as e:
        y_r = msg_error

    try:
        y_o = complex(self.y_o_box_2.text())
    except Exception as e:
        y_o = msg_error

    try:
        y_s = complex(self.y_s_box_2.text())
        print ("y_s = " + str(y_s) + " ==> Z_s = " + str((y_s*1e-3)**-1) + " ohm" )
    except Exception as e:
        y_s = msg_error
    
    try:
        y_L = complex(self.y_L_box_2.text())
        print ("y_L = " + str(y_L) + " ==> Z_L = " + str((y_L*1e-3)**-1) + " ohm" )
    except Exception as e:
        y_L = msg_error



    #############################################
    # compute stuff
    #############################################

    # compute C
    global C
    try:
        C = Y.calculate_C(y_i, y_f, y_o, y_r)
    except Exception as e:
        C = msg_error


    # compute betaA
    try:
        betaA  = Y.calculate_betaA(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        betaA = msg_error


    # compute y_in
    try:
        y_in = Y.calculate_y_in(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        y_in = msg_error

    # compute y_out
    try:
        y_out = Y.calculate_y_out(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        y_out = msg_error
    


    # compute A_V (voltage gain)
    try:
        A_V = Y.calculate_A_V(y_f, y_o, y_L)
    except Exception as e:
        A_V = msg_error

    try:
        vout_over_vs = Y.calculate_vout_over_vs(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        vout_over_vs = msg_error


    # compute G_A
    try:
        G_A = Y.calculate_G_A(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        G_A = msg_error

    # compute G_A_dB
    try:
        G_A_dB = to_dB(G_A)
    except Exception as e:
        G_A_dB = msg_error


    # compute G_P
    try:
        G_P = Y.calculate_G_P(y_i, y_f, y_o, y_r, y_s, y_L, y_in)
    except Exception as e:
        G_P = msg_error

    # compute G_P_dB
    try:
        G_P_dB = to_dB(G_P)
    except Exception as e:
        G_P_dB = msg_error


    # computer G_T
    try:
        G_T = Y.calculate_G_T(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        G_T = msg_error

    # compute G_T_dB
    try:
        G_T_dB = to_dB(G_T)
    except Exception as e:
        G_T_dB = msg_error

    
    # compute k
    # i.e. Linvill factor
    # http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=4376096
    try:
        k = Y.calculate_k(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        k = msg_error

    # compute y_s_opt
    global y_s_opt # used by the fill_ys_yl_opt_2N4957 function
    try:
        y_s_opt = Y.calculate_y_s_opt(y_i, y_f, y_o, y_r)
    except Exception as e:
        y_s_opt = msg_error
    

    # compute y_L_opt
    global y_L_opt # used by the fill_ys_yl_opt_2N4957 function
    try:
        y_L_opt = Y.calculate_y_L_opt(y_i, y_f, y_o, y_r)
    except Exception as e:
        y_L_opt = msg_error



    #############################################
    # display stuff
    #############################################

    try:
        if C < 0 or C>1:
            font_color = "red"
            self.Fill_ys_yl_opt_button.setEnabled(False)
        else:
            font_color = "green"
            self.Fill_ys_yl_opt_button.setEnabled(True)
        self.C_box_2.setText("<font color="+font_color+">"+str(C)+"</font>")
    except Exception as e:
        self.C_box_2.setText(str(C))
    
    
    try:
        self.beta_A_box_2.setText(str(abs(betaA)) + "∠" + str(math.degrees(cmath.phase(betaA))) + "°")
        # print ("betaA = " + str(betaA) + " = " + str(cmath.polar(betaA)) )
    except Exception as e:
        self.beta_A_box_2.setText(msg_error)
    

    self.GA_box_2.setText(str(G_A))
    self.GA_box_dB_2.setText(str(G_A_dB))
    self.GT_box_2.setText(str(G_T))
    self.GT_box_dB_2.setText(str(G_T_dB))
    self.GP_box_2.setText(str(G_P))
    self.GP_box_dB_2.setText(str(G_P_dB))

    try:
        self.A_V_box.setText(str(abs(A_V)))
    except Exception as e:
        self.A_V_box.setText(msg_error)

    try:
        self.vout_over_vs_box.setText(str(abs(vout_over_vs)))
    except Exception as e:
        self.vout_over_vs_box.setText(msg_error)

    self.y_out_box_2.setText(str(y_out))
    self.y_in_box_2.setText(str(y_in))
    
    try:
        if k > 1:
            font_color = "green"
        else:
            font_color = "red"
        self.k_box_3.setText("<font color="+font_color+">"+str(k)+"</font>")
    except Exception as e:
        self.k_box_3.setText(msg_error)
    

    try:
        if C < 0 or C > 1 :
            self.y_s_opt_box_2.setText("<i><font color=#909090>Undefined, since the system is potentially unstable.</font></i>")
            self.y_L_opt_box_2.setText("<i><font color=#909090>Undefined, since the system is potentially unstable.</font></i>")                
        else:
            self.y_s_opt_box_2.setText(str(y_s_opt))
            self.y_L_opt_box_2.setText(str(y_L_opt))
        
    except Exception as e:
        self.y_s_opt_box_2.setText(str(y_s_opt))
        self.y_L_opt_box_2.setText(str(y_L_opt))


    # writing the label
    status=""
    self.text_2.setText(msg_error)
    try:
        if (C < 0 or C>1):
            status = "Potentially unstable system"
            color  = 'red'
            self.text_2.setText("<i><font color="+color+">"+status+"</font></i>")
    except Exception as e:
        pass
    try:
        if (C > 0 and C<1):
            status = "Unconditionally stable system"
            color  = 'green'
            self.text_2.setText("<i><font color="+color+">"+status+"</font></i>")
    except Exception as e:
        pass
    try:
        if C==1:
            status = "Marginally stable system"
            color  = 'orange'
            self.text_2.setText("<i><font color="+color+">"+status+"</font></i>")
    except Exception as e:
        pass


    try:
        if (C < 0 or C>=1) and k > 1:
            status = "Stable system"
            color  = 'green'
            self.text_2.setText("<font color="+color+">"+status+"</font>")
    except Exception as e:
        pass
    try:
        if (C < 0 or C>=1) and k < 1:
            status = "Unstable system"
            color  = 'red'
            self.text_2.setText("<font color="+color+">"+status+"</font>")
    except Exception as e:
        pass
    try:
        if (C > 0 and C<1) and k>0: # regardless of wheter k<1 or k>1
            status = "Stable system"
            color  = 'green'
            self.text_2.setText("<font color="+color+">"+status+"</font>")
    except Exception as e:
        pass

    # --------------------------------------------------------------------------------


def show_plot_Y_parameters(self):
    if self.radioButton_CE.isChecked():
        import CE_param_2N4957
        f1, gie, f2, bie, f3, gfe, f4, bfe, f5, goe, f6, boe, f7, gre, f8, bre = CE_param_2N4957.Y_CE_parameters_fitted()
        CE_param_2N4957.visualize_CE_plot(f1, gie, f2, bie, f3, gfe, f4, bfe, f5, goe, f6, boe, f7, gre, f8, bre)
    else:
        import CB_param_2N4957
        f1, gib, f2, bib, f3, gfb, f4, bfb, f5, gob, f6, bob, f7, grb, f8, brb = CB_param_2N4957.Y_CB_parameters_fitted()
        CB_param_2N4957.visualize_CB_plot(f1, gib, f2, bib, f3, gfb, f4, bfb, f5, gob, f6, bob, f7, grb, f8, brb)


def fill_ys_yl_opt_2N4957(self):
    try:
        if C > 0 and C < 1: # if it is stable
            self.y_s_box_2.setText(str(y_s_opt))
            self.y_L_box_2.setText(str(y_L_opt))
            self.Calculate_button_4.click()     
    except Exception as e:
        pass


def open_datasheet_Y(self):
    try:
        if sys.platform == "linux":
            os.system("xdg-open 2N4957/2N4957.pdf")
        elif sys.platform == "darwin":
            os.system("open 2N4957/2N4957.pdf")
        elif sys.platform[:3] == "win":
            os.system('start "" "2N4957/2N4957.pdf"')
    except Exception as e:
        print ("Can't open the datasheet.")




""" plots Linvill value C with respect to the frequency of operation f0 """
def plot_C_vs_f(self):


    fig, ax = plt.subplots()

    
    freq_list = np.linspace(45, 1500, 800)
    yi_list = []
    yf_list = []
    yo_list = []
    yr_list = []

    C_list  = []


    for freq in freq_list:
        yi_, yf_, yo_, yr_ = retrieve_Y_parameters(self, freq)
        
        C = Y.calculate_C(yi_, yf_, yo_, yr_)
        C_list.append(C)



    # current bjt configuration CE/CB
    if self.radioButton_CE.isChecked():
        plt.ylim(0, 4.5)
    else:
        plt.ylim(-8, 8)

    
    

    
    ax.plot(freq_list, C_list, label="$C(f)$")


    # plot unconditionally stable area
    ax.axhspan(0, 1, alpha=0.1, color='green', label="Unconditionally stable area")

    

    plt.grid(True,which="both",ls="-")
    plt.xlim(45, 1500)

    plt.xscale('log')
    plt.legend()
    plt.xlabel("$f\ (Hz)$")

    plt.suptitle("$C(f)$")
    # C(f) = \frac{|y_R y_F|}{2 \mathbb{R}e\{y_i\} \mathbb{R}e\{y_o\} - \mathbb{R}e \{y_r y_f\}}
    plt.show()
    




def clean_Y_2N4957(self):
    self.y_s_box_2.setText("")
    self.y_L_box_2.setText("")
    self.Calculate_button_4.click()
    self.y_s_box_2.setFocus()


def clean_all_Y_2N4957(self):
    self.f0_box_2.setText("")
    self.C_box_2.setText("")
    self.beta_A_box_2.setText("")
    self.A_V_box.setText("")
    self.vout_over_vs_box.setText("")
    self.GA_box_2.setText("")
    self.GA_box_dB_2.setText("")
    self.GT_box_2.setText("")
    self.GT_box_dB_2.setText("")
    self.GP_box_2.setText("")
    self.GP_box_dB_2.setText("")
    self.y_in_box_2.setText("")
    self.y_out_box_2.setText("")
    self.k_box_3.setText("")
    self.y_L_opt_box_2.setText("")
    self.y_s_opt_box_2.setText("")
    self.y_s_box_2.setText("")
    self.y_L_box_2.setText("")
    self.y_i_box_2.setText("")
    self.y_f_box_2.setText("")
    self.y_o_box_2.setText("")
    self.y_r_box_2.setText("")
    self.Calculate_button_4.click()
    self.f0_box_2.setFocus()


