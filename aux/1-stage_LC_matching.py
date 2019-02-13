# @date        : Mon Mar 19 15:38:35 CEST 2018
# @author(s)   : Francesco Urbani
# @file        : 
# @descritpion : Python calculations for 1 stage LC matching network
#                

# RF Electronics class, Spring 2018



########################################
# series - shunt 
########################################

import sympy

R_L = sympy.Symbol("R_L", real=True)
X_L = sympy.Symbol("X_L", real=True)
R_0 = sympy.Symbol("R_0", real=True)
X_0 = sympy.Symbol("X_0", real=True)
X   = sympy.Symbol("X",   real=True)
B   = sympy.Symbol("B",   real=True)


 
 
Z_0 = 1/(1j*B + 1/(R_L+1j*(X+X_L)))
 

sympy.re(Z_0)
# R_L/((R_L**2 + (1.0*X + 1.0*X_L)**2)*(R_L**2/(R_L**2 + (1.0*X + 1.0*X_L)**2)**2 + (1.0*B + (-1.0*X - 1.0*X_L)/(R_L**2 + (1.0*X + 1.0*X_L)**2))**2))

#                                                R_L
# ──────────────────────────────────────────────────────────────────────────────
#                             ⎛               2
# ⎛   2                    2⎞ ⎜            R_L                ⎛             -1.0
# ⎝R_L  + (1.0⋅X + 1.0⋅X_L) ⎠⋅⎜──────────────────────────── + ⎜1.0⋅B + ─────────
#                             ⎜                           2   ⎜           2
#                             ⎜⎛   2                    2⎞    ⎝        R_L  + (1
#                             ⎝⎝R_L  + (1.0⋅X + 1.0⋅X_L) ⎠

# ───────────────────
#                  2⎞
# ⋅X - 1.0⋅X_L    ⎞ ⎟
# ────────────────⎟ ⎟
#                2⎟ ⎟
# .0⋅X + 1.0⋅X_L) ⎠ ⎟
#                   ⎠



sympy.im(Z_0)
# (-1.0*B - (-1.0*X - 1.0*X_L)/(R_L**2 + (1.0*X + 1.0*X_L)**2))/(R_L**2/(R_L**2 + (1.0*X + 1.0*X_L)**2)**2 + (1.0*B + (-1.0*X - 1.0*X_L)/(R_L**2 + (1.0*X + 1.0*X_L)**2))**2)

#                                -1.0⋅X - 1.0⋅X_L
#                  -1.0⋅B - ─────────────────────────
#                              2                    2
#                           R_L  + (1.0⋅X + 1.0⋅X_L)
# ───────────────────────────────────────────────────────────────────
#                2                                                  2
#             R_L                ⎛             -1.0⋅X - 1.0⋅X_L    ⎞
# ──────────────────────────── + ⎜1.0⋅B + ─────────────────────────⎟
#                            2   ⎜           2                    2⎟
# ⎛   2                    2⎞    ⎝        R_L  + (1.0⋅X + 1.0⋅X_L) ⎠
# ⎝R_L  + (1.0⋅X + 1.0⋅X_L) ⎠





eq1 = sympy.Eq( sympy.re(Z_0) ,  R_0)
eq2 = sympy.Eq( sympy.im(Z_0) , -X_0)

S = sympy.solve(eq1, eq2, X, B)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/Users/francescourbani/anaconda3/lib/python3.6/site-packages/sympy/solvers/solvers.py", line 827, in solve
#     symbols[0] and
#   File "/Users/francescourbani/anaconda3/lib/python3.6/site-packages/sympy/core/relational.py", line 195, in __nonzero__
#     raise TypeError("cannot determine truth value of Relational")
# TypeError: cannot determine truth value of Relational
# >>>





# S.X

# S.B





