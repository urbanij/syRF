#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:38:35 2018

@author         : francescourbani
@description    : fast prototype of functions

RF Electronics class, Spring 2018
"""


import numpy as np
import cmath

y_i = complex(input(">>> y_i = "))
y_f = complex(input(">>> y_f = "))
y_r = complex(input(">>> y_r = "))
y_o = complex(input(">>> y_o = "))

y_s = complex(input(">>> y_s = "))
y_L = complex(input(">>> y_L = "))


Y = np.matrix([[y_i, y_r], [y_f, y_o]])
print()
# print ("Y = ")
# print (Y)
print()


C = (abs(y_r * y_f)) / (2 * y_i.real * y_o.real - (y_r * y_f).real)
beta_A = (y_f * y_r) / ((y_i + y_s) * (y_o + y_L))
beta_A_polar = cmath.polar(beta_A)
y_in = y_i - (y_r * y_f) / (y_o + y_L)
y_out = y_o - (y_f * y_r) / (y_i + y_s)
G_A = (abs(y_f) ** 2 * y_s.real) / (
    (y_o * y_s + y_o * y_i - y_r * y_f) * (y_i + y_s).conjugate()
).real
G_P = ((abs(y_f) ** 2) / (abs(y_o + y_L) ** 2)) * (y_L.real) / (y_in.real)
G_T = (4 * y_s.real * y_L.real * abs(y_f) ** 2) / abs(
    (y_s + y_i) * (y_o + y_L) - y_r * y_f
) ** 2
k = (2 * (y_i.real + y_s.real) * (y_o.real + y_L.real)) / (
    (y_r * y_f).real + abs(y_r * y_f)
)

g_s_opt = (
    (2 * y_i.real * y_o.real - (y_r * y_f).real) ** 2 - abs(y_r * y_f) ** 2
) ** 0.5 / (2 * y_o.real)
b_s_opt = -y_i.imag + (y_r * y_f).imag / (2 * y_o.real)
y_s_opt = g_s_opt + b_s_opt * 1j

g_L_opt = (g_s_opt * y_o.real) / (y_i.real)
b_L_opt = -y_o.imag + (y_r * y_f).imag / (2 * y_i.real)
y_L_opt = g_L_opt + b_L_opt * 1j


print("C       = " + str(C))
print(
    "beta*A  = "
    + str(beta_A)
    + " = "
    + str(beta_A_polar[0])
    + "∠"
    + str(beta_A_polar[1])
    + " rad"
)
print("y_in    = " + str(y_in))
print("y_out   = " + str(y_out))
print("G_A     = " + str(G_A))
print("G_P     = " + str(G_P))
print("G_T     = " + str(G_T))
print("k       = " + str(k))
print("y_s_opt = " + str(y_s_opt))
print("y_L_opt = " + str(y_L_opt))
print()
print()
print()
