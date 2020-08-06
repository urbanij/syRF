from __future__ import division
from numpy import asarray, array, dot, zeros, inf, identity
from numpy.linalg import inv
import numpy as np
import ccomplex
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

        return 

        if labels:
            for x, r in zip(intercept_x_coords, rs):
                """ use this when z0 is float """
                # self.ax.text(x + 0.04, 0.03, '%.0f' % round(self.z0*r), **self.label_options)

                """ use this when z0 is complex """
                self.ax.text(x + 0.04, 0.03, '%s' % str(self.z0*r), **self.label_options)

            for a, x in zip(intercept_angles, xs):
                r = (a - 90) if x > 0 else (a + 90)
                a = np.radians(a)
                d = 1.04

                """ use this when z0 is float """
                # self.ax.text(d*cos(a), d*sin(a), '%.0fj' % round(self.z0*x), rotation=r, **self.label_options)

                """ use this when z0 is complex """
                self.ax.text(d*cos(a), d*sin(a), '%sj' % str(self.z0*x), rotation=r, **self.label_options)

    
    def draw_admittance_circles(self, intercept_x_coords, intercept_angles, labels=False):
        r_circle_coords, x_circle_coords, rs, xs = self._impedance_circle_coords(intercept_x_coords, intercept_angles)

        # admittance circles have same coords as impedance ones, except flipped
        # on the y-axis
        for (x, y), radius in chain(r_circle_coords, x_circle_coords):
            c = Circle((-x, -y), radius, **self.patch_options_light)

            c.set_clip_path(self.smith_circle)
            c.set_clip_box(self.ax.bbox)
            self.ax.add_patch(c)

        return 

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

        """ comment return for printing the labels along the constant gamma circles """
        # return 

        if labels:
            for r in gamma_radii:
                if r > 0:
                    gamma = r
                    self.ax.text(0, r, '%.1f' % gamma, **self.label_options)


    def draw_chart_axes(self):
        """ make outer circle """
        self.smith_circle = Circle((0, 0), 1, transform=self.ax.transData, fc='none', **self.patch_options_axis)
        self.ax.add_patch(self.smith_circle)

        """ make constant r=1 (impedance) circle """
        z0_circle = Circle((0.5, 0), 0.5, transform=self.ax.transData, fc='none', **self.patch_options_axis)
        z0_circle.set_clip_path(self.smith_circle)
        z0_circle.set_clip_box(self.ax.bbox)
        self.ax.add_patch(z0_circle)

        """ make constant g=1 (admittance) circle """
        y0_circle = Circle((-0.5, 0), 0.5, transform=self.ax.transData, fc='none', **self.patch_options_axis)
        y0_circle.set_clip_path(self.smith_circle)
        y0_circle.set_clip_box(self.ax.bbox)
        self.ax.add_patch(y0_circle)

        """ make x-axis """
        line = Line2D([-1,1],[0,0], **self.patch_options_axis)
        line.set_clip_path(self.smith_circle)
        line.set_clip_box(self.ax.bbox)
        self.ax.add_line(line)
        

    def draw_smith_chart(self, admittance, labels):
        # plot options for constant z/y circles and axes
        self.patch_options_light = {'fc':'none', 'color':'#474959', 'alpha':0.45, 'lw':.2}
        self.patch_options_dark = {'fc':'none', 'color':'#474959', 'alpha':0.8, 'lw':.3}
        self.patch_options_axis = {'color':'black', 'alpha':1, 'lw':.4}

        # options for z/y circle labels
        self.label_options = {'ha':'center', 'va':'center', 'size':'9', 'alpha':0.5}#,
                         #'bbox':dict(fc='white', ec='none', alpha=0.5)}
        #self.label_options = {'ha':'center', 'va':'center', 'size':'10', 'alpha':0.5}

        # x-axis coordinates where constant R circles will intersect
        

        # intercept_x_coords = arange(-1, 1, 0.1) # too compact imo
        intercept_x_coords = arange(-0.75, 1, 0.25)


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
        self.draw_admittance_circles(intercept_x_coords, intercept_angles, labels=0)
        
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








