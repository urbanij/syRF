#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 16:18:20 CET 2019

@author:         Francesco Urbani
@descritpion :   given 2 points on Smith Chart
                 returns 4 solutions like 
                 this [transmission_line_matching.png],
                 where curves (1) and (3) are transmission lines with 
                 characteristic impedance Z0 and lengths lambda1 
                 and lambda3 respectively,
                 and (2) is a transmission line with characteristic 
                 impedance Z1 (to be calculated) and length λ/4.
                 
                 Hypothesis: from load to source


RF Electronics class, Spring 2018
"""

def read_points():
    p0 = complex(input("p0 = "))
    p1 = complex(input("p1 = "))

    print ("{}\n{}".format(p0, p1))



def match():
    
    read_points()



match()