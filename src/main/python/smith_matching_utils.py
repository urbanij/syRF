#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Dec 16 13:26:46 CET 2019

@author(s)   : Francesco Urbani
@file        : smith_matching_utils.py
@descritpion : utilities for computing stuff revolving around smith chart.



"""



import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
import ccomplex


def round_of_rating(number):
    """Round a number to the closest half integer.
    >>> round_of_rating(1.3)
    1.5
    >>> round_of_rating(2.6)
    2.5
    >>> round_of_rating(3.0)
    3.0
    >>> round_of_rating(4.1)
    4.0"""
    return round(number * 2) / 2


def lambda_tick_map():
    # mapping the angles with the lambda scale
    num_points = 360*2 + 1
    angle_map  = np.linspace(180, -180, num_points)
    lambda_map = np.linspace(0  ,0.5  , num_points)

    lambda_tick_map = {}
    for i,j in zip(angle_map, lambda_map):
        lambda_tick_map[i]=j

    """
    print(lambda_tick_map)
    >>> {180.0: 0.0, 
        179.5: 0.0006944444444444445, 
        179.0: 0.001388888888888889, 
        178.5: 0.0020833333333333333, 
        ...
        -178.0: 0.49722222222222223, 
        -178.5: 0.4979166666666667, 
        -179.0: 0.4986111111111111, 
        -179.5: 0.49930555555555556, 
        -180.0: 0.5
        }
    """
    return lambda_tick_map


