#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri May 11 17:05:54 CEST 2018

@author(s)   : Francesco Urbani
@file        : quarter-wave-matching.py
@descritpion : 

"""

msg_error = "" # display nothing if error occurs



def calculate_z_lambda4(self):

	# read inputs
	try:
		z_norm_1 = float(self.z1_box.text())
	except Exception as e:
		z_norm_1 = msg_error

	try:
		z_norm_2 = float(self.z2_box.text())
	except Exception as e:
		z_norm_2 = msg_error
	
	try:
		z0 = float(self.Z0_box2_2.text())
	except Exception as e:
		z0 = msg_error



	# compute
	try:
		z = (z_norm_1*z_norm_2)**0.5
	except Exception as e:
		z = msg_error

	try:
		Z = z*z0
	except Exception as e:
		Z = msg_error



	# display
	self.zbox111.setText(str(z))
	self.Zbox111.setText(str(Z))




