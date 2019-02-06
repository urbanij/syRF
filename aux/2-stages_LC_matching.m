% @date        : Mon Mar 19 15:38:35 CEST 2018
% @author(s)   : Francesco Urbani
% @file        : 
% @descritpion : Matlab calculations for 2 stages LC matching network
%                

% RF Electronics class, Spring 2018




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% serial-shunt-serial-shunt %%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

clc
clear

syms R_L real
syms X_L real

syms R_0 real
syms X_0 real

syms X1 real
syms B1 real

syms X2 real
syms B2 real

 
Z_0 = 1/(j*B2 + 1/(j*X2 + 1/(j*B1 + 1/(R_L + j*(X1+X_L)))))

real(Z_0)
imag(Z_0)

eq1 = real(Z_0) ==  R_0
eq2 = imag(Z_0) == -X_0


S = solve(eq1, eq2, X1, B1)




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% shunt-serial-shunt-serial %%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


clc
clear

syms R_L real
syms X_L real

syms R_0 real
syms X_0 real

syms X1 real
syms B1 real

syms X2 real
syms B2 real

 
Z_0 = j*X2 + 1/(j*B2 + 1/(j*X1 + 1/(j*B1+1/(R_L + j*X_L))))

real(Z_0)
imag(Z_0)

eq1 = real(Z_0) ==  R_0
eq2 = imag(Z_0) == -X_0


S = solve(eq1, eq2, X1, B1)

