#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Dec 20 15:43:55 CET 2019

@author(s)   : Francesco Urbani
@file        : stub_matching.py
@descritpion :

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


def reset(event):
    d_slider.reset()
    l_slider.reset()


def Zv1(Z0, ZL, d):
    return (
        Z0
        * (ZL - 1j * Z0 * np.tan(2 * np.pi * d))
        / (Z0 - 1j * ZL * np.tan(2 * np.pi * d))
    )


def Zstub_OC(Z0_stub=50, l=0):
    if l % 0.5 == 0.25:
        return 0
    elif l % 0.5 == 0:
        return np.inf
    else:
        return -1j * Z0_stub / np.tan(2 * np.pi * l)


def Zv2(Z0, Z0_stub, ZL, d, l):
    return (Zv1(Z0, ZL, d) * Zstub_OC(Z0_stub, l)) / (
        Zv1(Z0, ZL, d) + Zstub_OC(Z0_stub, l)
    )


def Z(Z0, Z0_stub, ZL):
    return (
        Z0
        * (Zv2(Z0, Z0_stub, ZL) - 1j * Z0 * np.tan(2 * np.pi * z_plus))
        / (Z0 - 1j * Zv2(Z0, Z0_stub, ZL) * np.tan(2 * np.pi * z_plus))
    )


d_min = -0.5
d_max = 0
l_min = -0.5
l_max = 0

num_points = 1e3
z = np.linspace(-0.5, 0, num_points)

fig = plt.figure(figsize=(10, 8))


axcolor = "lightgoldenrodyellow"
ax = plt.axes([0.1, 0.30, 0.8, 0.65])
axfreq = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)
axL = plt.axes([0.1, 0.10, 0.8, 0.03], facecolor=axcolor)
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, "Reset", color=axcolor, hovercolor="0.975")


plt.axes(ax)
# plt.title("C(L) @ $f_0$ = {0:.2f} GHz".format(f0))


z_plus = np.linspace(0, 0, num_points)
z_minus = np.linspace(-0.5, 0, num_points)

(plot_re,) = plt.plot(
    -1e-3,
    Zv2(Z0=50, Z0_stub=50, ZL=50 + 32j, d=1e-3, l=1e-3).real,
    color="blue",
    label="Re Zv2(z)",
)
(plot_im,) = plt.plot(
    -1e-3,
    Zv2(Z0=50, Z0_stub=50, ZL=50 + 32j, d=1e-3, l=1e-3).imag,
    color="blue",
    label="Re Zv2(z)",
)
# plot_d_plus_re,  = plt.plot(z, Zv2(Z0=50, Z0_stub=50, ZL=50+32j).real , color="blue", label="Re Zv2(z)")
# plot_d_minus_re, = plt.plot(z, Zv2(Z0=50, Z0_stub=50, ZL=50+32j).real , color="blue", label="Re Zv2(z)")
# plot_d_plus_im,  = plt.plot(z, Zv2(Z0=50, Z0_stub=50, ZL=50+32j).imag , color="red", label="Im Zv2(z)")
# plot_d_minus_im, = plt.plot(z, Zv2(Z0=50, Z0_stub=50, ZL=50+32j).imag , color="red", label="Im Zv2(z)")


# plt.legend(
#         [plot,   marker],
#         ("C(L) @ $f_0$ = {0:.2f} GHz".format(f0), "$L_0$={} nH\n$C_0$={} pF".format(L0, C0))
#         )


plt.xlabel("z")
plt.ylabel("Z(z)")
plt.xlim(-0.5, 0)
# plt.ylim(-5,5)


# here we create the slider
d_slider = Slider(axfreq, "$d$ [$\lambda$]", d_min, d_max, valinit=0.5)
l_slider = Slider(axL, "$l$ [$\lambda$]", l_min, l_max, valinit=0.5)

plt.xlabel("z")
plt.ylabel("Z(z)")
plt.xlim(-0.5, 0)


# Next we define a function that will be executed each time the value
# indicated by the slider changes. The variable of this function will
# be assigned the value of the slider.
def update(val):

    d = d_slider.val
    l = l_slider.val

    z_plus = np.linspace(-d, 0, num_points)
    z_minus = np.linspace(-0.5, -d, num_points)

    Z0 = 50
    Z0_stub = 50
    ZL = 50 + 32j

    (plot_re,) = plt.set_ydata(
        Zv2(Z0, Z0_stub, ZL, d, l).real, color="blue", label="Re Zv2(z)"
    )
    (plot_im,) = plt.set_ydata(
        Zv2(Z0, Z0_stub, ZL, d, l).imag, color="red", label="Im Zv2(z)"
    )
    # plot_d_plus_im,  = plt.plot(z_plus, Zv2(Z0=50, Z0_stub=50, ZL=50+32j).imag , color="red", label="Im Zv2(z)")
    # plot_d_minus_im, = plt.plot(z_minus, Zv1(Z0=50, Z0_stub=50, ZL=50+32j).imag , color="red", label="Im Zv2(z)")

    fig.canvas.draw_idle()  # redraw the plot

    # update title and legend
    # plt.title("C(L) @ $f_0$ = {0:.3f} GHz".format(f))
    # plt.legend(
    #     [plot, marker],
    #     ( "C(L) @ $f_0$ = {0:.2f} GHz".format(f), "$L_0$={} nH\n$C_0$={} pF".format(L_val, C(f, L_val)) )
    #     )


# the final step is to specify that the slider needs to
# execute the above function when its value changes
d_slider.on_changed(update)
l_slider.on_changed(update)
button.on_clicked(reset)


plt.grid(True)
plt.show()
