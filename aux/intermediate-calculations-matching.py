import math

# test inputs
input_impedance  = 200-100j
output_impedance = 100
f0               = 500e6



# ----------------------------------------------
Z_L = input_impedance
Z_0 = output_impedance

R_L = Z_L.real
X_L = Z_L.imag
R_0 = Z_0.real
X_0 = Z_0.imag


if R_L >= R_0:

	# matlab results
	# shunt - series config
	X1 = (R_0*(X_L - ((R_L*(R_L**2 - R_0*R_L + X_L**2))/R_0)**(1/2)))/R_L - (R_0*X_L + R_L*X_0)/R_L
	X2 = (R_0*(X_L + ((R_L*(R_L**2 - R_0*R_L + X_L**2))/R_0)**(1/2)))/R_L - (R_0*X_L + R_L*X_0)/R_L
	 
	B1 = (X_L - ((R_L*(R_L**2 - R_0*R_L + X_L**2))/R_0)**(1/2))/(R_L**2 + X_L**2)
	B2 = (X_L + ((R_L*(R_L**2 - R_0*R_L + X_L**2))/R_0)**(1/2))/(R_L**2 + X_L**2)
 


if R_L < R_0:

	# matlab results
	# series - shunt config
	X1 = (R_L*(X_0 - ((R_0*(R_0**2 - R_L*R_0 + X_0**2))/R_L)**(1/2)))/R_0 - (R_0*X_L + R_L*X_0)/R_0
	X2 = (R_L*(X_0 + ((R_0*(R_0**2 - R_L*R_0 + X_0**2))/R_L)**(1/2)))/R_0 - (R_0*X_L + R_L*X_0)/R_0
	
	B1 = (X_0 - ((R_0*(R_0**2 - R_L*R_0 + X_0**2))/R_L)**(1/2))/(R_0**2 + X_0**2)
	B2 = (X_0 + ((R_0*(R_0**2 - R_L*R_0 + X_0**2))/R_L)**(1/2))/(R_0**2 + X_0**2)
 




print (X1)
print (B1)
print (X2)
print (B2)

