#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 19 15:38:35 2018

@author(s)   : Francesco Urbani
@file        : syRF.py
@descritpion : The main file

"""

from PyQt5 import QtCore, QtGui, QtWidgets
from syRF_ui import Ui_MainWindow

import math
import cmath
import numpy as np
import matplotlib.pyplot as plt



msg_error = "" # display nothing if error occurs


class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(mainProgram, self).__init__(parent)
		self.setupUi(self)


		
		# self.tabWidget.setCurrentIndex(1)
		self.checkBox.setChecked(True)
		self.checkBox_2.setChecked(True)

		self.f0_box_2.setFocus()
		self.vce_box.setFocus()
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
		self.Calculate_button_5.clicked.connect(self.compute_S_MRF571)
		self.clean_S_button.clicked.connect(self.clean_S_MRF571)
		self.Clean_all_button_6.clicked.connect(self.clean_all_S_MRF571)


		# LC_matching
		self.f0_box.editingFinished.connect(self.Calculate_button_3.click)
		self.input_box.editingFinished.connect(self.Calculate_button_3.click)
		self.output_box.editingFinished.connect(self.Calculate_button_3.click)
		self.comboBox.currentIndexChanged['QString'].connect(self.Calculate_button_3.click)
		self.comboBox_2.currentIndexChanged['QString'].connect(self.Calculate_button_3.click)
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
		from Y_tab import fill_Y_boxes
		fill_Y_boxes(self)


	def compute_Y_2N4957(self):
		from Y_tab import compute_Y_2N4957
		compute_Y_2N4957(self)

	def show_plot_Y_parameters(self):
		from Y_tab import show_plot_Y_parameters
		show_plot_Y_parameters(self)

	def open_datasheet_Y(self):
		from Y_tab import open_datasheet_Y
		open_datasheet_Y(self)

	def clean_Y_2N4957(self):
		from Y_tab import clean_Y_2N4957
		clean_Y_2N4957(self)

	def clean_all_Y_2N4957(self):
		from Y_tab import clean_all_Y_2N4957
		clean_all_Y_2N4957(self)

	def fill_ys_yl_opt_2N4957(self):
		from Y_tab import fill_ys_yl_opt_2N4957
		fill_ys_yl_opt_2N4957(self)

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
		from S_tab import fill_S_boxes
		fill_S_boxes(self)

	def compute_S_MRF571(self):
		from S_tab import compute_S_MRF571
		compute_S_MRF571(self)


	def open_datasheet(self):
		from S_tab import open_datasheet
		open_datasheet(self)
		
	def smith_plot_all(self):
		from S_tab import smith_plot_all
		smith_plot_all(self)
		
	def draw_equi_GA_stability_circles(self):
		from S_tab import draw_equi_GA_stability_circles
		draw_equi_GA_stability_circles(self)


	def clean_S_MRF571(self):
		from S_tab import clean_S_MRF571
		clean_S_MRF571(self)


	def clean_all_S_MRF571(self):
		from S_tab import clean_all_S_MRF571
		clean_all_S_MRF571(self)


	def disable_MRF57(self):
		from S_tab import disable_MRF57
		disable_MRF57(self)
	

	def disable_enable_Z_or_gamma_input(self):
		from S_tab import disable_enable_Z_or_gamma_input
		disable_enable_Z_or_gamma_input(self)




	def compute_LC_matching(self):
		from LC_matching_tab import compute_LC_matching
		compute_LC_matching(self)

	def clean_all_LC_matching(self):
		from LC_matching_tab import clean_all_LC_matching
		clean_all_LC_matching(self)

	def plot_reflection_coefficient(self):
		from plot_reflection_coefficient import plot_gamma
		from LC_matching_tab import compute_LC_matching
		plot_gamma( compute_LC_matching(self) )


	def compute_matching_microstrip(self):
		from microstrip_matching_tab import compute_matching_microstrip
		compute_matching_microstrip(self)

	def open_plots(self):
		from microstrip_matching_tab import open_plots
		open_plots(self)

	def show_plots(self):
		from microstrip_matching_tab import show_plots
		show_plots(self)

	def clean_all_microstrip_tab(self):
		from microstrip_matching_tab import clean_all_microstrip_tab
		clean_all_microstrip_tab(self)



	def showSmithPlot(self):
		from quarter_wave_matching import showSmithPlot
		showSmithPlot(self)


	def calculate_tab_quarter_wave_im(self):
		from quarter_wave_matching import calculate_tab_quarter_wave_im
		calculate_tab_quarter_wave_im(self)

	def disable_boxes_quarter_wave_im(self):
		from quarter_wave_matching import disable_boxes_quarter_wave_im
		disable_boxes_quarter_wave_im(self)

	def clean_all_quarter_wave(self):
		from quarter_wave_matching import clean_all_quarter_wave
		clean_all_quarter_wave(self)


	

	def calculate_z_lambda4(self):
		from lambda4_tab import calculate_z_lambda4
		calculate_z_lambda4(self)

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
