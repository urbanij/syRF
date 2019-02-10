#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Apr 23 22:02:42 2018

@author(s)   : Francesco Urbani
@file        : plot_epsilon_r_graphs.py
@descritpion : Contains the data interpolated used to plot 
               the common base parameters,
               and a function to retrive them but unused.

"""

import os
from io import StringIO  
import numpy as np
import matplotlib.pyplot as plt



# this function won't actually be used.
def calculate_epsilon_r_1():
    # PATH may need to be changed
    PATH = "microstrip_matching/1_z0_over_whratio/"


    with open(PATH + "er1.csv", "r") as f:
        er1=f.read()

    # convert c into another suitable format
    c = StringIO(er1)
    # load c into x and y numpy arrays
    x1, er1 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)


    with open(PATH + "er2.csv", "r") as f:
        er2=f.read()
    c = StringIO(er2)
    x2, er2 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

        
    with open(PATH + "er4.csv", "r") as f:
        er4=f.read()

    c = StringIO(er4)
    x4, er4 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er6.csv", "r") as f:
        er6=f.read()
    c = StringIO(er6)
    x6, er6 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er8.csv", "r") as f:
        er8=f.read()
    c = StringIO(er8)
    x8, er8 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er10.csv", "r") as f:
        er10=f.read()
    c = StringIO(er10)
    x10, er10 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er12.csv", "r") as f:
        er12=f.read()
    c = StringIO(er12)
    x12, er12 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er16.csv", "r") as f:
        er16=f.read()
    c = StringIO(er16)
    x16, er16 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    return (x1, er1, x2, er2, x4, er4, x6, er6, x8, er8, x10, er10, x12, er12, x16, er16)



def calculate_epsilon_r_2():
    # PATH may need to be changed
    PATH = "microstrip_matching/2_lambda_over_whratio/"


    with open(PATH + "er2_2.csv", "r") as f:
        er2=f.read()
    c = StringIO(er2)
    x2, er2 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)


    with open(PATH + "er4_2.csv", "r") as f:
        er4=f.read()
    c = StringIO(er4)
    x4, er4 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er6_2.csv", "r") as f:
        er6=f.read()
    c = StringIO(er6)
    x6, er6 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er8_2.csv", "r") as f:
        er8=f.read()
    c = StringIO(er8)
    x8, er8 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er10_2.csv", "r") as f:
        er10=f.read()
    c = StringIO(er10)
    x10, er10 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    with open(PATH + "er12_2.csv", "r") as f:
        er12=f.read()
    c = StringIO(er12)
    x12, er12 = np.loadtxt(c, delimiter=',', usecols=(0, 1), unpack=True)

    return (x2, er2, x4, er4, x6, er6, x8, er8, x10, er10, x12, er12)





def visualize_z0_over_whratio(x1, er1, x2, er2, x4, er4, x6, er6, x8, er8, x10, er10, x12, er12, x16, er16, x2_2, er2_2, x4_2, er4_2, x6_2, er6_2, x8_2, er8_2, x10_2, er10_2, x12_2, er12_2):

    # plot it
    plt.figure()



    plt.subplots_adjust(top=0.945) 
    plt.subplots_adjust(bottom=0.09)
    plt.subplots_adjust(left=0.33) 
    plt.subplots_adjust(right=0.68) 
    plt.subplots_adjust(hspace=0.2)
    plt.subplots_adjust(wspace=0.2) 




    plt.subplot(211)
    # plt.subplot(211, aspect = 'equal')
    
    # plt.plot(x1, er1, label="$\\varepsilon_r = 1$")
    plt.plot(x2, er2, label="$\\varepsilon_r = 2$")
    plt.plot(x4, er4, label="$\\varepsilon_r = 4$")
    plt.plot(x6, er6, label="$\\varepsilon_r = 6$")
    plt.plot(x8, er8, label="$\\varepsilon_r = 8$")
    plt.plot(x10, er10, label="$\\varepsilon_r = 10$")
    plt.plot(x12, er12, label="$\\varepsilon_r = 12$")
    # plt.plot(x1, er1, label="$\\varepsilon_r = 1$")
    # plt.plot(x16, er16, label="$\\varepsilon_r = 16$")
    plt.grid(True,which="both",ls="-")
    plt.xlim(0.1, 10)
    # plt.ylim(3, 1000)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.ylabel("$Z_0\ (\Omega)$")#.set_rotation(0)


    plt.subplot(212)
    plt.plot(x2_2, er2_2, label="$\\varepsilon_r = 2$")
    plt.plot(x4_2, er4_2, label="$\\varepsilon_r = 4$")
    plt.plot(x6_2, er6_2, label="$\\varepsilon_r = 6$")
    plt.plot(x8_2, er8_2, label="$\\varepsilon_r = 8$")
    plt.plot(x10_2, er10_2, label="$\\varepsilon_r = 10$")
    plt.plot(x12_2, er12_2, label="$\\varepsilon_r = 12$")
    plt.grid(True,which="both",ls="-")
    plt.xlim(0.1, 10)
    plt.ylim(1, 1.3)
    plt.xscale('log')
    plt.legend()
    plt.ylabel("$\\frac{\lambda}{\lambda_{TEM}}$")#.set_rotation(0)
    plt.xlabel("$w/h$")
    # plt.suptitle("")

    plt.show()



x1, er1, x2, er2, x4, er4, x6, er6, x8, er8, x10, er10, x12, er12, x16, er16     = calculate_epsilon_r_1()
x2_2, er2_2, x4_2, er4_2, x6_2, er6_2, x8_2, er8_2, x10_2, er10_2, x12_2, er12_2 = calculate_epsilon_r_2()

# visualize_z0_over_whratio(x1, er1, x2, er2, x4, er4, x6, er6, x8, er8, x10, er10, x12, er12, x16, er16, x2_2, er2_2, x4_2, er4_2, x6_2, er6_2, x8_2, er8_2, x10_2, er10_2, x12_2, er12_2)


