#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Apr 23 22:02:42 2018

@author(s)   : Francesco Urbani
@file        : plot_reflection_coefficient.py
@descritpion : File to plot Gamma in LC_matching_tab

"""

import numpy as np
import matplotlib.pyplot as plt


def plot_gamma(rv):
    f0, Z_L, Z_0, L1, C1, L2, C2 = rv

    LEVEL_dB = -3
    LEVEL = 10 ** (LEVEL_dB / 10)  # -3dB is close to 0.5
    F_upper = 1.5 * f0
    F_lower = 0.5 * f0
    Fpoints = 1e4

    lev_x = np.array([F_lower, F_upper])
    lev_y = np.array([LEVEL] * 2)

    R_L = Z_L.real
    X_L = Z_L.imag
    R_0 = Z_0.real
    X_0 = Z_0.imag

    w0 = 2 * np.pi * f0

    f = np.linspace(F_lower, F_upper, Fpoints)
    w = 2 * np.pi * f

    # estract the dependency of the frequency from X_L before going ahead.
    # if X_L is positive it means that it is an inductive load, hence:
    if X_L >= 0:

        if R_L >= R_0:
            # down conversion
            z0_1 = 1j * w * L1 + 1 / (1j * w * C1 + 1 / (R_L + 1j * w * X_L / w0))
            z0_2 = 1 / (1j * w * C2) + 1 / (
                (1 / (1j * w * L2) + 1 / (R_L + 1j * w * X_L / w0))
            )

        else:
            # up conversion
            z0_1 = 1 / (1j * w * C2 + 1 / (1j * w * L2 + R_L + 1j * w * X_L / w0))
            z0_2 = 1 / (
                1 / (1j * w * L1) + 1 / (1 / (1j * w * C1) + R_L + 1j * w * X_L / w0)
            )

    else:
        # otherhise if is it negative, i.e. capacitive load:
        # x_zl = -1/(X_L*w0)

        if R_L >= R_0:
            # down conversion
            z0_1 = 1j * w * L1 + 1 / (
                1j * w * C1 + 1 / (R_L + 1 / (1j * w * 1 / (w0 * X_L)))
            )
            z0_2 = 1 / (1j * w * C2) + 1 / (
                (1 / (1j * w * L2) + 1 / (R_L + 1 / (1j * w * 1 / (w0 * X_L))))
            )

        else:
            # up conversion
            z0_1 = 1 / (
                1j * w * C2 + 1 / (1j * w * L2 + R_L + 1 / (1j * w * 1 / (w0 * X_L)))
            )
            z0_2 = 1 / (
                1 / (1j * w * L1)
                + 1 / (1 / (1j * w * C1) + R_L + 1 / (1j * w * 1 / (w0 * X_L)))
            )

    # if R_L >= R_0:
    #   # if down conversion
    #   z0_1 = 1j*w*L1 + 1/(1j*w*C1 + 1/(R_L+1j*w*x_zl))
    #   z0_2 = 1/(1j*w*C2) + 1/((1/(1j*w*L2) + 1/(R_L+1j*w*x_zl)))

    # else:
    #   # if up conversion
    #   z0_1 = 1/(1j*w*C2 + 1/(1j*w*L2 + R_L + 1j*w*x_zl))
    #   z0_2 = 1/(1/(1j*w*L1) + 1/(1/(1j*w*C1) + R_L + 1j*w*x_zl))

    gamma1 = (z0_1 - Z_0) / (z0_1 + Z_0)
    gamma2 = (z0_2 - Z_0) / (z0_2 + Z_0)

    RL1 = -20 * np.log10(abs(gamma1))
    RL2 = -20 * np.log10(abs(gamma2))

    VSWR1 = (1 + abs(gamma1)) / (1 - abs(gamma1))
    VSWR2 = (1 + abs(gamma2)) / (1 - abs(gamma2))

    plt.figure(1, figsize=(10, 8))
    plt.subplot(211)
    # plt.yscale('log')
    plt.xlim(F_lower, F_upper)
    plt.ylim(0, 1)
    plt.grid(True, which="both", ls="-")
    plt.plot(f, abs(gamma1), label="$|\Gamma|_{L_1, C_1}$")
    plt.plot(f, abs(gamma2), label="$|\Gamma|_{L_2, C_2}$")
    # plt.plot(lev_x, lev_y, color='red',linewidth=1.5, label="$3\ dB$ level")
    plt.ylabel("Input reflection coefficient $|\Gamma_{in}|$")
    plt.legend()

    plt.subplot(212)
    plt.yscale("log")
    plt.xlim(F_lower, F_upper)
    # plt.ylim(1e-2, 1)
    plt.ylabel("$RL\ (dB)$")
    plt.grid(True, which="both", ls="-")
    plt.plot(f, RL1, label="$RL_{L_1, C_1}$")
    plt.plot(f, RL2, label="$RL_{L_2, C_2}$")
    # plt.plot(lev_x, np.array([(1+abs(LEVEL))/(1-abs(LEVEL))]*2) , color='red',linewidth=1.5, label="$3\ dB$ level")
    plt.legend()

    # plt.subplot(313)
    # plt.yscale('log')
    # plt.xlim(F_lower, F_upper)
    # plt.grid(True, which="both",ls="-")
    # plt.plot(f, VSWR1)
    # plt.plot(f, VSWR2)

    plt.xlabel("$f\ (MHz)$")
    # plt.suptitle('$|\Gamma(f)|$', fontsize=14)

    # plt.polar(f, abs(gamma2))

    plt.show()


# test1 down convversion--------
# f0 = 77e9
# Z_L = 420+53j
# Z_0 = 50
# L1 = 283.6647403621703e-12
# C1 = 13.907404352599274e-15

# L2 = 336.80162521958965e-12
# C2 = 15.060987801213773e-15
# end test1----------------------


# test1 up conversion-----------
f0 = 860e6
Z_L = 13 + 42j
Z_0 = 123 + 89j
L1 = 7.906657587383121e-9
C1 = 2.0651017169163284e-12

L2 = 1.0391155313956788e-9
C2 = 2.902494025069726e-12
# end test1----------------------

rv = [f0, Z_L, Z_0, L1, C1, L2, C2]
# plot_gamma(rv)
