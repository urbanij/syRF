# @date        : Thu Mar 19 18:34:05 CET 2020
# @author(s)   : Francesco Urbani
# @file        : 
# @descritpion : Python calculations for 1 stage L-section matching network
#                RF Electronics class, Spring 2018
# 

PI = 3.141592653589793

def compute_L_section_matching(input_impedance, output_impedance):
    """
    Returns `result` tuple. contains the 2 results: each result has a X and B value in ohms

    Parameters
    ----------
    input_impedance : complex
        impedance you want its value to be changed
    output_impedance : complex
        impendace value you want to see

    """

    Z_1 = input_impedance
    Z_2 = output_impedance

    R_1 = Z_1.real
    X_1 = Z_1.imag
    R_2 = Z_2.real
    X_2 = Z_2.imag


    if R_1 >= R_2:
        # shunt - series configuration (down coversion)

        X1 = (R_2*(X_1 - ((R_1*(R_1**2 - R_2*R_1 + X_1**2))/R_2)**(1/2)))/R_1 - (R_1*X_2 + R_2*X_1)/R_1
        X2 = (R_2*(X_1 + ((R_1*(R_1**2 - R_2*R_1 + X_1**2))/R_2)**(1/2)))/R_1 - (R_1*X_2 + R_2*X_1)/R_1

        B1 = (X_1 - ((R_1*(R_1**2 - R_2*R_1 + X_1**2))/R_2)**(1/2))/(R_1**2 + X_1**2)
        B2 = (X_1 + ((R_1*(R_1**2 - R_2*R_1 + X_1**2))/R_2)**(1/2))/(R_1**2 + X_1**2)


    if R_1 < R_2:
        # series - shunt configuration (up conversion)
        X1 = -(R_2*X_1 - R_1*X_2 + (R_1*R_2**2*(X_2 + ((R_2*(R_2**2 - R_1*R_2 + X_2**2))/R_1)**(1/2)))/(R_2**2 + X_2**2) + (R_1*X_2**2*(X_2 + ((R_2*(R_2**2 - R_1*R_2 + X_2**2))/R_1)**(1/2)))/(R_2**2 + X_2**2))/R_2
        X2 = -(R_2*X_1 - R_1*X_2 + (R_1*R_2**2*(X_2 - ((R_2*(R_2**2 - R_1*R_2 + X_2**2))/R_1)**(1/2)))/(R_2**2 + X_2**2) + (R_1*X_2**2*(X_2 - ((R_2*(R_2**2 - R_1*R_2 + X_2**2))/R_1)**(1/2)))/(R_2**2 + X_2**2))/R_2
 
        B1 = -(X_2 + ((R_2*(R_2**2 - R_1*R_2 + X_2**2))/R_1)**(1/2))/(R_2**2 + X_2**2)
        B2 = -(X_2 - ((R_2*(R_2**2 - R_1*R_2 + X_2**2))/R_1)**(1/2))/(R_2**2 + X_2**2)
 

    print(f"{input_impedance=} => {output_impedance=}")
    # solution (1) (X, B)
    print(f"({X1=} ohm, {B1=} Siemens")
    # solution (2) (X, B)
    print(f"({X2=} ohm, {B2=} Siemens")
    print("=======================")
    
    result = (X1, B1) , (X2, B2) # ohms

    return result



def compute_lumped_elements_values(sol, f):

    w = 2*PI*f

    X1 = sol[0][0]
    B1 = sol[0][1]

    X2 = sol[1][0]
    B2 = sol[1][1]

    # X in ohm, B in Siemens

    if X1 > 0: 
        e1 = {"L" : X1/w}           # inductor
    else:
        e1 = {"C" : -1/(w*X1)}      # capacitor

    if B1 > 0: 
        e2 = {"C" : B1/w}           # capacitor
    else:
        e2 = {"L" : -1/(w*B1)}      # inductor

        


    if X2 > 0:
        e3 = {"L" : X2/w}
    else:
        e3 = {"C" : -1/(w*X2)}

    if B2 > 0:
        e4 = {"L" : B2/w}
    else:
        e4 = {"C" : -1/(w*B2)}

    
    return (e1, e2) , (e3, e4)




assert(compute_L_section_matching(200-100j, 100)) == ((-122.4744871391589,-0.006898979485566356),(122.47448713915891,0.0028989794855663565))

compute_L_section_matching(200, 66+660j)

compute_L_section_matching(200, 661+66j)

compute_L_section_matching(4+80j, 20)


# print(compute_lumped_elements_values(compute_L_section_matching(200, 661+66j), 100e6))


