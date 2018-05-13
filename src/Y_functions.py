#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Apr 17 08:51:12 2018

@author(s)   : francescourbani
@file        : Y_functions.py
@descritpion : Functions used into Y tab.

"""

import cmath
import math


def calculate_C(y_i, y_f, y_o, y_r):
	return ( abs(y_r*y_f) ) / ( 2*y_i.real*y_o.real - (y_r*y_f).real )

def calculate_betaA(y_i, y_f, y_o, y_r, y_s, y_L):
	return ( (y_f*y_r)/( (y_i+y_s)*(y_o+y_L) ) )

def calculate_y_in(y_i, y_f, y_o, y_r, y_s, y_L):
	return ( y_i - (y_r*y_f)/(y_o + y_L) )

def calculate_y_out(y_i, y_f, y_o, y_r, y_s, y_L):
	return ( y_o - (y_f*y_r)/(y_i+y_s) )

def calculate_A_V(y_f, y_o, y_L):
	# calculate A_V (voltage gain)
	return ( -y_f/(y_o + y_L) )

def calculate_vout_over_vs(y_i, y_f, y_o, y_r, y_s, y_L):
	# change y from mS to S
	y_i *= 1e-3
	y_f *= 1e-3
	y_o *= 1e-3
	y_r *= 1e-3
	y_s *= 1e-3
	y_L *= 1e-3

	if y_s == 0:
		# rs -> infty
		v1_over_vs = 0
	elif y_L == 0:
		# rl -> infty
		rs = 1/y_s
		v1_over_vs = 1/(1+rs*y_i-rs*y_f*y_r*(1/y_o))
	else:
		rs = 1/y_s # ohm
		rl = 1/y_L # ohm
		v1_over_vs = ( 1+rl*y_o )/( (1+rs*y_i)*(1+rl*y_o) - y_f*y_r*rl*rs)
	
	vout_over_vs = calculate_A_V(y_f, y_o, y_L) * v1_over_vs
	return vout_over_vs
	

def calculate_G_A(y_i, y_f, y_o, y_r, y_s, y_L):
	return ( abs(y_f)**2 * y_s.real ) / ( (y_o*y_s + y_o*y_i - y_r*y_f)*(y_i+y_s).conjugate() ).real

def calculate_G_P(y_i, y_f, y_o, y_r, y_s, y_L, y_in):
	return ( (abs(y_f)**2) / (abs(y_o+y_L)**2) ) * (y_L.real)/(y_in.real)

def calculate_G_T(y_i, y_f, y_o, y_r, y_s, y_L):
	return ( 4*y_s.real*y_L.real*abs(y_f)**2)/abs((y_s+y_i)*(y_o+y_L)-y_r*y_f)**2

def calculate_k(y_i, y_f, y_o, y_r, y_s, y_L):
	return ( 2*(y_i.real+y_s.real)*(y_o.real+y_L.real) )/ ( (y_r*y_f).real + abs(y_r*y_f) )



def calculate_g_s_opt(y_i, y_f, y_o, y_r):
	g_s_opt = ((2*y_i.real*y_o.real - (y_r*y_f).real)**2 - abs(y_r*y_f)**2)**0.5/(2*y_o.real)
	return g_s_opt


def calculate_y_s_opt(y_i, y_f, y_o, y_r):
	g_s_opt = calculate_g_s_opt(y_i, y_f, y_o, y_r)
	b_s_opt = -y_i.imag + (y_r*y_f).imag/(2*y_o.real)
	y_s_opt = g_s_opt + b_s_opt*1j 
	return y_s_opt

def calculate_y_L_opt(y_i, y_f, y_o, y_r):
	g_s_opt = calculate_g_s_opt(y_i, y_f, y_o, y_r)
	g_L_opt = (g_s_opt*y_o.real)/(y_i.real)
	b_L_opt = -y_o.imag + (y_r*y_f).imag/(2*y_i.real)
	y_L_opt = g_L_opt + b_L_opt*1j
	return y_L_opt

	



