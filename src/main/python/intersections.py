#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Apr 28 10:14:23 2018

@author(s)   : Francesco Urbani
@file        : intersections.py
@descritpion : calculates the intersection (if exists) of two circumferences,
               given their radii and centers.

"""

import math
import cmath


def find_intersection_points(c1, r1, c2, r2):
    # c1 and c2 are the coordinates of the center (complex number) and r1 r2 their radii

    d = math.hypot(
        c2.real - c1.real, c2.imag - c1.imag
    )  # hypot: return the Euclidean norm, sqrt(x*x + y*y).
    # This is the length of the vector from the origin
    # to point (x, y).
    if d <= r1 + r2 and d >= abs(r2 - r1):
        ex = (c2.real - c1.real) / d
        ey = (c2.imag - c1.imag) / d
        x = (r1**2 - r2**2 + d**2) / (2 * d)
        y = (r1**2 - x**2) ** 0.5

        P1 = c1.real + x * ex + y * ey + (c1.imag + x * ey - y * ex) * 1j
        P2 = c1.real + x * ex - y * ey + (c1.imag + x * ey + y * ex) * 1j

        return P1, P2


# tests
# c1 = (-0.18950982066253522+0.38855271332139935j)
# r1 = 0.41572146338323246
# c2 = (-0.622856331738763+0.12067130435833404j)
# r2 = 0.4408755676369167


# c1 = 0
# r1=1
# c2 = 1.22
# r2=1


# points = find_intersection_points(c1, r1, c2, r2)

# for i in points:
#   print (i)
#   print (str(abs(i)) + ";" + str(math.degrees(cmath.phase(i))))