####---------------------------------------------------------------------------------
#### move in a module or something later
####---------------------------------------------------------------------------------
_z = lambda gamma: ((1+gamma)/(1-gamma))
_r = lambda gamma: _z(gamma).real
_x = lambda gamma: _z(gamma).imag

def equi_resistance_circle(gamma):
    """
    args: gamma
    ===========
    returns: tuple made of center (tuple) and radius (float)
    """
    r,x = _r(gamma), _x(gamma)
    center = (r/(r+1) , 0)
    radius = 1/(1+r)
    return (center,radius)

def equi_reactance_circle(gamma):
    """
    args: gamma
    ===========
    returns: tuple made of center (tuple) and radius (float)
    """
    r,x = _r(gamma), _x(gamma)
    try:
        center = (1 , 1/x)
        radius = 1/x
    except ZeroDivisionError:
        center = (1 , 1e3)
        radius = 1e3
    return (center,radius)

####---------------------------------------------------------------------------------












def plot_Smith(Cs, rs, Cl, rl, gamma_in, gamma_out, gamma_L, gamma_S, GA_dB, Ca, ra, NF_dB, Cnf, rnf, GT_dB, Ct, rt, GP_dB, Cp, rp, constant_gamma_circle, ZS, ZL, Z0, gamma_S_visualized, gamma_L_visualized, label_gamma_inout, vce, ic, f, bjt):

    # args = (Cs, rs, Cl, rl, gamma_in, gamma_out, gamma_L, gamma_S, GA_dB, Ca, ra, NF_dB, Cnf, rnf, GT_dB, Ct, rt, GP_dB, Cp, rp, constant_gamma_circle, ZS, ZL, Z0, gamma_S_visualized, gamma_L_visualized, label_gamma_inout, vce, ic, f, bjt)
    # print("=====================\nS data:")
    # print("\n".join(map(str,args)))



    fig, ax = subplots(figsize=(10,8)) # note we must use plt.subplots, not plt.subplot

    # subplots_adjust(top=0.915) 
    # subplots_adjust(bottom=0.065)
    # subplots_adjust(left=0.06) 
    # subplots_adjust(right=0.945) 
    # subplots_adjust(hspace=0.2)
    # subplots_adjust(wspace=0.2) 

    ## rename Matplotlib window
    fig = gcf()
    fig.canvas.set_window_title('Smith Chart')

    # draws Smith Plot
    sc = SmithChart(Z0, labels=1, show_cursor=0)




    # draws my circles above the preexisting smith circle.
    circle_in  = plt.Circle((Cs.real, Cs.imag), rs, color='red', fill=True, alpha=.15)
    plot(Cs.real, Cs.imag, marker=None, color="#fbe2e1", label="Input stability circle") # fbe2e1 is red with alpha=0.15

    circle_out = plt.Circle((Cl.real, Cl.imag), rl, color='green' , fill=True, alpha=.15)
    plot(Cl.real, Cl.imag, marker=None, color="#CCFFCC", label="Output stability circle") # CCFFCC is green with 

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
    

    


    if gamma_S != msg_error:
        if label_gamma_inout: # if true shows gamma as label
            plot(gamma_S.real, gamma_S.imag, marker="o", color="coral", label="$\Gamma_{S}$")
        else:
            plot(gamma_S.real, gamma_S.imag, marker="o", color="coral", label="$\Gamma_{S}(Z_S=" + str(ZS) + "\Omega)$")
        # draw circumference centered in the origin passing from gamma_S point
        gamma_S_circumference = plt.Circle((0, 0), abs(gamma_S), color='coral', linewidth=.3, fill=False)
        ax.add_artist(gamma_S_circumference)
            
    
    if gamma_in != msg_error:
        if label_gamma_inout: # if true shows gamma as label
            plot(gamma_in.real, gamma_in.imag, marker="o", color="crimson", label="$\Gamma_{in}(\Gamma_L=" + str(gamma_L_visualized) + ")$")
        else:
            plot(gamma_in.real, gamma_in.imag, marker="o", color="crimson", label="$\Gamma_{in}(Z_L=" + str(ZL) + "\Omega)$")
         



    if gamma_L != msg_error:
        if label_gamma_inout: # if true shows gamma as label
            plot(gamma_L.real, gamma_L.imag, marker="o", color="lime", label="$\Gamma_{L}$")
        else:
            plot(gamma_L.real, gamma_L.imag, marker="o", color="lime", label="$\Gamma_{L}(Z_L=" + str(ZL) + "\Omega)$")
        # draw circumference centered in the origin passing from gamma_L point
        gamma_L_circumference = plt.Circle((0, 0), abs(gamma_L), color='lime', linewidth=.3, fill=False)
        ax.add_artist(gamma_L_circumference)

    
    if gamma_out != msg_error:
        if label_gamma_inout: # if true shows gamma as label
            plot(gamma_out.real, gamma_out.imag, marker="o", color="darkgreen", label="$\Gamma_{out}(\Gamma_S=" + str(gamma_S_visualized) + ")$")
        else:
            plot(gamma_out.real, gamma_out.imag, marker="o", color="darkgreen", label="$\Gamma_{out}(Z_S=" + str(ZS) + "\Omega)$")

        


    if constant_gamma_circle != msg_error:
        Gamma = plt.Circle((0, 0), constant_gamma_circle, color='#00CCCC', fill=False)
        plot(0, 0, marker=None, color="#00CCCC", label="$\\bar \Gamma$ = "+ str(constant_gamma_circle))
        ax.add_artist(Gamma)




    title(bjt + "\n$V_{CE}$ = " + str(vce) + "V, $I_C$ = " + str(ic) + "mA, $f$ = " + str(f) + " MHz, $Z_0 = " + str(Z0) + "\ \Omega$" )
    legend()
    show()




