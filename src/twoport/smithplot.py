from __future__ import division
from numpy import asarray, array, dot, zeros, inf, identity
from numpy.linalg import inv
import numpy as np
from pylab import *
from twoport import *

"""edit from original: commented out these following 2 lines,
i don't know why but it caused an error when importing this
file later in S_MRF571_tab.py"""

# from networks import *
# from utils import *


from matplotlib.patches import Circle, FancyArrowPatch   # for drawing smith chart
from matplotlib.lines import Line2D                      # for drawing smith chart
from matplotlib.text import Text
from itertools import chain

# TODO:
# * Label points by freq
# * Label source/load cursors
# clip to rect

class SmithChart(object):
    # z0 = 50
    current_plane = None
    two_port = None
    show_matched_termination_cursor = True
    gain_cursor = False

    def __init__(self, z0, ax=None, show_cursor=True, admittance=True, labels=False):
        self.z0 = z0
        self.ax = ax if ax else gca()
        self.fig = self.ax.figure

        self.draw_smith_chart(admittance, labels)

        if show_cursor:
            self.enable_cursor()

    def _impedance_circle_coords(self, intercept_x_coords, intercept_angles):
        # find coords for constant R circles
        rs = 2/(1 - asarray(intercept_x_coords)) - 1 # convert to desired resistances
        r_circle_coords = [((r/(r+1), 0), 1/(r + 1)) for r in rs]

        # find coords for constant X circles
        intercept_angles = np.radians(intercept_angles)
        xs = np.sin(intercept_angles)/(1 - np.cos(intercept_angles)) # convert to desired reactances
        x_circle_coords = [((1, 1/x), abs(1/x)) for x in xs]

        return r_circle_coords, x_circle_coords, rs, xs

    def draw_impedance_circles(self, intercept_x_coords, intercept_angles, labels=False):
        r_circle_coords, x_circle_coords, rs, xs = self._impedance_circle_coords(intercept_x_coords, intercept_angles)

        for center, radius in chain(r_circle_coords, x_circle_coords):
            c = Circle(center, radius, **self.patch_options_dark)

            c.set_clip_path(self.smith_circle)
            c.set_clip_box(self.ax.bbox)
            self.ax.add_patch(c)

        if labels:
            for x, r in zip(intercept_x_coords, rs):
                self.ax.text(x + 0.04, 0.03, '%.0f' % round(self.z0*r), **self.label_options)

            for a, x in zip(intercept_angles, xs):
                r = (a - 90) if x > 0 else (a + 90)
                a = np.radians(a)
                d = 1.04

                self.ax.text(d*cos(a), d*sin(a), '%.0fj' % round(self.z0*x), rotation=r, **self.label_options)

    
    def draw_admittance_circles(self, intercept_x_coords, intercept_angles, labels=False):
        r_circle_coords, x_circle_coords, rs, xs = self._impedance_circle_coords(intercept_x_coords, intercept_angles)

        # admittance circles have same coords as impedance ones, except flipped
        # on the y-axis
        for (x, y), radius in chain(r_circle_coords, x_circle_coords):
            c = Circle((-x, -y), radius, **self.patch_options_light)

            c.set_clip_path(self.smith_circle)
            c.set_clip_box(self.ax.bbox)
            self.ax.add_patch(c)

        if labels:
            for x, r in zip(intercept_x_coords, rs):
                self.ax.text(-x, 0, '%.1f' % (1/(50*r)), **self.label_options)

            for a, x in zip(intercept_angles, xs):
                r = (a - 90) if x < 0 else (a + 90)
                a = np.radians(a)

                self.ax.text(cos(pi - a), sin(pi - a), '%.1f' % (1/(50*x)), rotation=r, **self.label_options)
    

    def draw_vswr_circles(self, vswr_radii, labels=False):
        for r in vswr_radii:
            c = Circle((0, 0), r, ls='dashed', **self.patch_options_light)

            c.set_clip_path(self.smith_circle)
            c.set_clip_box(self.ax.bbox)
            self.ax.add_patch(c)

        if labels:
            for r in vswr_radii:
                if r > 0:
                    vswr = (1 + r)/(1 - r)
                    self.ax.text(0, r, '%.1f' % vswr, **self.label_options)


    def draw_gamma_circles(self, gamma_radii, labels=False):
        for r in gamma_radii:
            c = Circle((0, 0), r, ls='dashed', **self.patch_options_light)

            c.set_clip_path(self.smith_circle)
            c.set_clip_box(self.ax.bbox)
            self.ax.add_patch(c)

        if labels:
            for r in gamma_radii:
                if r > 0:
                    gamma = r
                    self.ax.text(0, r, '%.1f' % gamma, **self.label_options)

    def draw_chart_axes(self):
        # make outer circle
        self.smith_circle = Circle((0, 0), 1, transform=self.ax.transData, fc='none',
                              **self.patch_options_axis)
        self.ax.add_patch(self.smith_circle)

        # make constant r=1 circle
        z0_circle = Circle((0.5, 0), 0.5, transform=self.ax.transData, fc='none',
                              **self.patch_options_axis)
        z0_circle.set_clip_path(self.smith_circle)
        z0_circle.set_clip_box(self.ax.bbox)
        self.ax.add_patch(z0_circle)

        # make x-axis
        line = Line2D([-1,1],[0,0], **self.patch_options_axis)
        line.set_clip_path(self.smith_circle)
        line.set_clip_box(self.ax.bbox)
        self.ax.add_line(line)

    def draw_smith_chart(self, admittance, labels):
        # plot options for constant z/y circles and axes
        self.patch_options_light = {'fc':'none', 'color':'#474959', 'alpha':0.2, 'lw':1}
        self.patch_options_dark = {'fc':'none', 'color':'#474959', 'alpha':0.5, 'lw':1}
        self.patch_options_axis = {'color':'black', 'alpha':0.8, 'lw':1.5}

        # options for z/y circle labels
        self.label_options = {'ha':'center', 'va':'center', 'size':'9', 'alpha':0.5}#,
                         #'bbox':dict(fc='white', ec='none', alpha=0.5)}
        #self.label_options = {'ha':'center', 'va':'center', 'size':'10', 'alpha':0.5}

        # x-axis coordinates where constant R circles will intersect
        intercept_x_coords = arange(-1, 1, 0.1)


        # angles where constant X circles will intersect (in degrees relative
        # to positive x-axis)
        # intercept_angles = arange(40, 360, 40)
        intercept_angles = arange(40, 360, 40)

        # radii for vswr circles
        vswr_radii = arange(0, 1, 0.2)

        gamma_radii = arange(0, 1, 0.2)

        self.draw_chart_axes()
        self.draw_impedance_circles(intercept_x_coords, intercept_angles, labels)
        
        # no need to draw also the admittance circle
        # self.draw_admittance_circles(intercept_x_coords, intercept_angles, labels=0)
        
        # either draw_vswr_circles or draw_gamma_circles has to be commented out
        
        # self.draw_vswr_circles(vswr_radii, labels)
        self.draw_gamma_circles(gamma_radii, labels)

        self.ax.grid(0)
        self.ax.axis('equal')
        self.ax.axis(np.array([-1.1, 1.1, -1.1, 1.1]))

        self.save_background()

   
    def plot_circle(self, center, radius, text='', text_color='black', circle_color='red',\
                filled=False, circle_alpha=0.2, linestyle='solid', hatch=None):
        text_alpha = 0.7

        text_x_offset = 0.15
        text_y_offset = 0.1

        # calculate position for text
        a, b = center

        # find closet point to edge of circle
        x = a*(1 - radius/sqrt(a**2 + b**2))
        y = b*(1 - radius/sqrt(a**2 + b**2))
        dist_to_circle = sqrt(x**2 + y**2)

        #print ('dist to sphere: ', sqrt(x**2 + y**2))

        if (x**2 + y**2) == 1:
            text_x_offset *= -1
            text_y_offset *= -1

            #textpos = ((a - x)/radius + text_x_offset, (b - y)/radius + text_y_offset)
            textpos = (x/dist_to_circle + text_x_offset, y/dist_to_circle + text_y_offset)
        else:
            textpos = (x + text_x_offset, y + text_y_offset)

        #print ('textpos: ', textpos)

        # make actual circle
        c = Circle(center, radius, fc=circle_color, ec='white', alpha=circle_alpha, fill=filled, linestyle=linestyle, hatch=hatch)
        self.ax.add_patch(c)

        self.ax.annotate(text, (x, y), color=text_color,\
            fontsize='small', alpha=text_alpha, xycoords='data', xytext=textpos,\
            arrowprops=dict(arrowstyle="->", alpha=text_alpha,\
            connectionstyle="arc3,rad=0.17"))


    def save_background(self):
        self.fig.canvas.draw()
        self.background = self.fig.canvas.copy_from_bbox(self.ax.bbox)


