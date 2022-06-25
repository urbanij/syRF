import math
import numpy as np
import matplotlib.pyplot as plt


def z0(w, L1, C1, L2, C2, R_L, xr_l):
    # impedance seen
    # is a function of w (and L, C, R_L, xr_l which are now fixed)
    return 1 / (
        1j * w * C2
        + 1 / (1j * w * L2 + 1 / (1j * w * C1 + 1 / (R_L + 1j * (w * L1 + w * xr_l))))
    )


def plot_reflection_coefficient(f0, R_L, X_L, L1, C1, L2, C2):
    w0 = 2 * math.pi * f0

    # evaluate the reactive part of X_L at f0
    if X_L >= 0:
        # reactive - inductive load
        xr_l = X_L / w0
    elif X_L < 0:
        # reactive - capacitive load
        xr_l = 1 / (X_L * w0)

    f = np.linspace(f0 - 2e9, f0 + 2e9, 1e4)
    w = 2 * math.pi * f

    # z0 = 1j*w*L1 + 1/(1j*w*C1 + 1/(R_L+1j*w*xr_l)) # is a function of w (and L, C, R_L, xr_l which are now fixed)

    z0 = z0(w, L1, C1, R_L, xr_l)

    zl = R_L + 1j * w * xr_l  # Z_L

    gamma_l = (z0 - zl) / (z0 + zl)
    abs_gamma_l_1 = abs(gamma_l)

    # print (f)
    # print (gamma_l)

    plt.figure()
    plt.subplot(121)
    plt.plot(f, abs_gamma_l)  # , label="$|\Gamma_L|(L="+str(L1)+", C="+str(C1)+")$")
    plt.grid(True)

    plt.subplot(122)
    plt.yscale("log")
    plt.plot(f, abs_gamma_l)
    plt.grid(True)

    plt.show()


f0 = 630e6
input_impedance = 200 + 100j
output_impedance = 100
L1 = 38.9848400616838e-12
C1 = 2.1960133748349335e-12
L2 = 109.80066874174666e-9
C2 = 2.5989893374455866e-12

Z_L = input_impedance
Z_0 = output_impedance
R_L = Z_L.real
X_L = Z_L.imag
R_0 = Z_0.real
X_0 = Z_0.imag


plot_reflection_coefficient(f0, R_L, X_L, L1, C1, L2, C2)
