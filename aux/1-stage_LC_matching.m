% @date        : Mon Mar 19 15:38:35 CEST 2018
% @author(s)   : Francesco Urbani
% @file        : 
% @descritpion : Matlab calculations for 1 stage LC matching network
%                

% RF Electronics class, Spring 2018



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% series - shunt %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clc
clear

syms R_L real
syms X_L real
syms R_0 real
syms X_0 real
syms X real
syms B real


 
 
Z_0 = 1/(j*B + 1/(R_L+j*(X+X_L)))
 
real(Z_0)
pretty(ans)

imag(Z_0)
pretty(ans)



eq1 = real(Z_0) ==  R_0
eq2 = imag(Z_0) == -X_0 


S=solve(eq1,eq2, X,B)

S.X

S.B





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%






%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% shunt -series %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




syms R_L real
syms X_L real
syms R_0 real
syms X_0 real
syms X real
syms B real


% equivalent impedance
Z_0 = j*X + 1/(j*B + 1/(R_L+j*X_L))
 

real(Z_0)
pretty(ans)


imag(Z_0)
pretty(ans)



eq1 = real(Z_0) ==  R_0 
eq2 = imag(Z_0) == -X_0
 
S=solve(eq1,eq2, X,B)

S.X

S.B

% >> pretty(S.X)
% /     /           /         2                2  \ \                     \
% |     |           | R_L (R_L  - R_0 R_L + X_L ) | |                     |
% | R_0 | X_L - sqrt| --------------------------- | |                     |
% |     \           \             R_0             / /   R_0 X_L + R_L X_0 |
% | ------------------------------------------------- - ----------------- |
% |                        R_L                                 R_L        |
% |                                                                       |
% |     /           /         2                2  \ \                     |
% |     |           | R_L (R_L  - R_0 R_L + X_L ) | |                     |
% | R_0 | X_L + sqrt| --------------------------- | |                     |
% |     \           \             R_0             / /   R_0 X_L + R_L X_0 |
% | ------------------------------------------------- - ----------------- |
% \                        R_L                                 R_L        /

% >> pretty(S.B)
% /           /         2                2  \ \
% |           | R_L (R_L  - R_0 R_L + X_L ) | |
% | X_L - sqrt| --------------------------- | |
% |           \             R_0             / |
% | ----------------------------------------- |
% |                   2      2                |
% |                R_L  + X_L                 |
% |                                           |
% |           /         2                2  \ |
% |           | R_L (R_L  - R_0 R_L + X_L ) | |
% | X_L + sqrt| --------------------------- | |
% |           \             R_0             / |
% | ----------------------------------------- |
% |                   2      2                |
% \                R_L  + X_L                 /


