#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 14 12:38:00 2018

@author(s)   : Francesco Urbani
@file        : S_tab.py
@descritpion : 

"""

import math
import cmath
import os
import sys
import numpy as np

import S_functions as S
import csv_parser
from twoport.utils import db as to_dB
from intersections import find_intersection_points as int_points


msg_error = "" # displays nothing if error occurs



def fill_S_boxes(self):

	try:
		vce = float(self.vce_box.text())	
	except Exception as e:
		vce = msg_error
	
	try:
		ic  = float(self.ic_box.text())
	except Exception as e:
		ic = msg_error
	
	try:
		f = float(self.f_box.text())
	except Exception as e:
		f = msg_error
	


	try:
		if self.radioButton_MRF571.isChecked():
			bjt = "MRF571"
		else:
			bjt = "MRF572"
	
		self.checkBox_2.setText(bjt + " (Common Emitter config.)")
		s11, s12, s21, s22, NF_opt_dB, R_n, gamma_s_on = csv_parser.get_S_parameters(vce, ic, f, bjt)	
	except Exception as e:
		bjt = msg_error


	try:
		# S paramters displayed in polar mode with phase in degrees
		self.s11_box.setText( str(s11[0]) + "∠" + str(s11[1]) )
		self.s12_box.setText( str(s12[0]) + "∠" + str(s12[1]) )
		self.s21_box.setText( str(s21[0]) + "∠" + str(s21[1]) )
		self.s22_box.setText( str(s22[0]) + "∠" + str(s22[1]) )
		# self.Z0_box.setText("50")
	except Exception as e:
		self.s11_box.setText(msg_error)
		self.s12_box.setText(msg_error)
		self.s21_box.setText(msg_error)
		self.s22_box.setText(msg_error)
		# self.Z0_box.setText(msg_error)


	try:
		self.gamma_s_on_box.setText( str(gamma_s_on[0]) + "∠" + str(gamma_s_on[1]) )
		self.NFmindb_box_2.setText(str(NF_opt_dB))
		self.NFdb_box_2.setPlaceholderText("[" + str(NF_opt_dB) + ", ∞)")
		self.rn_box_2.setText(str(R_n))
	
	except Exception as e:
		self.gamma_s_on_box.setText(msg_error)
		self.NFmindb_box_2.setText(msg_error)
		self.rn_box_2.setText(msg_error)
		
	
	try:
		# S parameters converted into rectangular form.
		s11 = cmath.rect(float(s11[0]), math.radians(float(s11[1])))
		s12 = cmath.rect(float(s12[0]), math.radians(float(s12[1])))
		s21 = cmath.rect(float(s21[0]), math.radians(float(s21[1])))
		s22 = cmath.rect(float(s22[0]), math.radians(float(s22[1])))
		gamma_s_on = cmath.rect(float(gamma_s_on[0]), math.radians(float(gamma_s_on[1])))
	except Exception as e:
		pass
		
	return vce, ic, f, bjt
	






def compute_S_MRF571(self):

	# --------------
	# read inputs
	# --------------

	try:
		s11 = self.s11_box.text().split("∠")
		s11 = cmath.rect(float(s11[0]), math.radians(float(s11[1])))
	except Exception as e:
		s11 = msg_error

	try:
		s21 = self.s21_box.text().split("∠")
		s21 = cmath.rect(float(s21[0]), math.radians(float(s21[1])))
	except Exception as e:
		s21 = msg_error

	try:
		s12 = self.s12_box.text().split("∠")
		s12 = cmath.rect(float(s12[0]), math.radians(float(s12[1])))
	except Exception as e:
		s12 = msg_error

	try:
		s22 = self.s22_box.text().split("∠")
		s22 = cmath.rect(float(s22[0]), math.radians(float(s22[1])))
	except Exception as e:
		s22 = msg_error

	try:
		Z0 = float(self.Z0_box.text()) # Z0 is not complex
	except Exception as e:
		Z0 = msg_error


	# READ Z IF Z INSERTION IS SELECTED, OTHERWISE READ GAMMA
	if self.radioButton_5.isChecked():
		try:
			ZL = complex(self.ZL_box.text())
		except Exception as e:
			ZL = msg_error

		try:
			ZS = complex(self.ZS_box.text())
		except Exception as e:
			ZS = msg_error
	else:
		# read gamma_s and gamma_l -- magnitute and phase 
		# and convert it to rectangular form
		try:
			abs_gamma_s = float(self.ZS_box_2.text())
		except Exception as e:
			abs_gamma_s = msg_error
		try:
			phase_gamma_s = float(self.ZS_box_5.text())
		except Exception as e:
			phase_gamma_s = msg_error
		try:
			abs_gamma_l = float(self.ZS_box_4.text())
		except Exception as e:
			abs_gamma_l = msg_error
		try:
			phase_gamma_l = float(self.ZS_box_3.text())
		except Exception as e:
			phase_gamma_l = msg_error

		# convertion:
		try:
			gamma_S = cmath.rect(abs_gamma_s, math.radians(phase_gamma_s))
		except Exception as e:
			gamma_S = msg_error
		try:
			gamma_L = cmath.rect(abs_gamma_l, math.radians(phase_gamma_l))
		except Exception as e:
			gamma_L = msg_error
	


	# --------------------------------------
	# NOISE PARAMETERS
	try:
		gamma_s_on = self.gamma_s_on_box.text().split("∠")
		gamma_s_on = cmath.rect(float(gamma_s_on[0]), math.radians(float(gamma_s_on[1])))
	except Exception as e:
		gamma_s_on = msg_error

	try:
		NF_opt_dB = float(self.NFmindb_box_2.text())
	except Exception as e:
		NF_opt_dB = msg_error

	try:
		R_n = float(self.rn_box_2.text())
	except Exception as e:
		R_n = msg_error
	# --------------------------------------



	try:
		NF_circle_dB = float(self.NFdb_box_2.text())
	except Exception as e:
		NF_circle_dB = msg_error


	try:
		Ga_circle_dB = float(self.GAdb_box_2.text())
	except Exception as e:
		Ga_circle_dB = msg_error


	try:
		Gt_circle_dB = float(self.GTdb_box_2.text())
	except Exception as e:
		Gt_circle_dB = msg_error


	try:
		Gp_circle_dB = float(self.GPdb_box_2.text())
	except Exception as e:
		Gp_circle_dB = msg_error











	# --------------
	# compute stuff
	# --------------

	try:
		D = S.calculate_D(s11, s12, s21, s22)
	except Exception as e:
		D = msg_error

	try:
		K = S.calculate_K(s11, s12, s21, s22)
		self.plot_isc_button_2.setEnabled(True)
	except Exception as e:
		K = msg_error
		self.plot_isc_button_2.setEnabled(False)


	# COMPUTE GAMMA IF Z WAS INSERTED OTHERISE COMPUTE R IF GAMMA WAS INSERTED
	if self.radioButton_5.isChecked():
		# z was inserted
		try:
			gamma_L = S.calculate_gamma(ZL, Z0)
		except Exception as e:
			gamma_L = msg_error

		try:
			gamma_S = S.calculate_gamma(ZS, Z0)
		except Exception as e:
			gamma_S = msg_error
	else:
		# gamma was inserted
		try:
			ZL = S.calculate_Z_from_gamma(gamma_L, Z0)
		except Exception as e:
			ZL = msg_error
		try:
			ZS = S.calculate_Z_from_gamma(gamma_S, Z0)
		except Exception as e:
			ZS = msg_error



	try:
		gamma_in = S.calculate_gamma_in(s11, s12, s21, s22, ZL, Z0)
	except Exception as e:
		gamma_in = msg_error

	try:
		gamma_out = S.calculate_gamma_out(s11, s12, s21, s22, ZS, Z0)
	except Exception as e:
		gamma_out = msg_error


	try:
		Cs, rs = S.calculate_ISC(s11, s12, s21, s22)
	except Exception as e:
		Cs = rs = msg_error


	try:
		Cl, rl = S.calculate_OSC(s11, s12, s21, s22)
	except Exception as e:
		Cl = rl = msg_error



	try:
		GP = S.calculate_GP(s11, s12, s21, s22, ZL, Z0)
	except Exception as e:
		GP = msg_error

	try:
		GP_dB = to_dB(GP)
	except Exception as e:
		GP_dB = msg_error



	try:
		GT = S.calculate_GT(s11, s12, s21, s22, ZS, ZL, Z0)
	except Exception as e:
		GT = msg_error


	try:
		GT_dB = to_dB(GT)
	except Exception as e:
		GT_dB = msg_error


	try:
		GA = S.calculate_GA(s11, s12, s21, s22, ZS, Z0)
	except Exception as e:
		GA = msg_error


	try:
		GA_dB = to_dB(GA)
	except Exception as e:
		GA_dB = msg_error


	try:
		NF = S.calculate_NF(NF_opt_dB, R_n, gamma_s_on, ZS, Z0)
	except Exception as e:
		NF = msg_error

	try:
		if NF == "inf":
			NF_dB = "inf"
		else:
			NF_dB = to_dB(NF)
	except Exception as e:
		NF_dB = msg_error


	try:
		gamma_S_opt = S.calculate_gamma_S_opt(s11, s12, s21, s22)
	except Exception as e:
		gamma_S_opt = msg_error


	try:
		gamma_L_opt = S.calculate_gamma_L_opt(s11, s12, s21, s22)
	except Exception as e:
		gamma_L_opt = msg_error

	
	try:
		Z_S_opt = S.calculate_Z_from_gamma(gamma_S_opt, Z0)
	except Exception as e:
		Z_S_opt = msg_error

	try:
		Z_L_opt = S.calculate_Z_from_gamma(gamma_L_opt, Z0)
	except Exception as e:
		Z_L_opt = msg_error

	# if potentially unstable maximum gains are infinite and no optimum load/source is defined, so I hide those boxes.
	try:
		if abs(D) > 1 or K<1:
			GP_max_dB = GT_max_dB = GA_max_dB = "+inf"
			self.textBrowser_8.hide()
			self.label_262.hide()
			self.textBrowser_7.hide()
			self.label_248.hide()
			self.gamma_s_opt_box_5.hide()
			self.label_258.hide()
			self.gamma_L_opt_box_5.hide()
			self.label_251.hide()
			self.GAdb_box_2.setPlaceholderText("(-∞, ∞)")
			self.GTdb_box_2.setPlaceholderText("(-∞, ∞)")
			self.GPdb_box_2.setPlaceholderText("(-∞, ∞)")
		else:
			try:
				GP_max_dB = to_dB( S.calculate_GP(s11, s12, s21, s22, Z_L_opt, Z0) )
				self.GPdb_box_2.setPlaceholderText("(-∞, " + str(GP_max_dB) + ")")
			except Exception as e:
				self.GPdb_box_2.setPlaceholderText("")
				GP_max_dB = msg_error

			try:
				GT_max_dB = to_dB( S.calculate_GT(s11, s12, s21, s22, Z_S_opt, Z_L_opt, Z0) )
			except Exception as e:
				GT_max_dB = msg_error

			try:
				GA_max_dB = to_dB( S.calculate_GA(s11, s12, s21, s22, Z_S_opt, Z0) )
				self.GAdb_box_2.setPlaceholderText("(-∞, " + str(GA_max_dB) + ")")
			except Exception as e:
				self.GAdb_box_2.setPlaceholderText("")
				GA_max_dB = msg_error

			self.textBrowser_8.show()
			self.label_262.show()
			self.textBrowser_7.show()
			self.label_248.show()
			self.gamma_s_opt_box_5.show()
			self.label_258.show()
			self.gamma_L_opt_box_5.show()
			self.label_251.show()

	except Exception as e:
		pass
	

	
	#----------------------------

	try:
		Cnf, rnf = S.calculate_NF_circle(s11, s12, s21, s22, Z0, NF_circle_dB, gamma_s_on, NF_opt_dB, R_n)
	except Exception as e:
		Cnf = rnf = msg_error


	try:
		Ca, ra = S.calculate_GA_circle(s11, s12, s21, s22, Ga_circle_dB)
	except Exception as e:
		Ca = ra = msg_error


	try:
		Ct, rt = S.calculate_GT_circle(s11, s12, s21, s22, ZS, ZL, Z0, Gt_circle_dB)
	except Exception as e:
		Ct = rt = msg_error

	
	try:
		Cp, rp = S.calculate_GP_circle(s11, s12, s21, s22, Gp_circle_dB)
	except Exception as e:
		Cp = rp = msg_error


	try:
		gamma_intersection = int_points(Ca, ra, Cnf, rnf)
	except Exception as e:
		gamma_intersection = msg_error








	# --------------
	# displaying
	# --------------
	try:
		if abs(D) < 1:
			font_color = "green"
		else:
			font_color = "red"
		self.D_box_2.setText("<font color="+font_color+">" + str(abs(D)) + "∠" + str(math.degrees(cmath.phase(D))) + "</font>")
	except Exception as e:
		self.D_box_2.setText(msg_error)
	

	try:
		if K < 1:
			font_color = "red"
		else:
			font_color = "green"
		self.k_box_4.setText("<font color="+font_color+">" + str(K) + "</font>")
	except Exception as e:
		self.k_box_4.setText(msg_error)
	
	
	try:
		if abs(D) < 1 and K>1:
			self.label_31.setText("<b><font color='green'>Unconditionally stable system</font></b>")
		else:
			self.label_31.setText("<i>Potentially unstable system</i>")
	except Exception as e:
		self.label_31.setText(msg_error)

	self.ZS_box2.setText(str(ZS))
	self.ZL_box2.setText(str(ZL))
	
	try:
		gamma_L_visualized = str(abs(gamma_L)) + "∠" + str(math.degrees(cmath.phase(gamma_L)))
	except Exception as e:
		gamma_L_visualized = msg_error
	self.gamma_L_box.setText(gamma_L_visualized)

	try:
		gamma_S_visualized = str(abs(gamma_S)) + "∠" + str(math.degrees(cmath.phase(gamma_S)))
	except Exception as e:
		gamma_S_visualized = msg_error
	self.gamma_S_box.setText(gamma_S_visualized)

	try:
		if abs(gamma_in) > 1 and abs(gamma_out) > 1:
			self.label_31.setText("<b><font color='red'>Unstable system.</b> |Γ<sub>in</sub>| &gt; 1 and |Γ<sub>out</sub>| &gt; 1</font>")
		elif abs(gamma_in) > 1:
			self.label_31.setText("<b><font color='red'>Unstable system.</b> |Γ<sub>in</sub>| &gt; 1</font>")
		elif abs(gamma_out) > 1:
			self.label_31.setText("<b><font color='red'>Unstable system.</b> |Γ<sub>out</sub>| &gt; 1</font>")
		else:
			self.label_31.setText("<b><font color='green'>Stable system</font></b>")
	except Exception as e:
		pass


	try:
		t = str(abs(gamma_in)) + "∠" + str(math.degrees(cmath.phase(gamma_in))) 
		if abs(gamma_in) > 1:
			self.gamma_in_box_2.setText("<font color='red'>"+t+ "</font>")
		else:
			self.gamma_in_box_2.setText("<font color='green'>"+t+ "</font>")
	except Exception as e:
		pass
		self.gamma_in_box_2.setText(msg_error)
	

	try:
		t = str(abs(gamma_out)) + "∠" + str(math.degrees(cmath.phase(gamma_out))) 
		if abs(gamma_out) > 1:
			self.gamma_out_box_2.setText("<font color='red'>"+t+ "</font>")
		else:
			self.gamma_out_box_2.setText("<font color='green'>"+t+ "</font>")
	except Exception as e:
		pass
		self.gamma_out_box_2.setText(msg_error)
	

	try:
		self.C_box_13.setText(str(abs(Cs)) + "∠" + str(math.degrees(cmath.phase(Cs))) )
	except Exception as e:
		self.C_box_13.setText(msg_error)

	try:
		self.C_box_19.setText(str(rs))
	except Exception as e:
		self.C_box_19.setText(msg_error)

	try:
		self.C_box_16.setText(str(abs(Cl)) + "∠" + str(math.degrees(cmath.phase(Cl))) )
	except Exception as e:
		self.C_box_16.setText(msg_error)

	try:
		self.C_box_32.setText(str(rl))
	except Exception as e:
		self.C_box_32.setText(msg_error)






	try:
		self.GPdb_box2_8.setText(str(GP))
	except Exception as e:
		self.GPdb_box2_8.setText(msg_error)


	try:
		self.GPdb_box2_7.setText(str(GP_dB))
	except Exception as e:
		self.GPdb_box2_7.setText(msg_error)


	try:
		self.GTdb_box2_7.setText(str(GT))
	except Exception as e:
		self.GTdb_box2_7.setText(msg_error)


	try:
		self.GTdb_box2_8.setText(str(GT_dB))
	except Exception as e:
		self.GTdb_box2_8.setText(msg_error)


	try:
		self.GAdb_box2_7.setText(str(GA))
	except Exception as e:
		self.GAdb_box2_7.setText(msg_error)


	try:
		self.GAdb_box2_8.setText(str(GA_dB))
	except Exception as e:
		self.GAdb_box2_8.setText(msg_error)


	try:
		self.textBrowser_4.setText(str(NF))
	except Exception as e:
		self.textBrowser_4.setText(msg_error)


	try:
		self.textBrowser_5.setText(str(NF_dB))
	except Exception as e:
		self.textBrowser_5.setText(msg_error)


	try: 
		self.gamma_s_opt_box_5.setText(str(abs(gamma_S_opt)) + "∠" + str(math.degrees(cmath.phase(gamma_S_opt))) )
	except Exception as e:
		self.gamma_s_opt_box_5.setText(msg_error)


	try: 
		self.gamma_L_opt_box_5.setText(str(abs(gamma_L_opt)) + "∠" + str(math.degrees(cmath.phase(gamma_L_opt))) )
	except Exception as e:
		self.gamma_L_opt_box_5.setText(msg_error)


	try:
		self.textBrowser_8.setText(str(Z_S_opt))
	except Exception as e:
		self.textBrowser_8.setText(msg_error)

	try:
		self.textBrowser_7.setText(str(Z_L_opt))
	except Exception as e:
		self.textBrowser_7.setText(msg_error)


	try:
		self.textBrowser_2.setText(str(GA_max_dB))
	except Exception as e:
		self.textBrowser_2.setText(msg_error)


	try:
		self.textBrowser.setText(str(GP_max_dB))
	except Exception as e:
		self.textBrowser.setText(msg_error)

	try:
		self.textBrowser_3.setText(str(GT_max_dB))
	except Exception as e:
		self.textBrowser_3.setText(msg_error)





	try:
		self.C_box_43.setText(str(abs(Ca)) + "∠" + str(math.degrees(cmath.phase(Ca))) )
	except Exception as e:
		self.C_box_43.setText(msg_error)

	try:
		self.C_box_42.setText(str(ra))
	except Exception as e:
		self.C_box_42.setText(msg_error)


	try:
		self.C_box_37.setText(str(abs(Cnf)) + "∠" + str(math.degrees(cmath.phase(Cnf))) )
	except Exception as e:
		self.C_box_37.setText(msg_error)

	try:
		self.C_box_36.setText(str(rnf))
	except Exception as e:
		self.C_box_36.setText(msg_error)


	try:
		self.C_box_39.setText(str(abs(Cp)) + "∠" + str(math.degrees(cmath.phase(Cp))) )
	except Exception as e:
		self.C_box_39.setText(msg_error)

	try:
		self.C_box_38.setText(str(rp))
	except Exception as e:
		self.C_box_38.setText(msg_error)


	try:
		self.C_box_41.setText(str(abs(Ct)) + "∠" + str(math.degrees(cmath.phase(Ct))) )
	except Exception as e:
		self.C_box_41.setText(msg_error)

	try:
		self.C_box_40.setText(str(rt))
	except Exception as e:
		self.C_box_40.setText(msg_error)


	try:
		self.Gamma_S_int1_box.setText(str(abs(gamma_intersection[0])) + "∠" + str(math.degrees(cmath.phase(gamma_intersection[0]))) )
	except Exception as e:
		self.Gamma_S_int1_box.setText(msg_error)

	try:
		self.Gamma_S_int2_box.setText(str(abs(gamma_intersection[1])) + "∠" + str(math.degrees(cmath.phase(gamma_intersection[1]))) )
	except Exception as e:
		self.Gamma_S_int2_box.setText(msg_error)



	if self.radioButton_5.isChecked():
		label_gamma_inout = False # z is checked
	else:
		label_gamma_inout = True  # gamma is checked


	return (s11, s21, s12, s22,
			ZS, ZL, Z0,
			label_gamma_inout,
			gamma_S_visualized, gamma_L_visualized,
            gamma_in, gamma_out,
            Cs, rs,
            Cl, rl,
            NF_circle_dB, Cnf, rnf,
            Ga_circle_dB, Ca, ra,
            Gt_circle_dB, Ct, rt,
            Gp_circle_dB, Cp, rp
        )





def smith_plot_all(self):

	s11, s21, s12, s22, ZS, ZL, Z0, label_gamma_inout, gamma_S_visualized, gamma_L_visualized, gamma_in, gamma_out, Cs, rs, Cl, rl, NF_dB, Cnf, rnf, GA_dB, Ca, ra, GT_dB, Ct, rt, GP_dB, Cp, rp = compute_S_MRF571(self)
	vce, ic, f, bjt = fill_S_boxes(self)


	# constant_gamma_circle = 0.6
	constant_gamma_circle = msg_error

	try:
		import twoport.smithplot
		twoport.smithplot.plot_Smith(Cs, rs, 
                                     Cl, rl,
                                     gamma_in, gamma_out, 
                                     GA_dB, Ca, ra, 
                                     NF_dB, Cnf, rnf,
                                     GT_dB, Ct, rt, 
                                     GP_dB, Cp, rp,
                                     constant_gamma_circle,
                                     ZS, ZL, Z0,
                                     gamma_S_visualized, gamma_L_visualized,
                                     label_gamma_inout,
                                     vce, ic, f, bjt
                                )
	except Exception as e:
		raise e





def open_datasheet(self):
	try:
		if sys.platform == "linux":
			os.system("xdg-open MRF57/MRF57.pdf")
		elif sys.platform == "darwin": # mac
			os.system("open MRF57/MRF57.pdf")
		elif sys.platform[:3] == "win": # sys.platform on windows actually returns win32 
			os.system('start "" "MRF57/MRF57.pdf"')
	except Exception as e:
		print ("Can't open the datasheet.")



def clean_S_MRF571(self):
	self.ZS_box.setText("")
	self.ZL_box.setText("")
	self.Calculate_button_5.click()
	self.ZS_box.setFocus()

def clean_all_S_MRF571(self):
	self.s11_box.setText("")
	self.s21_box.setText("")
	self.s12_box.setText("")
	self.s22_box.setText("")
	self.Z0_box.setText("")

	self.vce_box.setText("")
	self.ic_box.setText("")
	self.f_box.setText("")
	self.Calculate_button_5.click()
	self.vce_box.setFocus()



def disable_enable_Z_or_gamma_input(self):
	if self.radioButton_5.isChecked():
		self.label_196.setEnabled(True)
		self.ZS_box.setEnabled(True)
		self.label_26.setEnabled(True)
		self.label_197.setEnabled(True)
		self.ZL_box.setEnabled(True)
		self.label_25.setEnabled(True)

		self.label_250.setEnabled(False)
		self.ZS_box_2.setEnabled(False)
		self.label_257.setEnabled(False)
		self.ZS_box_5.setEnabled(False)
		self.label_264.setEnabled(False)
		self.ZS_box_4.setEnabled(False)
		self.label_265.setEnabled(False)
		self.ZS_box_3.setEnabled(False)
		self.ZS_box.setFocus()
	else:
		self.label_196.setEnabled(False)
		self.ZS_box.setEnabled(False)
		self.label_26.setEnabled(False)
		self.label_197.setEnabled(False)
		self.ZL_box.setEnabled(False)
		self.label_25.setEnabled(False)

		self.label_250.setEnabled(True)
		self.ZS_box_2.setEnabled(True)
		self.label_257.setEnabled(True)
		self.ZS_box_5.setEnabled(True)
		self.label_264.setEnabled(True)
		self.ZS_box_4.setEnabled(True)
		self.label_265.setEnabled(True)
		self.ZS_box_3.setEnabled(True)
		self.ZS_box_2.setFocus()

def disable_MRF57(self):
	if not self.checkBox_2.isChecked():
		self.radioButton_MRF571.setEnabled(False)
		self.radioButton_MRF572.setEnabled(False)
		self.label_185.setEnabled(False)
		self.vce_box.setEnabled(False)
		self.label_186.setEnabled(False)
		self.label_187.setEnabled(False)
		self.ic_box.setEnabled(False)
		self.label_188.setEnabled(False)
		self.label_189.setEnabled(False)
		self.f_box.setEnabled(False)
		self.label_190.setEnabled(False)
		self.s11_box.setFocus()
	else:
		self.radioButton_MRF571.setEnabled(True)
		self.radioButton_MRF572.setEnabled(True)
		self.label_185.setEnabled(True)
		self.vce_box.setEnabled(True)
		self.label_186.setEnabled(True)
		self.label_187.setEnabled(True)
		self.ic_box.setEnabled(True)
		self.label_188.setEnabled(True)
		self.label_189.setEnabled(True)
		self.f_box.setEnabled(True)
		self.label_190.setEnabled(True)
		self.vce_box.setFocus()

		