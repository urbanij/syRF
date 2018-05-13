#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 19 15:38:35 2018

@author(s)   : francescourbani
@file        : LC_matching_tab.py
@descritpion : 

"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

msg_error = "" # display nothing if error occurs
# msg_error = "<font color='#E8E8E8'>ERR</font>"



def compute_LC_matching(self):

	rv=[] # eventually it will contain all the variables needed to plot gamma


	# read frequency
	try:
		f0 = float(self.f0_box.text())
		f0 = f0*1e6 # MHz / Hz conversion
	except Exception as e:
		f0 = 0

	
	# read input impedance/admittance
	input_unit = self.comboBox.currentText()
	try:
		input_impedance = complex(self.input_box.text())
		if input_unit == "Admittance [mS]":
			input_admittance = input_impedance
			input_impedance  = (input_admittance*1e-3)**(-1)
		else:
			# input_admittance in mS
			input_admittance = input_impedance**(-1)*1e3 # 1e3 shifts from S to mS
	except Exception as e:
		input_impedance  = msg_error
		input_admittance = msg_error


	# read output impedance/admittance
	output_unit = self.comboBox_2.currentText()
	try:
		output_impedance = complex(self.output_box.text())
		if output_unit == "Admittance [mS]":
			output_admittance = output_impedance
			output_impedance  = (output_admittance*1e-3)**(-1)
		else:
			output_admittance = output_impedance**(-1)*1e3
	except Exception as e:
		output_impedance  = msg_error
		output_admittance = msg_error


	self.label_18.setText("")
	X1 = msg_error
	B1 = msg_error
	X2 = msg_error
	B2 = msg_error

	try:
		Z_L = input_impedance
		R_L = Z_L.real
		X_L = Z_L.imag
		if R_L == 0:
			self.label_18.setText("<i><font color=#F00>Matching can't be established.</font></i>")
		Z_0 = output_impedance
		R_0 = Z_0.real
		X_0 = Z_0.imag
		if R_0 == 0:
			self.label_18.setText("<i><font color=#F00>Matching can't be established.</font></i>")		
		
		if R_L != 0 and R_0 != 0:

			if R_L > R_0:
				self.label_18.setText("<i><b>Down coversion</b> (B shunt - X series)</i>")
				
				# matlab results
				# shunt - series config
				X1 = (R_0*(X_L + ((R_L*(R_L**2 - R_0*R_L + X_L**2))/R_0)**(1/2)))/R_L - (R_0*X_L + R_L*X_0)/R_L
				X2 = (R_0*(X_L - ((R_L*(R_L**2 - R_0*R_L + X_L**2))/R_0)**(1/2)))/R_L - (R_0*X_L + R_L*X_0)/R_L
				 
				B1 = (X_L + ((R_L*(R_L**2 - R_0*R_L + X_L**2))/R_0)**(1/2))/(R_L**2 + X_L**2)
				B2 = (X_L - ((R_L*(R_L**2 - R_0*R_L + X_L**2))/R_0)**(1/2))/(R_L**2 + X_L**2)


			elif R_L <= R_0:
				self.label_18.setText("<i><b>Up conversion</b> (X series - B shunt)</i>")

				# matlab results
				# series - shunt config
				X1 = (R_L*(X_0 + ((R_0*(R_0**2 - R_L*R_0 + X_0**2))/R_L)**(1/2)))/R_0 - (R_0*X_L + R_L*X_0)/R_0
				X2 = (R_L*(X_0 - ((R_0*(R_0**2 - R_L*R_0 + X_0**2))/R_L)**(1/2)))/R_0 - (R_0*X_L + R_L*X_0)/R_0

				B1 = (X_0 + ((R_0*(R_0**2 - R_L*R_0 + X_0**2))/R_L)**(1/2))/(R_0**2 + X_0**2)
				B2 = (X_0 - ((R_0*(R_0**2 - R_L*R_0 + X_0**2))/R_L)**(1/2))/(R_0**2 + X_0**2)


	except Exception as e:
		pass
		


	self.imp_input_box.setText(str(input_impedance))
	self.adm_input_box.setText(str(input_admittance))
	self.imp_output_box.setText(str(output_impedance))
	self.adm_output_box.setText(str(output_admittance))

	self.X1_box.setText(str(X1))
	self.X2_box.setText(str(X2))
	try:
		self.B1_box.setText(str(B1*1e3)) # B1 in mS instead of S
		self.B2_box.setText(str(B2*1e3)) # B2 in mS instead of S
	except Exception as e:
		self.B1_box.setText(msg_error)
		self.B2_box.setText(msg_error)

	
	
	try:
		if X1 >= 0:
			L1 = X1/(2*np.pi*f0)
		else:
			C1 = -1/(2*np.pi*f0*X1)

		if X2 >= 0:
			L2 = X2/(2*np.pi*f0)
		else:
			C2 = -1/(2*np.pi*f0*X2)

		if B1 >= 0:
			C1 = B1/(2*np.pi*f0)
		else:
			L1 = -1/(2*np.pi*f0*B1)

		if B2 >= 0:
			C2 = B2/(2*np.pi*f0)
		else:
			L2 = -1/(2*np.pi*f0*B2)

	except Exception as e:
		L1 = msg_error
		C1 = msg_error
		L2 = msg_error
		C2 = msg_error


	try:
		rv = [f0, Z_L, Z_0, L1, C1, L2, C2]	
	except Exception as e:
		pass
	

	L1um = ""
	L2um = ""
	C1um = ""
	C2um = ""

	try:
		if abs(L1)<1e-12:
			L1um = 'f'
			L1 *= 1e15
		elif abs(L1)<1e-9:
			L1um = 'p'
			L1 *= 1e12
		elif abs(L1)<1e-6:
			L1um = 'n'
			L1 *= 1e9
		elif abs(L1)<1e-3:
			L1um = 'u'
			L1 *= 1e6

		if abs(L2)<1e-12:
			L2um = 'f'
			L2 *= 1e15
		elif abs(L2)<1e-9:
			L2um = 'p'
			L2 *= 1e12
		elif abs(L2)<1e-6:
			L2um = 'n'
			L2 *= 1e9
		elif abs(L2)<1e-3:
			L2um = 'u'
			L2 *= 1e6

		if abs(C1)<1e-12:
			C1um = 'f'
			C1 *= 1e15
		elif abs(C1)<1e-9:
			C1um = 'p'
			C1 *= 1e12
		elif abs(C1)<1e-6:
			C1um = 'n'
			C1 *= 1e9
		elif abs(C1)<1e-3:
			C1um = 'u'
			C1 *= 1e6

		if abs(C2)<1e-12:
			C2um = 'f'
			C2 *= 1e15
		elif abs(C2)<1e-9:
			C2um = 'p'
			C2 *= 1e12
		elif abs(C2)<1e-6:
			C2um = 'n'
			C2 *= 1e9
		elif abs(C2)<1e-3:
			C2um = 'u'
			C2 *= 1e6

		self.label_112.setText(L1um+'H') # L1 unit measure label
		self.label_113.setText(C1um+'F') # C1 unit measure label
		self.label_116.setText(L2um+'H') # L2 unit measure label
		self.label_117.setText(C2um+'F') # C2 unit measure label

		# enable gamma plot if f0 is not empty.
		# actually this works only the first time, if f0 is inserted and cleared this
		# does not work anymore. Should find a better way with a check box content.
		self.plot.setEnabled(True)
	except Exception as e:
		pass
	


	try:
		self.L1_box.setText(str(L1))
		self.C1_box.setText(str(C1))
		self.L2_box.setText(str(L2))
		self.C2_box.setText(str(C2))

	except Exception as e:
		pass


	# return the list containing the variables needed for plotting gamma.
	return rv



def clean_all_LC_matching(self):
	self.f0_box.setText("")
	self.input_box.setText("")
	self.output_box.setText("")
	self.input_box.setFocus()




# not yet used
def to_eng_form(x):
	si_prefixes = {9:'P', 9:'G', 6:'M', 3:'k', 0:'', -3:'m', -6:'u', -9:'n', -12:'p', -15:'f'}
	for e in sorted(si_prefixes, reverse=True):
		if x >= 10**e:
			return x/10**e, si_prefixes[e]
	return x, ''