def plot_Smith_smith_matching(Z0, Z_in, Z_out, gamma_zin, gamma_zout):

    alpha_constant_gamma                = 0.78
    lw_constant_gamma                   = 0.9
    alpha_resistance_and_reactance_arcs = 0.5
    lw_resistance_reactance_arcs        = 0.65
    alpha_z_point                       = 0.80
    alpha_y_point                       = 0.40

    legend_caption = "$Z_0 = {}\ \Omega$\n".format(ccomplex.ccomplex(Z0))

    NORMALIZED_VALUES     = True
    
    


    fig, ax = subplots(figsize=(10,8)) # note we must use plt.subplots, not plt.subplot
    fig.canvas.set_window_title('Smith Chart')
    
    # draws Smith Plot
    sc = SmithChart(Z0, labels=1, show_cursor=0) 

    if gamma_zin != msg_error:

        if NORMALIZED_VALUES:
            gamma_zin_label = "$z_{L}$="+f"{Z_in/Z0:.4g}"
            gamma_yin_label = "$y_{L}$="+f"{(1/(Z_in/Z0)):.4g}"
        else:
            gamma_zin_label = "$Z_{L}$="+f"{Z_in:.4g}"+" $\Omega$"
            gamma_yin_label = "$Y_{L}$="+f"{(1/Z_in)*1e3:.4g}"+" mS"

        
        """ Z point (impedance) """
        plot(gamma_zin.real, gamma_zin.imag, marker="o", color="red", alpha=alpha_z_point, label=gamma_zin_label)

        """ constant resistance arc """
        (_cx, _cy), _r = equi_resistance_circle(gamma_zin)
        resistance_zin_circumference = plt.Circle((_cx, _cy), _r, color='red', linestyle='--', alpha=alpha_resistance_and_reactance_arcs, linewidth=lw_resistance_reactance_arcs, fill=False)
        ax.add_artist(resistance_zin_circumference)

        """ constant reactance arc """
        (_cx, _cy), _r = equi_reactance_circle(gamma_zin)
        reactance_zin_circumference = plt.Circle((_cx, _cy), _r, color='red', linestyle='-.', alpha=alpha_resistance_and_reactance_arcs, linewidth=lw_resistance_reactance_arcs, fill=False)
        ax.add_artist(reactance_zin_circumference)


        

        """ Y point (admittance) """
        plot(-gamma_zin.real, -gamma_zin.imag, marker="o", color="red", fillstyle='none', alpha=alpha_y_point, label=gamma_yin_label)

        """ constant conductance arc """
        (_cx, _cy), _r = equi_resistance_circle(-gamma_zin)
        reactance_zin_circumference = plt.Circle((_cx, _cy), _r, color='red', linestyle='--', alpha=alpha_resistance_and_reactance_arcs, linewidth=lw_resistance_reactance_arcs, fill=False)
        ax.add_artist(reactance_zin_circumference)

        """ constant susceptance arc """
        (_cx, _cy), _r = equi_reactance_circle(-gamma_zin)
        susceptance_zin_circumference = plt.Circle((_cx, _cy), _r, color='red', linestyle='-.', alpha=alpha_resistance_and_reactance_arcs, linewidth=lw_resistance_reactance_arcs, fill=False)
        ax.add_artist(susceptance_zin_circumference)


        """ constant gamma circumference"""
        gamma_zin_circumference = plt.Circle((0, 0), abs(gamma_zin), color='red', linestyle='-', alpha=alpha_constant_gamma, linewidth=lw_constant_gamma, fill=False)
        ax.add_artist(gamma_zin_circumference)



    if gamma_zout != msg_error:

        if NORMALIZED_VALUES:
            gamma_zout_label = "$z_{L}'$="+f"{Z_out/Z0:.4g}"
            gamma_yout_label = "$y_{L}'=$"+f"{(1/(Z_out/Z0)):.4g}"
        else:
            gamma_zout_label = "$Z_{L}'$="+f"{Z_out:.4g}"+" $\Omega$"
            gamma_yout_label = "$Y_{L}'=$"+f"{(1/Z_out)*1e3:.4g}"+" mS"

        """ Z point (impedance) """
        plot(gamma_zout.real, gamma_zout.imag, marker="o", color="blue", alpha=alpha_z_point, label=gamma_zout_label)
        # ax.annotate("$z_L$", (gamma_zout.real, gamma_zout.imag))

        """ constant resistance arc """
        (_cx, _cy), _r = equi_resistance_circle(gamma_zout)
        resistance_zout_circumference = plt.Circle((_cx, _cy), _r, color='blue', linestyle='--', alpha=alpha_resistance_and_reactance_arcs, linewidth=lw_resistance_reactance_arcs, fill=False)
        ax.add_artist(resistance_zout_circumference)

        """ constant admittance arc """
        (_cx, _cy), _r = equi_reactance_circle(gamma_zout)
        reactance_zout_circumference = plt.Circle((_cx, _cy), _r, color='blue', linestyle='-.', alpha=alpha_resistance_and_reactance_arcs, linewidth=lw_resistance_reactance_arcs, fill=False)
        ax.add_artist(reactance_zout_circumference)





        """ Y point (admittance) """
        plot(-gamma_zout.real, -gamma_zout.imag, marker="o", color="blue", fillstyle='none', alpha=alpha_y_point, label=gamma_yout_label)

        """ constant conductance arc """
        (_cx, _cy), _r = equi_resistance_circle(-gamma_zout)
        reactance_zout_circumference = plt.Circle((_cx, _cy), _r, color='blue', linestyle='--', alpha=alpha_resistance_and_reactance_arcs, linewidth=lw_resistance_reactance_arcs, fill=False)
        ax.add_artist(reactance_zout_circumference)

        """ constant susceptance arc """
        (_cx, _cy), _r = equi_reactance_circle(-gamma_zout)
        susceptance_zout_circumference = plt.Circle((_cx, _cy), _r, color='blue', linestyle='-.', alpha=alpha_resistance_and_reactance_arcs, linewidth=lw_resistance_reactance_arcs, fill=False)
        ax.add_artist(susceptance_zout_circumference)


        
        """ constant gamma circumference"""
        gamma_zout_circumference = plt.Circle((0, 0), abs(gamma_zout), color='blue', linestyle='-', alpha=alpha_constant_gamma, linewidth=lw_constant_gamma, fill=False)
        ax.add_artist(gamma_zout_circumference)
    
    
    if gamma_zout != msg_error or gamma_zin != msg_error:
        if NORMALIZED_VALUES:
            legend_caption += "Normalized values"
        else: 
            legend_caption += "Actual values"
    
    legend(title=legend_caption, ncol=2)

    subplots_adjust(left=-0.01, bottom=-0.01, right=1.005, top=1.005, wspace=0.45, hspace=0.2)
    show()





# =======================================================
# =======================================================


msg_error = "" # display nothing if error occurs


