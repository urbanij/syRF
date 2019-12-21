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


def Z(*,Z0, ZL):
    return Z0 * (ZL - 1j*Z0*np.tan(2*np.pi*z))/(Z0-1j*ZL*np.tan(2*np.pi*z))


d_min = -0.5
d_max = 0
l_min = -0.5
l_max = 0

num_points = 1e3
z = np.linspace(-0.5,0,num_points)

fig = plt.figure(figsize=(10,8))


axcolor = 'lightgoldenrodyellow'
ax      = plt.axes([0.1, 0.30, 0.8, 0.65])  
axfreq  = plt.axes([0.1, 0.15, 0.8, 0.03],facecolor=axcolor)
axL     = plt.axes([0.1, 0.10, 0.8, 0.03],facecolor=axcolor)
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button  = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')



plt.axes(ax) 
# plt.title("C(L) @ $f_0$ = {0:.2f} GHz".format(f0))


plot,   = plt.plot(z, Z(Z0=50, ZL=50+32j).real , color="blue", label="Z(z)")
plot,   = plt.plot(z, Z(Z0=50, ZL=50+32j).imag , color="red", label="Z(z)")



# plt.legend(
#         [plot,   marker],
#         ("C(L) @ $f_0$ = {0:.2f} GHz".format(f0), "$L_0$={} nH\n$C_0$={} pF".format(L0, C0))
#         )


plt.xlabel("z")
plt.ylabel("Z(z)")
plt.xlim(-0.5,0)
plt.ylim(-5,5)


# here we create the slider
d_slider = Slider(axfreq, '$d$ [$\lambda$]', d_min, d_max, valinit=0.5)
l_slider = Slider(axL, '$l$ [$\lambda$]', l_min, l_max, valinit=0.5)



# Next we define a function that will be executed each time the value
# indicated by the slider changes. The variable of this function will
# be assigned the value of the slider.
def update(val):
    d     = d_slider.val
    l     = l_slider.val
    
    plot.set_ydata( Z(Z0=50, ZL=d*23).real )
    plot.set_ydata( Z(Z0=50, ZL=50+32j).imag )

    # marker.set_xdata(L_val)
    # marker.set_ydata(C(f,L_val))

    fig.canvas.draw_idle()                       # redraw the plot

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

