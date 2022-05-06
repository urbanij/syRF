#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Nov 11 11:17:58 CET 2019

@author(s)   : Francesco Urbani
@file        : 
@descritpion : functions for computing centers and radii of the arcs
               interceping a certain gamma point on the Smith Chart

"""

_z = lambda gamma: ((1 + gamma) / (1 - gamma))
_r = lambda gamma: _z(gamma).real
_x = lambda gamma: _z(gamma).imag


def equi_conductance_circle(gamma):
    """
    args: gamma
    ===========
    returns: tuple made of center (tuple) and radius (float)
    """
    r, x = _r(gamma), _x(gamma)
    center = (r / (r + 1), 0)
    radius = 1 / (1 + r)
    return (center, radius)


def equi_admittance_circle(gamma):
    """
    args: gamma
    ===========
    returns: tuple made of center (tuple) and radius (float)
    """
    r, x = _r(gamma), _x(gamma)
    try:
        center = (1, 1 / x)
        radius = 1 / x
    except ZeroDivisionError:
        center = (1, 1e3)
        radius = 1e3
    return (center, radius)
