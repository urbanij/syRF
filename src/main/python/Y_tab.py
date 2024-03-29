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
import pandas as pd
import matplotlib.pyplot as plt
import cmath
import math

import Y_functions as Y  # import all the functions from Y_functions, used to compute Y related parameters.
from twoport.utils import db as to_dB
from twoport.utils import find_nearest

msg_error = ""  # displays nothing if error occurs


def retrieve_Y_parameters(self, f0_):

    # current bjt configuration CE/CB
    if self.radioButton_CE.isChecked():
        self.radiobutton_2n4957.setText("2N4957 (Common Emitter config.)")
        import CE_param_2N4957

        (
            f1,
            gie,
            f2,
            bie,
            f3,
            gfe,
            f4,
            bfe,
            f5,
            goe,
            f6,
            boe,
            f7,
            gre,
            f8,
            bre,
        ) = CE_param_2N4957.Y_CE_parameters()

        # now retrieve data from CE_param_2N4957
        # given f0_ get the closest value to f0_ from the numpy arrays called f* (* from 1 to 8). then get their indices and get
        # eventually get the value from the corresponding numpy array (gie, gfe, etc...)

        # retrieving y_ie
        closest_to_f0_ = find_nearest(f1, f0_)
        (ind,) = np.where(f1 == closest_to_f0_)[0]
        gie_ = gie[ind]
        closest_to_f0_ = find_nearest(f2, f0_)
        (ind,) = np.where(f2 == closest_to_f0_)[0]
        bie_ = bie[ind]
        yi_ = gie_ + 1j * bie_

        # retrieving y_fe
        closest_to_f0_ = find_nearest(f3, f0_)
        (ind,) = np.where(f3 == closest_to_f0_)[0]
        gfe_ = gfe[ind]
        closest_to_f0_ = find_nearest(f4, f0_)
        (ind,) = np.where(f4 == closest_to_f0_)[0]
        bfe_ = -bfe[ind]  # SIGN IS NEGATIVE!
        yf_ = gfe_ + 1j * bfe_

        # retrieving y_oe
        closest_to_f0_ = find_nearest(f5, f0_)
        (ind,) = np.where(f5 == closest_to_f0_)[0]
        goe_ = goe[ind]
        closest_to_f0_ = find_nearest(f6, f0_)
        (ind,) = np.where(f6 == closest_to_f0_)[0]
        boe_ = boe[ind]
        yo_ = goe_ + 1j * boe_

        # retrieving y_fe
        closest_to_f0_ = find_nearest(f7, f0_)
        (ind,) = np.where(f7 == closest_to_f0_)[0]
        gre_ = -gre[ind]  # SIGN IS NEGATIVE!
        closest_to_f0_ = find_nearest(f8, f0_)
        (ind,) = np.where(f8 == closest_to_f0_)[0]
        bre_ = -bre[ind]  # SIGN IS NEGATIVE!
        yr_ = gre_ + 1j * bre_

    else:
        self.radiobutton_2n4957.setText("2N4957 (Common Base config.)")
        import CB_param_2N4957

        (
            f1,
            gib,
            f2,
            bib,
            f3,
            gfb,
            f4,
            bfb,
            f5,
            gob,
            f6,
            bob,
            f7,
            grb,
            f8,
            brb,
        ) = CB_param_2N4957.Y_CB_parameters_fitted()

        # now retrieve data from CB_param_2N4957
        # given f0_ get the closest value to f0_ from the numpy arrays called f* (* from 1 to 8). then get their indices and get
        # eventually get the value from the corresponding numpy array (gib, gfb, etc...)

        # retrieving y_ib
        closest_to_f0_ = find_nearest(f1, f0_)
        (ind,) = np.where(f1 == closest_to_f0_)[0]
        gib_ = gib[ind]
        closest_to_f0_ = find_nearest(f2, f0_)
        (ind,) = np.where(f2 == closest_to_f0_)[0]
        bib_ = -bib[ind]  # SIGN IS NEGATIVE!
        yi_ = gib_ + 1j * bib_

        # retrieving y_fe
        closest_to_f0_ = find_nearest(f3, f0_)
        (ind,) = np.where(f3 == closest_to_f0_)[0]
        gfb_ = -gfb[ind]  # SIGN IS NEGATIVE!
        closest_to_f0_ = find_nearest(f4, f0_)
        (ind,) = np.where(f4 == closest_to_f0_)[0]
        bfb_ = bfb[ind]
        yf_ = gfb_ + 1j * bfb_

        # retrieving y_oe
        closest_to_f0_ = find_nearest(f5, f0_)
        (ind,) = np.where(f5 == closest_to_f0_)[0]
        gob_ = gob[ind]
        closest_to_f0_ = find_nearest(f6, f0_)
        (ind,) = np.where(f6 == closest_to_f0_)[0]
        bob_ = bob[ind]
        yo_ = gob_ + 1j * bob_

        # retrieving y_fe
        closest_to_f0_ = find_nearest(f7, f0_)
        (ind,) = np.where(f7 == closest_to_f0_)[0]
        grb_ = -grb[ind]  # SIGN IS NEGATIVE!
        closest_to_f0_ = find_nearest(f8, f0_)
        (ind,) = np.where(f8 == closest_to_f0_)[0]
        brb_ = -brb[ind]  # SIGN IS NEGATIVE!
        yr_ = grb_ + 1j * brb_

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
            self.statusBar.showMessage(
                "Frequency out of range. Enter a frequency within the 45 - 1500 MHz range."
            )
            self.statusBar.setStyleSheet("background-color: red; color: white;")
            # self.statusBar.setStyleSheet("color: red;")
        else:
            self.statusBar.showMessage("")
            self.statusBar.setStyleSheet("background-color: auto;")
            # self.statusBar.setStyleSheet("color: auto;")

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
    except ValueError as e:
        y_i = msg_error

    try:
        y_f = complex(self.y_f_box_2.text())
    except ValueError as e:
        y_f = msg_error

    try:
        y_r = complex(self.y_r_box_2.text())
    except ValueError as e:
        y_r = msg_error

    try:
        y_o = complex(self.y_o_box_2.text())
    except ValueError as e:
        y_o = msg_error

    try:
        y_s = complex(self.y_s_box_2.text())
        if y_s != 0:
            print(
                "y_s = " + str(y_s) + " ==> Z_s = " + str((y_s * 1e-3) ** -1) + " ohm"
            )
        elif y_s == 0:
            print("y_s = " + str(y_s) + " ==> Z_s = +inf ohm")
    except ValueError as e:
        y_s = msg_error

    try:
        y_L = complex(self.y_L_box_2.text())
        if y_L != 0:
            print(
                "y_L = " + str(y_L) + " ==> Z_L = " + str((y_L * 1e-3) ** -1) + " ohm"
            )
        elif y_L == 0:
            print("y_L = " + str(y_s) + " ==> Z_L = +inf ohm")
    except ValueError as e:
        y_L = msg_error

    #############################################
    # compute stuff
    #############################################

    # compute C
    global C
    try:
        C = Y.calculate_C(y_i=y_i, y_f=y_f, y_o=y_o, y_r=y_r)
    except Exception as e:
        C = msg_error

    # compute betaA
    try:
        betaA = Y.calculate_betaA(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        betaA = msg_error

    # compute y_in
    try:
        y_in = Y.calculate_y_in(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        y_in = msg_error

    # compute y_out
    try:
        y_out = Y.calculate_y_out(y_i, y_f, y_o, y_r, y_s, y_L)
    except Exception as e:
        y_out = msg_error

    # compute A_V (voltage gain)
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
    global y_s_opt  # used by the fill_ys_yl_opt_2N4957 function
    try:
        y_s_opt = Y.calculate_y_s_opt(y_i, y_f, y_o, y_r)
    except Exception as e:
        y_s_opt = msg_error

    # compute y_L_opt
    global y_L_opt  # used by the fill_ys_yl_opt_2N4957 function
    try:
        y_L_opt = Y.calculate_y_L_opt(y_i, y_f, y_o, y_r)
    except Exception as e:
        y_L_opt = msg_error

    #############################################
    # display stuff
    #############################################

    try:
        if C < 0 or C > 1:
            self.C_box_2.setStyleSheet("color: red")
            self.Fill_ys_yl_opt_button.setEnabled(False)
        else:
            self.C_box_2.setStyleSheet("color: green")
            self.Fill_ys_yl_opt_button.setEnabled(True)
    except:
        pass

    try:
        self.C_box_2.setText("{:.6g}".format(C))
    except:
        self.C_box_2.setText(msg_error)

    try:
        self.beta_A_box_2.setText(
            "{:.6g}∠{:.6g} deg".format(abs(betaA), math.degrees(cmath.phase(betaA)))
        )
    except Exception as e:
        self.beta_A_box_2.setText(msg_error)

    try:
        self.GA_box_2.setText("{:.6g}".format(G_A))
    except:
        self.GA_box_2.setText(msg_error)
    try:
        self.GA_box_dB_2.setText("{:.6g}".format(G_A_dB))
    except:
        self.GA_box_dB_2.setText(msg_error)
    try:
        self.GT_box_2.setText("{:.6g}".format(G_T))
    except:
        self.GT_box_2.setText(msg_error)
    try:
        self.GT_box_dB_2.setText("{:.6g}".format(G_T_dB))
    except:
        self.GT_box_dB_2.setText(msg_error)
    try:
        self.GP_box_2.setText("{:.6g}".format(G_P))
    except:
        self.GP_box_2.setText(msg_error)
    try:
        self.GP_box_dB_2.setText("{:.6g}".format(G_P_dB))
    except:
        self.GP_box_dB_2.setText(msg_error)
    try:
        self.A_V_box.setText("{:.6g}".format(abs(A_V)))
    except Exception as e:
        self.A_V_box.setText(msg_error)
    try:
        self.vout_over_vs_box.setText("{:.6g}".format(abs(vout_over_vs)))
    except Exception as e:
        self.vout_over_vs_box.setText(msg_error)

    try:
        self.y_out_box_2.setText("{:.6g}".format(y_out))
    except:
        self.y_out_box_2.setText(msg_error)
    try:
        self.y_in_box_2.setText("{:.6g}".format(y_in))
    except:
        self.y_in_box_2.setText(msg_error)

    try:
        if k > 1:
            self.k_box_3.setStyleSheet("color: green")
        else:
            self.k_box_3.setStyleSheet("color: red")
        self.k_box_3.setText("{:.6g}".format(k))
    except Exception as e:
        self.k_box_3.setText(msg_error)

    try:
        if C < 0 or C > 1:
            self.y_s_opt_box_2.setStyleSheet("color: #909090")
            self.y_s_opt_box_2.setText("Undefined -- potentially unstable")

            self.y_L_opt_box_2.setStyleSheet("color: #909090")
            self.y_L_opt_box_2.setText("Undefined -- potentially unstable")
        else:

            self.y_s_opt_box_2.setStyleSheet("color: black")
            self.y_L_opt_box_2.setStyleSheet("color: black")
            self.y_s_opt_box_2.setText("{:.6g}".format(y_s_opt))
            self.y_L_opt_box_2.setText("{:.6g}".format(y_L_opt))

    except Exception as e:
        self.y_s_opt_box_2.setText(str(y_s_opt))
        self.y_L_opt_box_2.setText(str(y_L_opt))

    # writing the label
    status = ""
    self.text_2.setText(msg_error)
    try:
        if C < 0 or C > 1:
            status = "Potentially unstable system"
            color = "red"
            self.text_2.setText(
                "<i><font color=" + color + ">" + status + "</font></i>"
            )
    except Exception as e:
        print(e)
        pass

    try:
        if C > 0 and C < 1:
            status = "Unconditionally stable system"
            color = "green"
            self.text_2.setText(
                "<i><font color=" + color + ">" + status + "</font></i>"
            )
    except Exception as e:
        pass

    try:
        if C == 1:
            status = "Marginally stable system"
            color = "orange"
            self.text_2.setText(
                "<i><font color=" + color + ">" + status + "</font></i>"
            )
    except Exception as e:
        pass

    try:
        if (C < 0 or C >= 1) and k > 1:
            status = "Stable system"
            color = "green"
            self.text_2.setText("<font color=" + color + ">" + status + "</font>")
    except Exception as e:
        pass

    try:
        if (C < 0 or C >= 1) and k < 1:
            status = "Unstable system"
            color = "red"
            self.text_2.setText("<font color=" + color + ">" + status + "</font>")
    except Exception as e:
        pass

    try:
        if (C > 0 and C < 1) and k > 0:  # regardless of wheter k<1 or k>1
            status = "Stable system"
            color = "green"
            self.text_2.setText("<font color=" + color + ">" + status + "</font>")
    except Exception as e:
        pass

    # --------------------------------------------------------------------------------


def show_plot_Y_parameters(self):
    if self.radioButton_CE.isChecked():
        import CE_param_2N4957

        (
            f1,
            gie,
            f2,
            bie,
            f3,
            gfe,
            f4,
            bfe,
            f5,
            goe,
            f6,
            boe,
            f7,
            gre,
            f8,
            bre,
        ) = CE_param_2N4957.Y_CE_parameters_fitted()
        CE_param_2N4957.visualize_CE_plot(
            f1, gie, f2, bie, f3, gfe, f4, bfe, f5, goe, f6, boe, f7, gre, f8, bre
        )
    else:
        import CB_param_2N4957

        (
            f1,
            gib,
            f2,
            bib,
            f3,
            gfb,
            f4,
            bfb,
            f5,
            gob,
            f6,
            bob,
            f7,
            grb,
            f8,
            brb,
        ) = CB_param_2N4957.Y_CB_parameters_fitted()
        CB_param_2N4957.visualize_CB_plot(
            f1, gib, f2, bib, f3, gfb, f4, bfb, f5, gob, f6, bob, f7, grb, f8, brb
        )


def fill_ys_yl_opt_2N4957(self):
    try:
        if C > 0 and C < 1:  # if it is stable
            self.y_s_box_2.setText(str(y_s_opt))
            self.y_L_box_2.setText(str(y_L_opt))
            self.Calculate_button_4.click()
    except Exception as e:
        pass


""" plots Linvill value C with respect to the frequency of operation f0 """


def plot_C_vs_f(self):

    fig, ax = plt.subplots(figsize=(10, 8))

    freq_list = np.linspace(45, 1500, 800)

    """
    ### retrieve Linvil data:
    yi_list = []
    yf_list = []
    yo_list = []
    yr_list = []

    C_list  = []

    for freq in freq_list:
        yi_, yf_, yo_, yr_ = retrieve_Y_parameters(self, freq)
        
        C = Y.calculate_C(y_i=yi_, y_f=yf_, y_o=yo_, y_r=yr_)
        C_list.append(C)
    print(C_list)
    """

    C_common_emit = np.array(
        [
            3.581760396693358,
            3.3682647072668632,
            3.2738153475265834,
            3.525268537103796,
            3.285958820274154,
            2.850274697937659,
            3.14652689960125,
            3.2693574446691334,
            3.050114488507493,
            3.8740696190310207,
            3.6968382719879815,
            4.028097019261114,
            3.897677234782995,
            3.6523679981519837,
            3.078808900793946,
            3.0887134366433955,
            3.0893145351516185,
            3.164247478363306,
            2.9548812640162305,
            2.6484752294745944,
            3.139702286297088,
            3.2067536030836834,
            3.295456144559025,
            3.1436307211948433,
            3.127729623068714,
            3.235028776587059,
            3.3044059940150583,
            3.5626418189828684,
            3.5746060661053725,
            3.180984783237298,
            2.9755660219302,
            3.843127071472861,
            4.2138945644954475,
            4.042789323996015,
            4.023646124026304,
            3.947599475173467,
            3.9186182714072912,
            3.8465965515708125,
            3.815478139975696,
            3.8106890534373257,
            3.798667500945467,
            3.72623756922963,
            3.682107136750575,
            3.6627021929890304,
            3.625428011689745,
            3.6203416304481597,
            3.5910171270961864,
            3.528804329237906,
            3.499610066010452,
            3.483770589892,
            3.4116318929251044,
            3.3758696245505684,
            3.369091125723778,
            3.302680744316544,
            3.246448142288365,
            3.277877035374978,
            3.0021161614039826,
            2.5693142703954868,
            2.5592593953968454,
            2.884972650176174,
            2.8149683622019768,
            2.8735271344691213,
            2.8256998469236914,
            2.782519259810127,
            2.7608620504707506,
            2.731253655749891,
            2.657532584629209,
            2.6324704620650548,
            2.604962634744964,
            2.599138130850828,
            2.559936710325902,
            2.563604018744263,
            2.518036618900107,
            2.4838360774032395,
            2.46732410762516,
            2.381255045862401,
            2.3768189104113984,
            2.3483909511858316,
            2.338201838894509,
            2.3631580202467233,
            2.3709765890642562,
            2.4750574084884223,
            2.489554330917601,
            2.446710321670622,
            2.415138308937269,
            2.3072481753123624,
            2.306937707709376,
            2.3172048626131843,
            2.3291486249798234,
            2.241912368376072,
            2.2324594466943903,
            2.207613347777693,
            2.2002002617703287,
            2.170037799185914,
            2.157953712174966,
            2.1331397416629554,
            2.12723102675603,
            2.168831321448635,
            2.1366734360382447,
            2.1252955693497917,
            2.101225707108361,
            2.0928791941508886,
            2.0641239889610863,
            2.0523698046901964,
            2.046009177794086,
            2.0381952854238596,
            2.03204085295567,
            1.9854556451057797,
            1.9854556451057797,
            1.9575521213961842,
            1.9353174814710308,
            1.8950500024612211,
            1.8964098960570142,
            1.901283800709126,
            1.849785114638603,
            1.844591697250946,
            1.8219147794634762,
            1.8589350226338501,
            1.8369837460817546,
            1.809427129545463,
            1.8114028153032757,
            1.8023808526464589,
            1.789378167672486,
            1.7959243003890433,
            1.7535001870942184,
            1.7538514219215202,
            1.7840710404752524,
            1.7493424734483678,
            1.742848989136608,
            1.7526289610800356,
            1.733488867447689,
            1.6937256322825607,
            1.6817181872371751,
            1.6737466333022815,
            1.6720764039992932,
            1.6554154726621417,
            1.6712371624359192,
            1.6867934863892948,
            1.6695128176981113,
            1.6209862254544256,
            1.6014200014245998,
            1.5858361610334952,
            1.5937991689850586,
            1.5760168596575184,
            1.5688763054256347,
            1.6028154599633262,
            1.587409737976144,
            1.5714906053613473,
            1.5588425291033374,
            1.5589562026319506,
            1.5523781777850811,
            1.5523781777850811,
            1.531733911328782,
            1.522682849608765,
            1.522682849608765,
            1.505827559866074,
            1.504982870250955,
            1.504982870250955,
            1.4824290226480736,
            1.4822021030179504,
            1.4822021030179504,
            1.4760105146452465,
            1.4635044522872167,
            1.456906110155428,
            1.456906110155428,
            1.4457596343936094,
            1.4391532352129948,
            1.4412849356910027,
            1.4412849356910027,
            1.4195681427229547,
            1.4214715622659713,
            1.4214715622659713,
            1.4073717162549138,
            1.4083978800704904,
            1.4083978800704904,
            1.391506357082072,
            1.380898620899318,
            1.3825140685538801,
            1.3825140685538801,
            1.3740511677263887,
            1.3648465578305145,
            1.3666312978510375,
            1.3612051492608956,
            1.3543118634732312,
            1.3522811278490776,
            1.3448263676430798,
            1.3448263676430798,
            1.3271570119724971,
            1.3202298011078168,
            1.3219358480682613,
            1.3219358480682613,
            1.303036233230029,
            1.3002848910051257,
            1.2889716983546284,
            1.2889716983546284,
            1.2641000800854512,
            1.2614026368624034,
            1.2577915721603738,
            1.284013210399591,
            1.28037869677294,
            1.271393182832246,
            1.2687594587201472,
            1.2549136910610612,
            1.251674964255853,
            1.2426331669692299,
            1.2434967938627366,
            1.243163328842244,
            1.237351593232025,
            1.237351593232025,
            1.2352599933755293,
            1.2313625214398911,
            1.2227720996902953,
            1.2227720996902953,
            1.2227720996902953,
            1.2133143661471302,
            1.2114364346630633,
            1.2114364346630633,
            1.2114364346630633,
            1.2015628263349742,
            1.2047253769593163,
            1.2047253769593163,
            1.2047253769593163,
            1.2004798926191267,
            1.1993283711333818,
            1.1989994788696219,
            1.1909473789380443,
            1.1909473789380443,
            1.18641593025958,
            1.1830616684046105,
            1.1814270433909964,
            1.1814270433909964,
            1.1814270433909964,
            1.1729835460712463,
            1.1715107459005243,
            1.1689682185152448,
            1.1689682185152448,
            1.1633817554345809,
            1.1621435559634177,
            1.1589026899896546,
            1.1515456771970598,
            1.1515456771970598,
            1.1494446699100966,
            1.1526958956337139,
            1.145600880967925,
            1.145600880967925,
            1.145600880967925,
            1.1337191868438068,
            1.1356185540787305,
            1.1153488801659794,
            1.1153488801659794,
            1.1147471763852967,
            1.1121303380896557,
            1.1126806959970756,
            1.1143786301234881,
            1.1143786301234881,
            1.1143786301234881,
            1.1191571617961837,
            1.1191571617961837,
            1.1184466421681654,
            1.1080019571037858,
            1.109335279482943,
            1.109335279482943,
            1.1022058662866419,
            1.100082077560076,
            1.100082077560076,
            1.101624982472916,
            1.101624982472916,
            1.0936842962812445,
            1.0856543190596957,
            1.0856543190596957,
            1.0843404336237996,
            1.07937475015571,
            1.07937475015571,
            1.077924104600533,
            1.0758043099786698,
            1.07306839877879,
            1.0724553860728476,
            1.0724553860728476,
            1.065316899426883,
            1.0651608090923026,
            1.0651608090923026,
            1.0598284595950416,
            1.061762621408322,
            1.061762621408322,
            1.0609119797665205,
            1.0543998926233746,
            1.0543998926233746,
            1.052060666820404,
            1.0540070469927925,
            1.0504596875904366,
            1.0499488591012165,
            1.0435101682311345,
            1.0435101682311345,
            1.0347418423787038,
            1.0368028688158446,
            1.0363670631846613,
            1.033111811685525,
            1.0323968297660366,
            1.0323968297660366,
            1.029817790038866,
            1.03163187167715,
            1.0262521402944775,
            1.0262521402944775,
            1.037239043569299,
            1.034750480038935,
            1.026291166780666,
            1.0282286257077942,
            1.0279485729668802,
            1.0279485729668802,
            1.0157415094432996,
            1.0120469851450322,
            1.0120469851450322,
            1.0141725703158584,
            1.0084125325109543,
            1.0062253996649382,
            1.0064754770898579,
            1.0064754770898579,
            1.0048885591042445,
            1.0049311836458021,
            1.0049311836458021,
            1.0048925573237444,
            0.9858783865696538,
            0.9856493639668272,
            0.9835179043999183,
            0.9858528071613941,
            0.9831995278052438,
            0.9832368608585401,
            0.9832368608585401,
            0.9744582371906679,
            0.9744582371906679,
            0.9744582371906679,
            0.9777545158439871,
            0.9777545158439871,
            0.9777973364485157,
            0.9764648053655703,
            0.9769982142998009,
            0.9740892983594005,
            0.9716487829715145,
            0.9716487829715145,
            0.9719790012916358,
            0.9684677783201178,
            0.9658525979629814,
            0.9658525979629814,
            0.9643934747277165,
            0.9643934747277165,
            0.9613000254857981,
            0.9541484567556034,
            0.9564617105118544,
            0.9483184036888546,
            0.9483184036888546,
            0.9483184036888546,
            0.9459807178070595,
            0.9459807178070595,
            0.9428676020467022,
            0.9451910344566091,
            0.9474080842600919,
            0.9413273020468473,
            0.9413273020468473,
            0.9413273020468473,
            0.9413273020468473,
            0.9381018827077588,
            0.9381155464035216,
            0.9378204537096392,
            0.9378204537096392,
            0.9377948415440603,
            0.9333371735868684,
            0.9321421908841635,
            0.9321421908841635,
            0.930513923398701,
            0.9320741935624369,
            0.9307294064996576,
            0.9307294064996576,
            0.9307294064996576,
            0.9186119674745438,
            0.9186119674745438,
            0.9145694801619976,
            0.9171816167027912,
            0.918438376584708,
            0.9165255094802057,
            0.9128798560576036,
            0.9156908354414147,
            0.9156908354414147,
            0.9155948458068225,
            0.9155948458068225,
            0.9159300998941066,
            0.9133167930851811,
            0.9133167930851811,
            0.9133167930851811,
            0.9106396336597118,
            0.9067998304637594,
            0.9066999767288896,
            0.9088844164197121,
            0.9084645858324357,
            0.9084645858324357,
            0.9054999315332151,
            0.9021969731528707,
            0.9021969731528707,
            0.9021969731528707,
            0.9020757141083364,
            0.9043631134812075,
            0.9019217846522013,
            0.9019217846522013,
            0.9019217846522013,
            0.8969741708219693,
            0.8969741708219693,
            0.8936552390516306,
            0.8892869442966376,
            0.8918021219145441,
            0.8912029856287152,
            0.8902888601461924,
            0.8902888601461924,
            0.8830438974241815,
            0.8830438974241815,
            0.882305446450043,
            0.8796247446795844,
            0.8797316993139928,
            0.877310356554736,
            0.877310356554736,
            0.877310356554736,
            0.877310356554736,
            0.8737860740186194,
            0.8734951010643319,
            0.8712912217244609,
            0.8747968752264472,
            0.8755316893847782,
            0.8755316893847782,
            0.8718512401430601,
            0.8695342563508608,
            0.8638700778312576,
            0.8638700778312576,
            0.8657973791575891,
            0.8630772425723167,
            0.8630772425723167,
            0.8623952183370316,
            0.8623952183370316,
            0.8623952183370316,
            0.8591451298492515,
            0.8568231764828802,
            0.8588205000355865,
            0.8583021050947894,
            0.8583021050947894,
            0.857766406442362,
            0.8555558794612516,
            0.852820931251693,
            0.852820931251693,
            0.8436827736462736,
            0.8417670633567641,
            0.8454912561193244,
            0.8447384956238069,
            0.8447384956238069,
            0.8419552675682468,
            0.8399797100462343,
            0.8399797100462343,
            0.8399797100462343,
            0.8365749598253308,
            0.8365749598253308,
            0.8379976754215963,
            0.8345808691427449,
            0.8345808691427449,
            0.8340771769091693,
            0.8340771769091693,
            0.8340771769091693,
            0.8317800299944491,
            0.824631057883224,
            0.824631057883224,
            0.8259669376669866,
            0.8259669376669866,
            0.8259669376669866,
            0.822842761436336,
            0.8208497279496285,
            0.8208497279496285,
            0.8254048457414344,
            0.8254048457414344,
            0.8273572371193101,
            0.8273572371193101,
            0.8273572371193101,
            0.8233419601482341,
            0.821596330336712,
            0.8236792606271903,
            0.8236792606271903,
            0.8236792606271903,
            0.8099111025396509,
            0.8092395524274462,
            0.8079892277847164,
            0.8073716232325607,
            0.8073716232325607,
            0.8071824946216175,
            0.8071824946216175,
            0.8071824946216175,
            0.806365711908974,
            0.7985669493260785,
            0.7985669493260785,
            0.7985669493260785,
            0.7991506766283245,
            0.7991506766283245,
            0.7989513824993749,
            0.7992165004777133,
            0.7986687387498421,
            0.7979693791113865,
            0.7958098844419272,
            0.7883797049776387,
            0.7883797049776387,
            0.7883797049776387,
            0.7893007183275987,
            0.7886811616344317,
            0.7886178989591345,
            0.7877639388459771,
            0.7877639388459771,
            0.7877639388459771,
            0.7875407369914417,
            0.7780782964087526,
            0.7780782964087526,
            0.7780782964087526,
            0.7812356011902767,
            0.7812356011902767,
            0.7796036857915084,
            0.7773692072952328,
            0.7771478847807769,
            0.7771478847807769,
            0.7771478847807769,
            0.7608756688362285,
            0.7608756688362285,
            0.7598988544836379,
            0.7630325869883531,
            0.7630036492194381,
            0.7633122551454882,
            0.7633122551454882,
            0.7633122551454882,
            0.7633122551454882,
            0.7633122551454882,
            0.7567711471569373,
            0.7573901546403725,
            0.7573901546403725,
            0.7573901546403725,
            0.7573901546403725,
            0.7573901546403725,
            0.7576827493815541,
            0.7511268440712822,
            0.7511268440712822,
            0.7511268440712822,
            0.7546743139522785,
            0.7416313898036916,
            0.7428174968277433,
            0.7428174968277433,
            0.7428174968277433,
            0.7437620532603201,
            0.7442509120183006,
            0.7442509120183006,
            0.7418774685186308,
            0.7406128942937983,
            0.7435376002238328,
            0.7435376002238328,
            0.7286530230813903,
            0.7286530230813903,
            0.7286530230813903,
            0.7291151761562694,
            0.7272984311316196,
            0.7256329212743218,
            0.7256329212743218,
            0.7256329212743218,
            0.7286927743584665,
            0.7286927743584665,
            0.7173249123298759,
            0.7173249123298759,
            0.7161429130475053,
            0.7161429130475053,
            0.7174868801239335,
            0.7152320371358157,
            0.7161172514556949,
            0.7174060403736184,
            0.7174060403736184,
            0.7174060403736184,
            0.7174060403736184,
            0.706983746043,
            0.7047485074310831,
            0.7081803673625883,
            0.7081803673625883,
            0.7081803673625883,
            0.7066485934789826,
            0.7076026148751596,
            0.709405179869266,
            0.7115427965520964,
            0.7115427965520964,
            0.7115427965520964,
            0.702851242979343,
            0.702851242979343,
            0.702851242979343,
            0.7011727519147898,
            0.7011727519147898,
            0.7011727519147898,
            0.7024714109771194,
            0.705830627368773,
            0.705830627368773,
            0.705830627368773,
            0.7062360389367273,
            0.7062360389367273,
            0.6910237172204085,
            0.6910237172204085,
            0.6910237172204085,
            0.6910237172204085,
            0.6910237172204085,
            0.6941960174285797,
            0.6978808960183971,
            0.6978808960183971,
            0.6954240292857364,
            0.6954240292857364,
            0.6954240292857364,
            0.688412039543875,
            0.688412039543875,
            0.688412039543875,
            0.692386967353577,
            0.692386967353577,
            0.695437732232956,
            0.6970085154443909,
            0.6970085154443909,
            0.6944932054276595,
            0.6944932054276595,
            0.6944932054276595,
            0.6944932054276595,
            0.6826552891486044,
            0.6826552891486044,
            0.6826552891486044,
            0.6826552891486044,
            0.6864176576324577,
            0.6864176576324577,
            0.6863498963357926,
            0.6863498963357926,
            0.6863498963357926,
            0.6863498963357926,
            0.6891789660539612,
            0.6891789660539612,
            0.6731826882626538,
            0.6731826882626538,
            0.6770682958792651,
            0.6770682958792651,
            0.6741370877298326,
            0.6741370877298326,
            0.6741370877298326,
            0.6796072388703637,
            0.6796072388703637,
            0.6796072388703637,
            0.6796072388703637,
            0.6796072388703637,
            0.662344771045622,
            0.6671527232519284,
            0.6652480050648348,
            0.6679811494436834,
            0.6679811494436834,
            0.6679811494436834,
            0.6707641298632764,
            0.6707641298632764,
            0.6707641298632764,
            0.6707641298632764,
            0.6707641298632764,
            0.6736612458411845,
            0.677131806070278,
            0.6545930550512705,
            0.6545930550512705,
            0.6545930550512705,
            0.6545930550512705,
            0.6545930550512705,
            0.6561428928046398,
            0.6602358646132876,
            0.6632389482546476,
            0.6632389482546476,
            0.6632389482546476,
            0.6632389482546476,
            0.6615466375739808,
            0.6615466375739808,
            0.6500570301230034,
            0.6500570301230034,
            0.6500570301230034,
            0.6500570301230034,
            0.6534112286519103,
            0.6503655558319903,
            0.6503655558319903,
            0.6503655558319903,
            0.6503655558319903,
            0.6473653411041844,
            0.6473653411041844,
            0.6473653411041844,
            0.6539869945626388,
            0.6378411538233391,
            0.6378411538233391,
            0.6378411538233391,
            0.6378411538233391,
            0.6378411538233391,
            0.6397532119574669,
            0.6397532119574669,
            0.6374537474219847,
            0.6374537474219847,
            0.6374537474219847,
            0.6444008921418516,
            0.6444008921418516,
            0.6444008921418516,
            0.6251924413536669,
            0.6251924413536669,
            0.6251924413536669,
            0.6251924413536669,
            0.6251924413536669,
            0.6304320499197092,
            0.6304320499197092,
            0.6304320499197092,
            0.6344201902269935,
            0.6344201902269935,
            0.6344201902269935,
            0.640450859449753,
            0.640450859449753,
            0.6179179737414952,
            0.6179179737414952,
            0.6179179737414952,
            0.6161983704833974,
            0.6161983704833974,
            0.6202290342769287,
            0.6224951968711666,
            0.6257597849053371,
            0.6257597849053371,
            0.6257597849053371,
            0.6257597849053371,
            0.6257597849053371,
            0.6257597849053371,
            0.6217776710218493,
            0.6015088682357246,
            0.6051653830336593,
            0.6110626446316698,
            0.6110626446316698,
            0.6110626446316698,
            0.6141667338588396,
            0.6141667338588396,
            0.6141667338588396,
            0.6127944088223864,
            0.6127944088223864,
            0.6217863348343841,
            0.6217863348343841,
            0.6217863348343841,
            0.6049308430650762,
            0.6042474802338643,
            0.6042474802338643,
            0.6042474802338643,
            0.6042474802338643,
            0.6043356565774655,
            0.6043356565774655,
            0.6073549189527389,
            0.6073549189527389,
            0.6073549189527389,
            0.5919173354872379,
            0.5919173354872379,
            0.5919173354872379,
            0.5951903906111684,
            0.5951903906111684,
            0.5951903906111684,
            0.5940560669883251,
            0.5940560669883251,
            0.5940560669883251,
            0.5940560669883251,
            0.5846418306252446,
            0.587655894812049,
            0.5950768439494702,
            0.5950768439494702,
            0.5950768439494702,
            0.5950768439494702,
            0.5950768439494702,
            0.5950768439494702,
            0.5935648832844804,
            0.5934114388920256,
            0.5934114388920256,
            0.5934114388920256,
            0.5698165909894015,
            0.5698165909894015,
            0.5770160816863822,
            0.5803587960039499,
            0.5836739706139803,
            0.5836739706139803,
            0.5836739706139803,
            0.5823057621789929,
            0.566863865099583,
            0.5701740501698612,
            0.5701740501698612,
            0.5701740501698612,
            0.5693064332450427,
            0.5693064332450427,
            0.5737885165890814,
            0.5780530654213111,
            0.5780530654213111,
            0.5583321581205755,
            0.5580099865457965,
            0.5580099865457965,
            0.5580099865457965,
            0.5580099865457965,
            0.5580099865457965,
            0.5607525725308337,
            0.5607525725308337,
            0.5588697401306065,
            0.5588697401306065,
            0.5590492281925125,
            0.5590492281925125,
            0.5590492281925125,
            0.5590492281925125,
            0.5590492281925125,
            0.5590492281925125,
        ]
    )
    C_common_base = np.array(
        [
            0.37573900735055354,
            0.39762919860801343,
            0.414896340031141,
            0.43639846931274123,
            0.4577714452514175,
            0.4729686501191764,
            0.49386306241581995,
            0.514099844853547,
            0.5320349019925017,
            0.5431917032463246,
            0.5620439455724879,
            0.5714865347949716,
            0.5905207565434479,
            0.5970244503843506,
            0.6181815879382556,
            0.6242497019761912,
            0.6335123380893267,
            0.6545849029505804,
            0.6612133407938655,
            0.6701909969417897,
            0.6813879237401146,
            0.7056861644438431,
            0.71693412014796,
            0.7233319013581598,
            0.7342784836773327,
            0.7526154436088817,
            0.7670065181998537,
            0.7817677348243786,
            0.796856394694598,
            0.8116245225353428,
            0.8284353220596365,
            0.8443111509214403,
            0.8659624301822657,
            0.8836352768965288,
            0.9048044790908106,
            0.9267080329589763,
            0.9499445618998655,
            0.9762591087408472,
            0.9783618676174656,
            1.0011698727801042,
            1.0298927325204865,
            1.0557704248770852,
            1.0907330132142365,
            1.0958862276364234,
            1.1221910619896729,
            1.1556958263305928,
            1.1941455772405143,
            1.2303168045907837,
            1.2394827091696605,
            1.2757465293043486,
            1.3127723511938556,
            1.3234409404189036,
            1.3922938676983672,
            1.4029446723367642,
            1.427216436246326,
            1.4631167337288427,
            1.4755016537134145,
            1.5662810618025858,
            1.5670932351919393,
            1.6200419612743235,
            1.631726851358046,
            1.6733911912265336,
            1.7323640279881218,
            1.7460130049151783,
            1.7917248354521362,
            1.855094154942822,
            1.8618482235616671,
            1.9151712970174382,
            1.9233223110140785,
            1.9794566172807642,
            1.9828849265747663,
            2.0193317282577734,
            2.1022663428330324,
            2.0781366531262657,
            2.170539678327668,
            2.161117794840146,
            2.224581415926641,
            2.216234609739242,
            2.2841649374371458,
            2.2692743809912628,
            2.3394092237739437,
            2.324655201951058,
            2.3997238840835147,
            2.373554645827918,
            2.4514758089516033,
            2.4088115576115765,
            2.4976457019501797,
            2.469777021762681,
            2.5418035222732036,
            2.5114573255461647,
            2.6062052990915556,
            2.567709754788075,
            2.637444812398657,
            2.5949313086591976,
            2.6957248468351356,
            2.6003176438496136,
            2.641896223848661,
            2.627729991260813,
            2.6717063453618013,
            2.768346912478966,
            2.7203346160203274,
            2.815525724731132,
            2.7607453661848718,
            2.8556061032683493,
            2.7468664425261062,
            2.7963589051203788,
            2.8949970687933746,
            2.8452179746405735,
            2.9583865038650417,
            2.826119587298333,
            2.8795005304985506,
            2.991626092752444,
            2.9480538482163943,
            3.008934086747534,
            3.0050475298876673,
            2.9597995621526954,
            3.094061947647151,
            3.0460264009649403,
            3.043622257103833,
            3.1623224514527433,
            3.1193769552496278,
            3.2490959259009573,
            3.246322453075755,
            3.1961581218023154,
            3.3465953033403624,
            3.442500181586417,
            3.300545815177133,
            3.456407295864791,
            3.4388895156886465,
            3.60388473993811,
            3.6029019049212425,
            3.573809540027555,
            3.7452744601310277,
            3.745074876330107,
            3.7514749158147116,
            3.957866448781929,
            3.9586094753229824,
            3.929443123894413,
            4.160892111554576,
            4.1625773856877855,
            4.18443798133338,
            4.443969797797263,
            4.447159902960708,
            4.4642838619485685,
            4.469600312599974,
            4.75781171836753,
            4.790082260531763,
            4.815834433729684,
            5.125895863191537,
            5.341036609825922,
            5.236349248914831,
            5.6226187970731765,
            5.88016633378661,
            5.730483002162425,
            6.21915581289942,
            6.229410452930138,
            6.388996880800129,
            6.438434791297174,
            6.452018627857941,
            8.015480463736532,
            8.10129407446515,
            8.118427118359184,
            8.070930299750641,
            8.469370289233384,
            9.53638242952008,
            9.564267667828993,
            10.091404922050458,
            10.252550459641153,
            11.77166800654336,
            11.699455781112869,
            12.62921358360248,
            15.213558091398387,
            15.164548819275003,
            16.78116373692457,
            16.78116373692457,
            21.76803287856789,
            21.701613572198433,
            25.074950209373128,
            26.20493716608543,
            38.25356521475712,
            51.62701043339526,
            46.539567251700184,
            56.596628942172664,
            136.60897557372348,
            136.60897557372348,
            456.58217457095225,
            2435.5854770968276,
            -93.99165653365236,
            -54.88090408038849,
            -58.07032650399647,
            -58.07896804971837,
            -35.68829047668754,
            -28.41014472811073,
            -28.323360238205378,
            -28.323360238205378,
            -21.81907674147593,
            -19.450889105952253,
            -19.384450133211764,
            -18.87822623542292,
            -15.820561524374067,
            -16.157095415256336,
            -14.369515875711473,
            -14.369515875711473,
            -13.444473698950619,
            -12.948748312098052,
            -11.864375854064237,
            -11.864375854064237,
            -10.473510200377705,
            -10.886189012606554,
            -10.141210354942306,
            -10.027480307695372,
            -9.979485561988806,
            -9.758552887743074,
            -8.95483073171856,
            -8.90546372942517,
            -8.90546372942517,
            -8.536509984216078,
            -8.536509984216078,
            -8.08465372907535,
            -7.9161485904715985,
            -7.9161485904715985,
            -7.873373881802352,
            -7.679886625916913,
            -7.26526171234203,
            -7.26526171234203,
            -7.2605045379175825,
            -7.044349758512448,
            -6.763115439934025,
            -6.763115439934025,
            -6.763115439934025,
            -6.751232462707705,
            -6.692210257393012,
            -6.422670535080513,
            -6.422670535080513,
            -6.279315946700616,
            -6.306027773012021,
            -6.263850399605311,
            -5.972620959289499,
            -5.972620959289499,
            -5.651583036941243,
            -5.937866427312729,
            -5.768930734740215,
            -5.768930734740215,
            -5.768930734740215,
            -5.360230639957314,
            -5.801170928934294,
            -5.657891451167478,
            -5.496420223824412,
            -5.443013246687297,
            -5.471432621161803,
            -5.473493944484716,
            -5.2972294223886776,
            -5.414672241214318,
            -5.328101186895486,
            -4.953298383634998,
            -5.275491587570428,
            -5.174104772458709,
            -5.124682266070766,
            -5.124682266070766,
            -4.959310501599719,
            -5.1158669818231015,
            -5.1158669818231015,
            -4.959571561574876,
            -4.959571561574876,
            -4.847027118343734,
            -4.9708150842242835,
            -4.9708150842242835,
            -4.821245493727285,
            -4.754317537171853,
            -4.754317537171853,
            -4.732158288374851,
            -4.7345379396111404,
            -4.7345379396111404,
            -4.642490831658221,
            -4.60575242027342,
            -4.60575242027342,
            -4.663813436348368,
            -4.663813436348368,
            -4.568496565304976,
            -4.529660875422399,
            -4.430360132486856,
            -4.430360132486856,
            -4.512506653275874,
            -4.512506653275874,
            -4.36743305167085,
            -4.332308382025889,
            -4.332308382025889,
            -4.332308382025889,
            -4.317602038932996,
            -4.293112900277647,
            -4.21848990220863,
            -4.185368239714856,
            -4.185368239714856,
            -4.153654564467286,
            -4.149435008512521,
            -4.149435008512521,
            -4.079111036564726,
            -4.079111036564726,
            -4.023877235973128,
            -3.8711374490159,
            -4.037233213775166,
            -4.037233213775166,
            -3.9772541948247997,
            -3.8817012933676156,
            -3.8843618780082836,
            -3.8841816051867384,
            -3.854657595951472,
            -3.823050303664102,
            -3.823050303664102,
            -3.7996699999372083,
            -3.7588808525984327,
            -3.6591636220729997,
            -3.823273077914698,
            -3.705440253710575,
            -3.705440253710575,
            -3.705440253710575,
            -3.533442668170091,
            -3.533442668170091,
            -3.649605288587709,
            -3.649605288587709,
            -3.5407686496418487,
            -3.5407686496418487,
            -3.4159304958383427,
            -3.4159304958383427,
            -3.490391473274308,
            -3.471100866666207,
            -3.471100866666207,
            -3.4194342107118962,
            -3.4194342107118962,
            -3.302940791174039,
            -3.2184826238319353,
            -3.338249782744135,
            -3.338249782744135,
            -3.338249782744135,
            -3.271534426761381,
            -3.271534426761381,
            -3.1649279840428455,
            -3.248619006040548,
            -3.224876057627863,
            -3.162011886150153,
            -3.162011886150153,
            -3.162011886150153,
            -3.066264515817663,
            -3.008096891117998,
            -3.10657033113232,
            -3.10657033113232,
            -3.10657033113232,
            -3.028392055047379,
            -2.959512881755752,
            -2.959512881755752,
            -2.937516545258157,
            -3.0254754647016466,
            -3.0254754647016466,
            -2.9665061393659924,
            -2.8855306894509463,
            -2.8855306894509463,
            -2.8638236109409223,
            -2.844776982954905,
            -2.8967533172960938,
            -2.8967533172960938,
            -2.836472114539902,
            -2.8265464323994953,
            -2.8287076712881962,
            -2.7771784350510966,
            -2.7771784350510966,
            -2.7454221162782817,
            -2.7595045369879356,
            -2.7580282184477896,
            -2.732697556682744,
            -2.732697556682744,
            -2.732697556682744,
            -2.7126644205960475,
            -2.6596044133993337,
            -2.6676281426234048,
            -2.6676281426234048,
            -2.6584418417393785,
            -2.64050801845931,
            -2.64050801845931,
            -2.64050801845931,
            -2.6066584343534167,
            -2.5899853514119613,
            -2.5899853514119613,
            -2.5899853514119613,
            -2.58875839592709,
            -2.58875839592709,
            -2.543783407298735,
            -2.543783407298735,
            -2.5256154343428996,
            -2.5341566914473965,
            -2.5120372732025014,
            -2.5120372732025014,
            -2.5120372732025014,
            -2.5120372732025014,
            -2.5120372732025014,
            -2.451445009866668,
            -2.3910030314809316,
            -2.4755488903623406,
            -2.4755488903623406,
            -2.4755488903623406,
            -2.4454147858400166,
            -2.4454147858400166,
            -2.4454147858400166,
            -2.4454147858400166,
            -2.3854734582272292,
            -2.445926775358806,
            -2.4232026178456567,
            -2.4232026178456567,
            -2.4232026178456567,
            -2.4232026178456567,
            -2.397245519396717,
            -2.397245519396717,
            -2.3402814748373126,
            -2.4290236441455306,
            -2.4290236441455306,
            -2.367438501967648,
            -2.367438501967648,
            -2.367438501967648,
            -2.416295135152839,
            -2.3795129479530717,
            -2.373712055027307,
            -2.373712055027307,
            -2.324962148143479,
            -2.3928155511691567,
            -2.3928357293614146,
            -2.3248133947146163,
            -2.3244339349110708,
            -2.3244339349110708,
            -2.3260156797979006,
            -2.3862467929344944,
            -2.3862467929344944,
            -2.3862467929344944,
            -2.350223376781794,
            -2.333474782684923,
            -2.3166293989515316,
            -2.3166293989515316,
            -2.2940169893517464,
            -2.297117948751868,
            -2.4456144008695877,
            -2.390785722560323,
            -2.390785722560323,
            -2.375218845045291,
            -2.3237081153267,
            -2.3237081153267,
            -2.3237081153267,
            -2.3284601707435657,
            -2.4698133559130633,
            -2.4166827074175705,
            -2.4166827074175705,
            -2.4166827074175705,
            -2.370014505293884,
            -2.355712930361707,
            -2.3328740783979063,
            -2.3328740783979063,
            -2.3391257144303137,
            -2.5200924457873954,
            -2.5200924457873954,
            -2.4075331827024464,
            -2.4075331827024464,
            -2.4075331827024464,
            -2.4075331827024464,
            -2.4075331827024464,
            -2.4075331827024464,
            -2.4021792129791573,
            -2.5383996104127364,
            -2.4717055290705767,
            -2.4717055290705767,
            -2.4717055290705767,
            -2.4717055290705767,
            -2.450008856335651,
            -2.450008856335651,
            -2.450008856335651,
            -2.4037225708405523,
            -2.6323491952681066,
            -2.5609311348729116,
            -2.5609311348729116,
            -2.5518057572957984,
            -2.5518057572957984,
            -2.546198376685853,
            -2.5519448114974264,
            -2.5519448114974264,
            -2.449065606059838,
            -2.6669786975508765,
            -2.6669786975508765,
            -2.6669786975508765,
            -2.6400826244735893,
            -2.6400826244735893,
            -2.6400826244735893,
            -2.635586740593134,
            -2.5244552438483727,
            -2.5244552438483727,
            -2.854005586785324,
            -2.854005586785324,
            -2.842061289022477,
            -2.86051350723736,
            -2.77319622871233,
            -2.77319622871233,
            -2.77319622871233,
            -2.7000256040589155,
            -2.7000256040589155,
            -2.6995753811038408,
            -2.689113047435928,
            -3.0640193246163263,
            -2.976542566180142,
            -2.976542566180142,
            -2.8928733382394887,
            -2.8928733382394887,
            -2.886515073607598,
            -2.886515073607598,
            -2.886515073607598,
            -2.886086877393255,
            -3.1497748498313523,
            -3.1497748498313523,
            -3.0679181337488632,
            -3.0574976411464965,
            -3.0574976411464965,
            -3.0574976411464965,
            -3.0574976411464965,
            -3.0574976411464965,
            -3.0574976411464965,
            -3.057148525327008,
            -3.602953136947714,
            -3.4343037346173046,
            -3.1870674364558393,
            -3.1870674364558393,
            -3.1870674364558393,
            -3.1870674364558393,
            -3.1870674364558393,
            -3.1870674364558393,
            -3.1813471957304036,
            -3.196687462221619,
            -3.6213407538885236,
            -3.6213407538885236,
            -3.620041651256456,
            -3.620041651256456,
            -3.6434726870634213,
            -3.6434726870634213,
            -3.6361452388764652,
            -3.6361452388764652,
            -3.1282328571488676,
            -3.1282328571488676,
            -3.7343083588533212,
            -3.7343083588533212,
            -3.7310601717779663,
            -3.7310601717779663,
            -3.7310601717779663,
            -3.7310601717779663,
            -3.7310601717779663,
            -3.624696480445007,
            -3.624696480445007,
            -3.4779859690718293,
            -3.4779895709812867,
            -4.193805211553644,
            -4.193805211553644,
            -4.193805211553644,
            -4.193805211553644,
            -4.193805211553644,
            -3.734598657194529,
            -3.7306411772491663,
            -3.797940871107673,
            -3.797940871107673,
            -3.797940871107673,
            -3.7980048915793367,
            -4.622173123027474,
            -4.432446987662558,
            -4.087306184964177,
            -4.084658967910418,
            -4.084658967910418,
            -4.084658967910418,
            -4.084658967910418,
            -4.534855983953739,
            -4.337928990406116,
            -4.118904708554365,
            -4.118983774468443,
            -4.118983774468443,
            -4.118983774468443,
            -4.118983774468443,
            -4.118277073657742,
            -4.998121560273297,
            -4.732545609682616,
            -4.4002701669962745,
            -4.4002701669962745,
            -4.400274999575058,
            -4.400274999575058,
            -4.4002793479676265,
            -4.4002793479676265,
            -4.4002793479676265,
            -4.211996153043525,
            -5.199137573244606,
            -4.63395800581404,
            -4.63395800581404,
            -4.78355811881005,
            -4.78355811881005,
            -4.783698697867709,
            -4.783698697867709,
            -4.534490456065867,
            -4.534490456065867,
            -4.534490456065867,
            -4.133776141201701,
            -4.133776141201701,
            -5.031514681623902,
            -5.228108629523274,
            -5.228108629523274,
            -5.228334546289206,
            -4.904803782216326,
            -4.645414828533864,
            -4.645414828533864,
            -4.651755951440943,
            -4.651755951440943,
            -4.651755951440943,
            -4.651755951440943,
            -4.651755951440943,
            -5.303336881088562,
            -5.303336881088562,
            -4.94240050267788,
            -4.952912535761085,
            -4.952912535761085,
            -4.952912535761085,
            -4.952633795263265,
            -4.656911927993108,
            -4.656911927993108,
            -4.656911927993108,
            -4.867460001288425,
            -4.867460001288425,
            -5.838830853734494,
            -5.274186630822789,
            -5.274186630822789,
            -5.274186630822789,
            -5.288058712906374,
            -5.288058712906374,
            -5.287895273685035,
            -5.287895273685035,
            -5.0720985116269315,
            -4.739491149656386,
            -4.739491149656386,
            -4.739491149656386,
            -5.959036065473626,
            -5.959036065473626,
            -5.959036065473626,
            -5.599697754639607,
            -5.599697754639607,
            -5.599697754639607,
            -4.939346722363702,
            -4.93948132720957,
            -5.2013683173244605,
            -5.22579259747066,
            -5.22579259747066,
            -5.025857921274337,
            -6.592871717174341,
            -6.592871717174341,
            -6.592871717174341,
            -6.592871717174341,
            -5.6163052590136315,
            -5.6163052590136315,
            -5.6163052590136315,
            -5.625120746554413,
            -5.625120746554413,
            -5.625120746554413,
            -5.625120746554413,
            -5.625120746554413,
            -5.625120746554413,
            -7.862763459890804,
            -6.433693979972905,
            -6.459533797961855,
            -6.083971600147039,
            -6.083971600147039,
            -6.450023931146282,
            -6.450023931146282,
            -6.461278730806482,
            -6.461278730806482,
            -6.461278730806482,
            -6.153228420896658,
            -5.247506180979436,
            -5.247506180979436,
            -7.2223362912665365,
            -7.2223362912665365,
            -7.811645743586211,
            -7.811645743586211,
            -7.811645743586211,
            -7.213741413034578,
            -7.213741413034578,
            -7.218431513377577,
            -7.218431513377577,
            -5.940824978540178,
            -5.987381394710549,
            -5.987381394710549,
            -6.302791610598425,
            -8.864708635869103,
            -8.864708635869103,
            -8.864708635869103,
            -8.864708635869103,
            -8.864708635869103,
            -8.56137308629535,
            -6.808002146295821,
            -6.8585640730981625,
            -6.8585640730981625,
            -6.8585640730981625,
            -7.38625456491086,
            -7.38625456491086,
            -6.765726439378816,
            -10.609184434579857,
            -10.609184434579857,
            -7.909059408821382,
            -7.909059408821382,
            -7.909059408821382,
            -7.95853411273009,
            -8.523986343496492,
            -8.155594109948385,
            -8.155594109948385,
            -8.155594109948385,
            -8.155594109948385,
            -8.175603230512225,
            -6.437289080360434,
            -6.437289080360434,
            -8.6494979526715,
            -8.6494979526715,
            -9.691768831758507,
            -9.78051424094251,
            -9.78051424094251,
            -9.78051424094251,
            -9.78051424094251,
            -9.816449575683937,
            -6.914147399549932,
            -6.914147399549932,
            -6.914147399549932,
            -6.914147399549932,
            -6.914147399549932,
            -11.558319671201351,
            -11.558319671201351,
            -10.639146944080162,
            -10.639146944080162,
            -7.843315356721152,
            -7.843315356721152,
            -7.843315356721152,
            -7.843315356721152,
            -7.870845633976884,
            -7.870845633976884,
            -10.065462943862405,
            -10.065462943862405,
            -10.065462943862405,
            -10.065462943862405,
            -7.392369992622828,
            -7.392369992622828,
            -7.392369992622828,
            -7.392369992622828,
            -7.392369992622828,
            -9.774553948070425,
            -9.906888098893601,
            -11.39388216918492,
            -11.449588399763499,
            -11.449588399763499,
            -8.116261262906619,
            -8.116261262906619,
            -8.116261262906619,
            -8.116261262906619,
            -7.57194335356725,
            -7.57194335356725,
            -7.57194335356725,
            -8.966132714791044,
            -8.966132714791044,
            -15.581924419593653,
            -10.126080327777222,
            -10.126080327777222,
            -9.52133047376507,
            -9.52133047376507,
            -9.692766131685989,
            -9.692766131685989,
            -9.826401994954196,
            -9.607997433464348,
            -9.607997433464348,
            -10.620188659957623,
            -10.620188659957623,
            -10.620188659957623,
            -8.8871373811846,
            -8.92826716427421,
            -8.92826716427421,
            -8.92826716427421,
            -9.682170576379345,
            -9.739336016510878,
            -9.827257018302165,
            -9.827257018302165,
            -9.0807069087448,
            -7.93174847956649,
            -7.93174847956649,
            -7.93174847956649,
            -11.155938370161488,
            -11.155938370161488,
            -11.155938370161488,
            -11.155938370161488,
            -7.403671415226294,
            -6.898191309605864,
            -7.012923611358617,
            -7.012923611358617,
            -7.076956779638238,
            -6.749542233217342,
            -6.730679620870806,
            -6.99770950657096,
            -6.99770950657096,
            -6.99770950657096,
            -4.861441262291578,
            -4.861441262291578,
        ]
    )

    N = 25  # window size
    C_common_emit_ma = (
        pd.Series(C_common_emit).rolling(window=N).mean().iloc[N - 1 :].values
    )
    C_common_base_ma = (
        pd.Series(C_common_base).rolling(window=N).mean().iloc[N - 1 :].values
    )

    # current bjt configuration CE/CB
    if self.radioButton_CE.isChecked():
        ax.plot(freq_list, C_common_emit, label="C (raw data)")
        ax.plot(freq_list[N - 1 :], C_common_emit_ma, label=f"C (moving average N={N})")
        plt.suptitle("$C_{CE}(f)$")
        plt.ylim(0, 4.5)
    else:
        ax.plot(freq_list, C_common_base, label="C (raw data)")
        ax.plot(freq_list[N - 1 :], C_common_base_ma, label=f"C (moving average N={N})")
        plt.suptitle("$C_{CB}(f)$")
        plt.ylim(-8, 8)

    # plot unconditionally stable area
    ax.axhspan(0, 1, alpha=0.08, color="green", label="Unconditionally stable area")

    plt.grid(True, which="both", ls="-")
    plt.xlim(45, 1500)

    plt.xscale("log")
    plt.legend()
    plt.xlabel("$f\ (MHz)$")
    plt.ylabel("C")

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
    if self.radiobutton_2n4957.isChecked():
        self.f0_box_2.setFocus()
    else:
        self.y_i_box_2.setFocus()