#----------------------------------------------------------------









def plot_Smith(Cs, rs, Cl, rl, gamma_in, gamma_out, GA_dB, Ca, ra, NF_dB, Cnf, rnf, GT_dB, Ct, rt, GP_dB, Cp, rp, constant_gamma_circle, ZS, ZL, Z0, gamma_S_visualized, gamma_L_visualized, label_gamma_inout, vce, ic, f, bjt):

    fig, ax = subplots() # note we must use plt.subplots, not plt.subplot

    ## rename Matplotlib window
    fig = gcf()
    fig.canvas.set_window_title('Smith Chart')

    # draws Smith Plot
    sc = SmithChart(Z0, labels=1, show_cursor=0)




    # draws my circles above the preexisting smith circle.
    circle_in  = plt.Circle((Cs.real, Cs.imag), rs, color='blue', fill=True, alpha=.15)
    plot(Cs.real, Cs.imag, marker=None, color="#E0E2FD", label="Input stability circle") # E0E2FD is blue with alpha=0.15

    circle_out = plt.Circle((Cl.real, Cl.imag), rl, color='red' , fill=True, alpha=.15)
    plot(Cl.real, Cl.imag, marker=None, color="#fbe2e1", label="Output stability circle") # fbe2e1 is red with alpha=0.15

    ax.add_artist(circle_in)
    ax.add_artist(circle_out)



    if Cnf != msg_error:
        NF = plt.Circle((Cnf.real, Cnf.imag), rnf, color='#1749CD', fill=False)
        plot(Cnf.real, Cnf.imag, marker="x", color="#1749CD", label="$NF$ = "+ str(NF_dB) + " dB")
        ax.add_artist(NF)

    if Ca != msg_error:
        GA = plt.Circle((Ca.real, Ca.imag), ra, color='#CD1701', fill=False)
        plot(Ca.real, Ca.imag, marker="x", color="#CD1701", label="$G_A$ = "+ str(GA_dB) + " dB")
        ax.add_artist(GA)

    if Ct != msg_error:
        GT = plt.Circle((Ct.real, Ct.imag), rt, color='#23AE0A', fill=False)
        plot(Ct.real, Ct.imag, marker="x", color="#23AE0A", label="$G_T$ = "+ str(GT_dB) + " dB")
        ax.add_artist(GT)

    if Cp != msg_error:
        GP = plt.Circle((Cp.real, Cp.imag), rp, color='#ffa500', fill=False)
        plot(Cp.real, Cp.imag, marker="x", color="#ffa500", label="$G_P$ = "+ str(GP_dB) + " dB")
        ax.add_artist(GP)
    

    


    if gamma_out != msg_error:
        if label_gamma_inout: # if true shows gamma as label
            plot(gamma_out.real, gamma_out.imag, marker="o", color="red", label="$\Gamma_{out}(\Gamma_S=" + str(gamma_S_visualized) + ")$")
        else:
            plot(gamma_out.real, gamma_out.imag, marker="o", color="red", label="$\Gamma_{out}(Z_S=" + str(ZS) + "\Omega)$")
            
    
    if gamma_in != msg_error:
        if label_gamma_inout: # if true shows gamma as label
            plot(gamma_in.real, gamma_in.imag, marker="o", color="blue", label="$\Gamma_{in}(\Gamma_L=" + str(gamma_L_visualized) + ")$")
        else:
            plot(gamma_in.real, gamma_in.imag, marker="o", color="blue", label="$\Gamma_{in}(Z_L=" + str(ZL) + "\Omega)$")
            

    if constant_gamma_circle != msg_error:
        Gamma = plt.Circle((0, 0), constant_gamma_circle, color='#00CCCC', fill=False)
        plot(0, 0, marker=None, color="#00CCCC", label="$\\bar \Gamma$ = "+ str(constant_gamma_circle))
        ax.add_artist(Gamma)




    title(bjt + "\n$V_{CE}$ = " + str(vce) + "V, $I_C$ = " + str(ic) + "mA, $f$ = " + str(f) + " MHz, $Z_0 = " + str(Z0) + "\ \Omega$" )
    legend()
    show()




