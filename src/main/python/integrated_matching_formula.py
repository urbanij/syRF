#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Feb 20 14:40:02 CET 2019

@author(s)   : Francesco Urbani
@file        : integrated_matching.py
@descritpion : 

"""

import numpy as np


def gm(ic, vT):
    return (ic * 1e-3) / (vT * 1e-3)  # A/V,
    # vT = kT/q


def c_pi(ic, vT, fT):  # cπ
    return (gm(ic, vT)) / (2 * np.pi * fT * 1e9)  # F


def Le(Rs, fT):
    return Rs / (2 * np.pi * fT * 1e9)  # H


def Lb(f0, ic, vT, fT, Rs):
    return 1 / ((2 * np.pi * f0 * 1e9) ** 2 * c_pi(ic, vT, fT)) - Le(Rs, fT)
