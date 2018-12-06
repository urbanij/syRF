#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Apr 17 08:59:08 2018

@author(s)   : francescourbani
@file        : S_functions.py
@descritpion : Functions used into S tab

"""

import cmath
import math
from twoport.utils import un_db


def calculate_D(s11, s12, s21, s22):
	return (s11*s22 - s12*s21)

def calculate_K(s11, s12, s21, s22):
	D = calculate_D(s11, s12, s21, s22)
	# print ("K = ")
	# print (1-abs(s11)**2-abs(s22)**2+abs(D)**2)/(2*abs(s12*s21))
	return (1-abs(s11)**2-abs(s22)**2+abs(D)**2)/(2*abs(s12*s21))

def calculate_gamma(zl, z0):
	return (zl-z0)/(zl+z0)

def calculate_gamma_in(s11, s12, s21, s22, zl, z0):
	gamma_L = calculate_gamma(zl, z0)
	return ( s11 + (s12*s21*gamma_L)/(1 - s22*gamma_L) )

def calculate_gamma_out(s11, s12, s21, s22, zs, z0):
	gamma_S = calculate_gamma(zs, z0)
	return ( s22 + (s21*s12*gamma_S)/(1 - s11*gamma_S) )


def calculate_ISC(s11, s12, s21, s22):
	D = calculate_D(s11, s12, s21, s22)
	Cs = ( (s11 - s22.conjugate()*D).conjugate()/(abs(s11)**2 - abs(D)**2) )
	rs = ( abs(s12*s21)/(abs(abs(D)**2 - abs(s11)**2)) )
	return Cs, rs


def calculate_OSC(s11, s12, s21, s22):
	D = calculate_D(s11, s12, s21, s22)
	Cl = ( (s22 - s11.conjugate()*D).conjugate()/(abs(s22)**2 - abs(D)**2) )
	rl = ( abs(s12*s21)/(abs(abs(D)**2 - abs(s22)**2)) )
	return Cl, rl


def calculate_GP(s11, s12, s21, s22, zl, z0):
	gamma_L = calculate_gamma(zl, z0)
	gamma_in = calculate_gamma_in(s11, s12, s21, s22, zl, z0)
	return ((abs(s21))**2/(abs(1-s22*gamma_L))**2)*((1-abs(gamma_L)**2)/(1-abs(gamma_in)**2))


def calculate_GT(s11, s12, s21, s22, zs, zl, z0):
	gamma_S = calculate_gamma(zs, z0)
	gamma_L = calculate_gamma(zl, z0)
	gamma_out = calculate_gamma_out(s11, s12, s21, s22, zs, z0)
	return ((1-abs(gamma_S)**2)*(abs(s21)**2)*(1-abs(gamma_L)**2))/((abs(1-gamma_out*gamma_L)**2) * (abs(1-s11*gamma_S)**2))


def calculate_GA(s11, s12, s21, s22, zs, z0):
	gamma_S = calculate_gamma(zs, z0)
	gamma_out = calculate_gamma_out(s11, s12, s21, s22, zs, z0)
	return ((abs(s21))**2/(abs(1-s11*gamma_S))**2)*((1-abs(gamma_S)**2)/(1-abs(gamma_out)**2))	


def calculate_NF(NFmin_db, Rn, gamma_s_on, zs, z0):
	NFmin = un_db(NFmin_db)
	rn = Rn/z0
	gamma_S = calculate_gamma(zs, z0)
	if abs(gamma_S) == 1:
		return "inf"
	NF = NFmin + (4*rn*abs(gamma_S - gamma_s_on)**2)/((1-abs(gamma_S)**2)*abs(1+gamma_s_on)**2)
	return NF






def calculate_Ni(NF_dB, NFmin_db, gamma_s_on, Rn, z0):
	# Note: NF_circle_dB is in dB
	NF = un_db(NF_dB)
	NFmin = un_db(NFmin_db)
	rn = Rn/z0
	return ( ((NF-NFmin)*abs(1+gamma_s_on)**2)/(4*rn) )

def calculate_NF_circle(s11, s12, s21, s22, z0, NF_circle_dB, gamma_s_on, NF_opt_dB, Rn):
	Ni = calculate_Ni(NF_circle_dB, NF_opt_dB, gamma_s_on, Rn, z0)
	Cnf = gamma_s_on/(1+Ni)
	rnf = ( (Ni*(1+Ni-abs(gamma_s_on)**2))/(1+Ni)**2 )**0.5
	return Cnf, rnf



def calculate_GA_circle(s11, s12, s21, s22, Ga_circle_dB):
	ga = un_db(Ga_circle_dB)/abs(s21)**2
	D = calculate_D(s11, s12, s21, s22)
	K = calculate_K(s11, s12, s21, s22)
	Ca = (ga*(s11-s22.conjugate()*D).conjugate())/(1+ga*(abs(s11)**2-abs(D)**2))
	ra = ((1-2*K*abs(s12*s21)*ga + ga**2*abs(s12*s21)**2)**0.5)/(abs(1+ga*(abs(s11)**2 - abs(D)**2)))
	return Ca, ra



def calculate_GP_circle(s11, s12, s21, s22, Gp_circle_dB):
	gp = un_db(Gp_circle_dB)/abs(s21)**2
	D = calculate_D(s11, s12, s21, s22)
	K = calculate_K(s11, s12, s21, s22)
	Cp = (gp*(s22-s11.conjugate()*D).conjugate())/(1+gp*(abs(s22)**2-abs(D)**2))
	rp = ((1-2*K*abs(s12*s21)*gp + gp**2*abs(s12*s21)**2)**0.5)/(abs(1+gp*(abs(s22)**2 - abs(D)**2)))
	return Cp, rp


def calculate_GTi(Gt_circle_dB, s11, s21, zs, z0):
	gamma_S = calculate_gamma(zs, z0)
	Gt_circle = un_db(Gt_circle_dB)
	return (Gt_circle*abs(1-s11*gamma_S)**2)/((1-abs(gamma_S)**2)*abs(s21)**2)


def calculate_GT_circle(s11, s12, s21, s22, zs, zl, z0, Gt_circle_dB):
	GTi = calculate_GTi(Gt_circle_dB, s11, s21, zs, z0)
	gamma_out = calculate_gamma_out(s11, s12, s21, s22, zs, z0)
	Ct = ( GTi * gamma_out.conjugate() )/(GTi*abs(gamma_out)**2 + 1)
	rt = ( (GTi**2 * abs(gamma_out)**2)/(GTi*abs(gamma_out)**2 + 1)**2 + (1-GTi)/(GTi*abs(gamma_out)**2 + 1) )**0.5
	return Ct, rt


def calculate_gamma_S_opt(s11, s12, s21, s22):
	D  = calculate_D(s11, s12, s21, s22)
	B1 = 1 - abs(s22)**2 + abs(s11)**2 - abs(D)**2
	C1 = s11 - s22.conjugate() * D
	abs_gamma_S_opt   = B1/(2*abs(C1)) - ((B1**2 - 4*abs(C1)**2)/(4*abs(C1)**2))**0.5
	phase_gamma_S_opt = cmath.phase( C1.conjugate() )
	gamma_S_opt = cmath.rect(abs_gamma_S_opt, phase_gamma_S_opt)
	return gamma_S_opt



def calculate_gamma_L_opt(s11, s12, s21, s22):
	D  = calculate_D(s11, s12, s21, s22)
	B2 = 1 - abs(s11)**2 + abs(s22)**2 - abs(D)**2
	C2 = s22 - s11.conjugate() * D
	abs_gamma_L_opt   = B2/(2*abs(C2)) - ((B2**2 - 4*abs(C2)**2)/(4*abs(C2)**2))**0.5
	phase_gamma_L_opt = cmath.phase( C2.conjugate() )
	gamma_L_opt = cmath.rect(abs_gamma_L_opt, phase_gamma_L_opt)
	return gamma_L_opt


def calculate_Z_from_gamma(gamma, z0):
	return z0 * ((1+gamma)/(1-gamma))


	