def plot_Smith_quarter_wave_matching(Z0, Z_in, Z_out, gamma_zin, gamma_zout):

    fig, ax = subplots() # note we must use plt.subplots, not plt.subplot
    


    # draws Smith Plot
    sc = SmithChart(Z0, labels=1, show_cursor=0)



    if gamma_zin != msg_error:
        plot(gamma_zin.real, gamma_zin.imag, marker="o", color="red", label="$\Gamma(Z_{L}=" + str(Z_in) + "\ \Omega)$")

        # draws the circumference passing from zin centered in 0 (constant gamma)
        gamma_zin_circumference = plt.Circle((0, 0), abs(gamma_zin), color='red', linewidth=.5, fill=False)
        ax.add_artist(gamma_zin_circumference)

    if gamma_zout != msg_error:
        plot(gamma_zout.real, gamma_zout.imag, marker="o", color="blue", label="$\Gamma(Z_{L}'=" + str(Z_out) + "\ \Omega)$")
        
        # draws the circumference passing from zout centered in 0 (constant gamma)
        gamma_zout_circumference = plt.Circle((0, 0), abs(gamma_zout), color='blue', linewidth=.5, fill=False)
        ax.add_artist(gamma_zout_circumference)
    
    
    # title("Quarter-wave impedance transformer \n$Z_0 = " + str(Z0) + "\ \Omega$")
    title("Smith Chart\n$Z_0 = " + str(Z0) + "\ \Omega$")
    legend()
    show()






# =======================================================
# =======================================================


msg_error = "" # display nothing if error occurs


