

from L_section_matching_network import L_section_matching


if __name__ == '__main__':

    mn = L_section_matching(input_impedance=90+30j, output_impedance=100, frequency=100e6)
    mn.match()
    assert mn.get_solutions() == 'C=5.3052 pF, wire=0, C=5.3052 pF, wire=0, L=477.46 nH, C=26.526 pF, '
    #print(mn)


    mn = L_section_matching(input_impedance=10-12j, output_impedance=100, frequency=100e6)
    mn.match()
    assert mn.get_solutions() == 'C=47.746 pF, L=66.845 nH, L=53.052 nH, C=88.419 pF, '
    print(mn)

    
