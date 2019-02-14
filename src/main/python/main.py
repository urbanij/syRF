#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 19 15:38:35 2018

@author(s)   : Francesco Urbani
@file        : syRF.py
@descritpion : The main file

"""

# ============================================================
from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
# ============================================================

from PyQt5 import QtCore, QtGui, QtWidgets
from syRF_ui import Ui_MainWindow

import math
import cmath
import numpy as np
import matplotlib.pyplot as plt


# import my files
import Y_tab
import S_tab
import plot_reflection_coefficient
import LC_matching_tab
import microstrip_matching
import quarter_wave_matching
import lambda4_tab
import open_pdf



msg_error = "" # display nothing if error occurs


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)
        

        
        # self.tabWidget.setCurrentIndex(1)
        self.checkBox.setChecked(True)
        self.checkBox_2.setChecked(True)

        self.f0_box_2.setFocus()  # set focus on frequency of Y tab on startup

        self.radioButton.setChecked(True) # Z of quarter wave impedance matching set

        self.radioButton_CE.setChecked(True) # radioButton is checked on startup. Common emitter is the default config.
        self.radioButton_MRF571.setChecked(True) # radioButton_MRF571 is the default
        self.radioButton_5.setChecked(True) # insert impedance as Z is the default
        self.Fill_ys_yl_opt_button.setEnabled(False)
        self.plot.setEnabled(False)
        # self.Z0_box.setEnabled(False) # Z0 is disabled by default, i.e. it's fixed @ 50 ohm
        self.plot_isc_button_2.setEnabled(False)
        

        # Y
        self.f0_box_2.editingFinished.connect(self.fill_Y_boxes)
        self.f0_box_2.editingFinished.connect(self.Calculate_button_4.click)
        self.radioButton_CE.toggled['bool'].connect(self.fill_Y_boxes)
        self.radioButton_CE.toggled['bool'].connect(self.Calculate_button_4.click)

        self.checkBox.stateChanged.connect(self.disable_2N4957)
        self.checkBox_2.stateChanged.connect(self.disable_MRF57)

        self.y_i_box_2.editingFinished.connect(self.Calculate_button_4.click)
        self.y_f_box_2.editingFinished.connect(self.Calculate_button_4.click)
        self.y_o_box_2.editingFinished.connect(self.Calculate_button_4.click)
        self.y_r_box_2.editingFinished.connect(self.Calculate_button_4.click)
        self.y_s_box_2.editingFinished.connect(self.Calculate_button_4.click)
        self.y_L_box_2.editingFinished.connect(self.Calculate_button_4.click)

        self.Calculate_button_4.clicked.connect(self.compute_Y_2N4957)
        self.show_plots_button.clicked.connect(self.show_plot_Y_parameters)
        self.open_datasheet_Y_button.clicked.connect(self.open_datasheet_Y)
        self.open_Y_formulas_button.clicked.connect(self.open_Y_formulas)

        self.plot_C_f0_button.clicked.connect(self.plot_C_vs_f)

        self.Clean_button_3.clicked.connect(self.clean_Y_2N4957)
        self.Clean_all_button_4.clicked.connect(self.clean_all_Y_2N4957)
        self.Fill_ys_yl_opt_button.clicked.connect(self.fill_ys_yl_opt_2N4957)
        

        # S
        self.vce_box.editingFinished.connect(self.fill_S_boxes)
        self.ic_box.editingFinished.connect(self.fill_S_boxes)
        self.f_box.editingFinished.connect(self.fill_S_boxes)
        
        self.vce_box.editingFinished.connect(self.Calculate_button_5.click)
        self.ic_box.editingFinished.connect(self.Calculate_button_5.click)
        self.f_box.editingFinished.connect(self.Calculate_button_5.click)

        

        self.s11_box.editingFinished.connect(self.Calculate_button_5.click)
        self.s21_box.editingFinished.connect(self.Calculate_button_5.click)
        self.s12_box.editingFinished.connect(self.Calculate_button_5.click)
        self.s22_box.editingFinished.connect(self.Calculate_button_5.click)

        self.radioButton_MRF571.toggled['bool'].connect(self.fill_S_boxes)
        self.radioButton_MRF571.toggled['bool'].connect(self.Calculate_button_5.click)

        self.Z0_box.editingFinished.connect(self.Calculate_button_5.click)
        self.ZS_box.editingFinished.connect(self.Calculate_button_5.click)
        self.ZL_box.editingFinished.connect(self.Calculate_button_5.click)

        self.ZS_box_2.editingFinished.connect(self.Calculate_button_5.click)
        self.ZS_box_5.editingFinished.connect(self.Calculate_button_5.click)
        self.ZS_box_4.editingFinished.connect(self.Calculate_button_5.click)
        self.ZS_box_3.editingFinished.connect(self.Calculate_button_5.click)
        
        self.radioButton_5.toggled['bool'].connect(self.disable_enable_Z_or_gamma_input)
        self.radioButton_5.toggled['bool'].connect(self.Calculate_button_5.click)


        self.GAdb_box_2.editingFinished.connect(self.Calculate_button_5.click)
        self.GPdb_box_2.editingFinished.connect(self.Calculate_button_5.click)
        self.GTdb_box_2.editingFinished.connect(self.Calculate_button_5.click)
        self.NFmindb_box_2.editingFinished.connect(self.Calculate_button_5.click)
        self.NFdb_box_2.editingFinished.connect(self.Calculate_button_5.click)
        self.rn_box_2.editingFinished.connect(self.Calculate_button_5.click)
        self.gamma_s_on_box.editingFinished.connect(self.Calculate_button_5.click)

        self.plot_isc_button_2.clicked.connect(self.smith_plot_all)
        self.open_datasheet_button.clicked.connect(self.open_datasheet)
        self.open_S_formulas_button.clicked.connect(self.open_S_formulas)
        self.Calculate_button_5.clicked.connect(self.compute_S_MRF571)
        self.clean_S_button.clicked.connect(self.clean_S_MRF571)
        self.Clean_all_button_6.clicked.connect(self.clean_all_S_MRF571)


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
        
        

        
        # MAKE QUARTER WAVE CALCULATE BUTTON AND SHOW SMITH PLOT BUTTON

        # quarter_wave_matching

        self.radioButton.toggled['bool'].connect(self.disable_boxes_quarter_wave_im)

        self.Z0_box2.editingFinished.connect(self.Calculate_quarter.click)

        self.Z_in_box.editingFinished.connect(self.Calculate_quarter.click)
        self.Z_out_box.editingFinished.connect(self.Calculate_quarter.click)
        
        self.ZS_box_9.editingFinished.connect(self.Calculate_quarter.click)
        self.ZS_box_6.editingFinished.connect(self.Calculate_quarter.click)
        self.ZS_box_7.editingFinished.connect(self.Calculate_quarter.click)
        self.ZS_box_8.editingFinished.connect(self.Calculate_quarter.click)

        
        self.Calculate_quarter.clicked.connect(self.calculate_tab_quarter_wave_im)
        self.Show_Smith.clicked.connect(self.showSmithPlot)
        self.clean_all_button213.clicked.connect(self.clean_all_quarter_wave)


        # lambda4_tab
        self.z1_box.editingFinished.connect(self.Calculate_lambda4.click)
        self.z2_box.editingFinished.connect(self.Calculate_lambda4.click)
        self.Z0_box2_2.editingFinished.connect(self.Calculate_lambda4.click)
        
        self.Calculate_lambda4.clicked.connect(self.calculate_z_lambda4)
        self.clean_lambda4_button.clicked.connect(self.clean_lambda4)


        # ------------------------------------------------------------------------------------
    
        
    
    def fill_Y_boxes(self):
        Y_tab.fill_Y_boxes(self)


    def compute_Y_2N4957(self):
        Y_tab.compute_Y_2N4957(self)

    def show_plot_Y_parameters(self):
        Y_tab.show_plot_Y_parameters(self)

    def open_datasheet_Y(self):
        open_pdf.open_pdf("2N4957/2N4957.pdf")

    def open_Y_formulas(self):
        open_pdf.open_pdf("../../../doc/Formulario-ETLC_Y.pdf") # from here: https://github.com/giuliof/Dispense-ETLC)

    def plot_C_vs_f(self):
        Y_tab.plot_C_vs_f(self)

    def clean_Y_2N4957(self):
        Y_tab.clean_Y_2N4957(self)

    def clean_all_Y_2N4957(self):
        Y_tab.clean_all_Y_2N4957(self)

    def fill_ys_yl_opt_2N4957(self):
        Y_tab.fill_ys_yl_opt_2N4957(self)

    def disable_2N4957(self):
        if not self.checkBox.isChecked():
            self.label_165.setEnabled(False)
            self.label_166.setEnabled(False)
            self.label_118.setEnabled(False)
            self.label_37.setEnabled(False)
            self.label_38.setEnabled(False)
            self.label_8.setEnabled(False)
            self.radioButton_CE.setEnabled(False)
            self.radioButton_CB.setEnabled(False)
            self.f0_box_2.setEnabled(False)
            self.y_i_box_2.setFocus()
        else:
            self.label_165.setEnabled(True)
            self.label_166.setEnabled(True)
            self.label_118.setEnabled(True)
            self.label_37.setEnabled(True)
            self.label_38.setEnabled(True)
            self.label_8.setEnabled(True)
            self.radioButton_CE.setEnabled(True)
            self.radioButton_CB.setEnabled(True)
            self.f0_box_2.setEnabled(True)
            self.f0_box_2.setFocus()


    def fill_S_boxes(self):
        S_tab.fill_S_boxes(self)

    def compute_S_MRF571(self):
        S_tab.compute_S_MRF571(self)


    def open_datasheet(self):
        open_pdf.open_pdf("MRF57/MRF57.pdf")

    def open_S_formulas(self):
        open_pdf.open_pdf("../../../doc/Formulario-ETLC_S.pdf") # from here: https://github.com/giuliof/Dispense-ETLC)
        
    def smith_plot_all(self):
        S_tab.smith_plot_all(self)
        
    def draw_equi_GA_stability_circles(self):
        S_tab.draw_equi_GA_stability_circles(self)


    def clean_S_MRF571(self):
        S_tab.clean_S_MRF571(self)


    def clean_all_S_MRF571(self):
        S_tab.clean_all_S_MRF571(self)


    def disable_MRF57(self):
        S_tab.disable_MRF57(self)
    

    def disable_enable_Z_or_gamma_input(self):
        S_tab.disable_enable_Z_or_gamma_input(self)




    def compute_LC_matching(self):
        LC_matching_tab.compute_LC_matching(self)

    def clean_all_LC_matching(self):
        LC_matching_tab.clean_all_LC_matching(self)

    def plot_reflection_coefficient(self):
        plot_reflection_coefficient.plot_gamma( LC_matching_tab.compute_LC_matching(self) )

    def open_pdf_sketch_matching(self):
        open_pdf.open_pdf("../../../aux/matching_network.pdf")


    def compute_matching_microstrip(self):
        microstrip_matching_tab.compute_matching_microstrip(self)

    def open_plots(self):
        open_pdf.open_pdf("microstrip_matching/epsilon_r_graphs.pdf")


    def show_plots(self):
        microstrip_matching_tab.show_plots(self)

    def clean_all_microstrip_tab(self):
        microstrip_matching_tab.clean_all_microstrip_tab(self)





    def showSmithPlot(self):
        quarter_wave_matching.showSmithPlot(self)

    def calculate_tab_quarter_wave_im(self):
        quarter_wave_matching.calculate_tab_quarter_wave_im(self)

    def disable_boxes_quarter_wave_im(self):
        quarter_wave_matching.disable_boxes_quarter_wave_im(self)

    def clean_all_quarter_wave(self):
        quarter_wave_matching.clean_all_quarter_wave(self)




    

    def calculate_z_lambda4(self):
        lambda4_tab.calculate_z_lambda4(self)

    def clean_lambda4(self):
        self.z1_box.setText("")
        self.z2_box.setText("")
        self.z1_box.setFocus()
        self.Calculate_lambda4.click()


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = mainProgram()
    nextGui.show()
    sys.exit(app.exec_())
