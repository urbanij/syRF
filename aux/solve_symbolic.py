#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:38:35 2018

@author: francescourbani

RF Electronics class, Spring 2018
"""

import sympy

X   = sympy.symbols('X', real=True)
B   = sympy.symbols('B', real=True)
R_L = sympy.symbols('R_L', real=True)
X_L = sympy.symbols('X_L', real=True)



#------------------------------------------------------------------------------------------

# solve shunt - series (down conversion)

Z_0 = sympy.simplify( X*1j + 1/(B*1j + 1/(R_L+X_L*1j)) )


print ("-"*40)
print ()

print ("solving shunt-series configuration:")
print ("Z_0 = ")
print (Z_0)
R_0, X_0 = Z_0.as_real_imag()

print ()
print ("R_0 = ")
print (R_0)
# R_L/((R_L**2 + 1.0*X_L**2)*(R_L**2/(R_L**2 + 1.0*X_L**2)**2 + (1.0*B - 1.0*X_L/(R_L**2 + 1.0*X_L**2))**2))

print ()
print ("X_0 = ")
print (X_0)
# 1.0*X + (-1.0*B + 1.0*X_L/(R_L**2 + 1.0*X_L**2))/(R_L**2/(R_L**2 + 1.0*X_L**2)**2 + (1.0*B - 1.0*X_L/(R_L**2 + 1.0*X_L**2))**2)



#------------------------------------------------------------------------------------------


# solve series - shunt (up conversion)
Z_0 = sympy.simplify( 1/(B*1j + 1/(X*1j + R_L + X_L*1j) ) )


print ("-"*40)
print ("solving series-shunt configuration:")
print ("Z_0 = ")
print (Z_0)
R_0, X_0 = Z_0.as_real_imag()



print ()
print ("R_0 = ")
print (R_0)
# 1.0*B*R_L*(X + X_L)/(B**2*R_L**2 + (-B*X - B*X_L + 1)**2) + 1.0*R_L*(-B*X - B*X_L + 1)/(B**2*R_L**2 + (-B*X - B*X_L + 1)**2)

print ()
print ("X_0 = ")
print (X_0)
# -1.0*B*R_L**2/(B**2*R_L**2 + (-B*X - B*X_L + 1)**2) + 1.0*(X + X_L)*(-B*X - B*X_L + 1)/(B**2*R_L**2 + (-B*X - B*X_L + 1)**2)

print ("-"*40)

