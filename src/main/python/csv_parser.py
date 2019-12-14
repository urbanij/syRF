#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 19 15:38:35 2018

@author(s)   : Francesco Urbani
@file        : csv_parser.py
@descritpion : This file retrieves the data from MRF57/MRF571.csv used in S_tab

"""

import csv
import math
import cmath

def get_S_parameters(Vce, Ic, f, bjt):

    # bjt parameter has to be either MRF571 or MRF572

    if (bjt != "MRF571" and bjt != "MRF572"):
        print ("ERROR")
        quit()

    path = "src/main/python/MRF57/"
    
    with open(path + bjt.upper() +".csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)

        # skip the first 2 rows since it's the header
        next(csv_reader)
        next(csv_reader)

        for line in csv_reader:
            if  int(line[0]) == Vce and \
                int(line[1]) == Ic  and \
                int(line[2]) == f:

                # actual form of the S parameters written in the datasheet
                s11 = ( float(line[3]), float(line[4]) )
                s21 = ( float(line[5]), float(line[6]) )
                s12 = ( float(line[7]), float(line[8]) )
                s22 = ( float(line[9]), float(line[10]) )
                
                try:
                    NF_opt_dB = float(line[11])
                    R_n = float(line[12])
                    gamma_s_on = ( float(line[13]), float(line[14]) )
                except Exception as e:
                    NF_opt_dB = 0
                    R_n = 0
                    gamma_s_on = (0,0)
                    
    return s11, s12, s21, s22, NF_opt_dB, R_n, gamma_s_on
        


# print ( get_S_parameters(6, 50, 200, "MRF571") )

