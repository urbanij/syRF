# @date        : Fri Mar 20 11:11:30 CET 2020
# @author(s)   : Francesco Urbani
# @file        : 
# @descritpion : Python calculations for 1 stage L-section matching network
#                RF Electronics class, Spring 2020
# 

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [12, 8]
plt.style.use("ggplot")

import quantiphy

PI = np.pi

class ReactiveComponent:
    """
    Reactive component object

    >>> ReactiveComponent(1000, f=1e6)
    Inductor:
        X = 1 kΩ ⇔ B = -1 mS
        L = 159.15 uH (@ 1 MHz)
    
    Z = R + jX (impedance = resistance + j*reactance) 
    Y = G + jB (admittance = conductance + j*susceptance)
    
    """
    def __init__(self, reactance, f=None):
        self._frequency = f
        self._reactance = quantiphy.Quantity(str(reactance) + 'Ω')
        self._component_type = "L" if reactance > 0 else "C" if reactance < 0 else "wire"
        
        if f != None: 
            assert f > 0

            self._frequency = quantiphy.Quantity(str(f) + 'Hz')
        
            if self._component_type == "L":
                inductor_val = (self._reactance/(2*PI*self._frequency)).real
                self._component_value = quantiphy.Quantity(str(inductor_val) + 'H')
            elif self._component_type == "C":
                capacitor_val = (-1/(2*PI*self._frequency*self._reactance)).real
                self._component_value = quantiphy.Quantity(str(capacitor_val) + 'F')
            else:
                self._component_value = 0
        else:
            self._component_value = 0

    def __eq__(self, other):
        return  self._frequency == other._frequency and \
                self._reactance == other._reactance

    def get_freq(self):
        return self._frequency
    
    def get_susceptance(self):
        if self._reactance != 0:
            return quantiphy.Quantity(str(-1/self._reactance) + 'S')
        else:
            return -np.inf
    
    def __repr__(self):
        rv = "Inductor" if self._component_type == "L" else "Capacitor" if self._component_type == "C" else "wire"
        rv += ":\n\t"
        rv += f"X = {self._reactance} ⇔ B = {self.get_susceptance() }"
        rv += f"\n\t\033[1m{self._component_type}\033[0;0m = \033[1m{self._component_value}\033[0;0m  (@ {self._frequency})" if self._frequency != None else ""
        return rv


class Solution:
    def __init__(self, config_type, shunt_elem: ReactiveComponent, series_elem: ReactiveComponent):
        
        assert shunt_elem.get_freq() == series_elem.get_freq()
        
        self._config_type = config_type
        self._shunt_elem = shunt_elem
        self._series_elem = series_elem

    def __eq__(self, other):
        return  self._config_type == other._config_type and \
                self._shunt_elem  == other._shunt_elem  and \
                self._series_elem == other._series_elem
    
    def __repr__(self):
        if self._config_type == "shunt-series":
            return f"{self._config_type}\n\tShunt {self._shunt_elem}\n\tSeries {self._series_elem}\n"
        else:
            return f"{self._config_type}\n\tSeries {self._series_elem}\n\tShunt {self._shunt_elem}\n"


class L_section_matching:
    def __init__(self, input_impedance, output_impedance, frequency=None):
        
        assert input_impedance.real > 0 and output_impedance.real > 0
        
        self._Z1 = input_impedance
        self._Z2 = output_impedance
        self._normalized_impedance = input_impedance/output_impedance
        
        self._frequency = frequency
        self._solutions = []
        
        self._input_reactance = ReactiveComponent(input_impedance.imag, frequency)
        
    def match(self):
        R1 = self._Z1.real
        X1 = self._Z1.imag
        R2 = self._Z2.real
        X2 = self._Z2.imag

        if R1*(R1 - R2) + X1**2 >= 0:
            """
            shunt - series configuration (down coversion)
            
                                          jXser
                                       +--------+
                      +-----------+----+        +----+
                      |           |    +--------+
                      |           |
                     +++         +++                                                   1
            Z1 =     | |         | | jXshu             Z2 = R2 + jX2 = jXser + -----------------
            R1 + jX1 | |         | |                                             1        1
                     +++         +++                                           ----- + --------
                      |           |                                            jXshu   R1 + jX1
                      |           |
                      +-----------+------------------+
            
            """

            Xshu_1 = (R1*X2 + R2*X1 - R1*(X2 - ((R2*(R1**2 - R2*R1 + X1**2))/R1)**(1/2)))/(R1 - R2)
            Xser_1 = X2 - ((R2*(R1**2 - R2*R1 + X1**2))/R1)**(1/2)

            Xshu_2 = (R1*X2 + R2*X1 - R1*(X2 + ((R2*(R1**2 - R2*R1 + X1**2))/R1)**(1/2)))/(R1 - R2)
            Xser_2 = X2 + ((R2*(R1**2 - R2*R1 + X1**2))/R1)**(1/2)
            
            sol1 = Solution(
                    config_type="shunt-series", 
                    shunt_elem=ReactiveComponent(Xshu_1, f=self._frequency),
                    series_elem=ReactiveComponent(Xser_1, f=self._frequency)
                )
            
            sol2 = Solution(
                    config_type="shunt-series", 
                    shunt_elem=ReactiveComponent(Xshu_2, f=self._frequency),
                    series_elem=ReactiveComponent(Xser_2, f=self._frequency)
                )

            self._solutions.append(sol1)
            if sol2 != sol1: # do not duplicate solutions
                self._solutions.append(sol2)
     

        if R2*(R2 - R1) + X2**2 >= 0:
            """ series - shunt configuration (up conversion)
            
                                jXser
                              +--------+
                      +-------+        +-----+--------------+
                      |       +--------+     |
                      |                      |
                     +++                    +++                                          1
            Z1 =     | |                    | | jXshu       Z2 = R2 + jX2 = -------------------------
            R1 + jX1 | |                    | |                                1            1
                     +++                    +++                              ----  + ----------------
                      |                      |                               jXshu   R1 + jX1 + jXser
                      |                      |
                      +----------------------+---------------+


            """

            Xshu_1 = (R1*X2 + (R1*R2*(R2**2 - R1*R2 + X2**2))**(1/2))/(R1 - R2)
            Xser_1 = -(R2*X1 - (R1*R2*(R2**2 - R1*R2 + X2**2))**(1/2))/R2

            Xshu_2 = (R1*X2 - (R1*R2*(R2**2 - R1*R2 + X2**2))**(1/2))/(R1 - R2)
            Xser_2 = -(R2*X1 + (R1*R2*(R2**2 - R1*R2 + X2**2))**(1/2))/R2
            
            sol1 = Solution(
                    config_type="series-shunt", 
                    shunt_elem=ReactiveComponent(Xshu_1, f=self._frequency),
                    series_elem=ReactiveComponent(Xser_1, f=self._frequency)
                )
            
            sol2 = Solution(
                    config_type="series-shunt",
                    shunt_elem=ReactiveComponent(Xshu_2, f=self._frequency),
                    series_elem=ReactiveComponent(Xser_2, f=self._frequency)
                )
            
            self._solutions.append(sol1)
            if sol2 != sol1: # do not duplicate solutions
                self._solutions.append(sol2)

    def get_solutions(self):
        rv = ""
        for sol in self._solutions:
            rv += f"{sol._shunt_elem._component_type}={sol._shunt_elem._component_value}, "
            rv += f"{sol._series_elem._component_type}={sol._series_elem._component_value}, "
        return rv
        
        
    def get_input_reactance(self):
        return self._input_reactance
    
    def plot(self):
        pass
        delta_f = 2000
        freq = np.linspace(self._frequency-delta_f/2, self._frequency+delta_f/2, 2000)
        for solution in self._solutions:
            print(solution)
            if solution._config_type=="shunt-series":
                if solution._shunt_elem._component_type == "L":
                    if solution._series_elem._component_type == "C":
                        Z2 = 1/(2*PI*freq*solution._series_elem._component_value.real) 
                        
        plt.plot(freq, Z2)
        
    def __repr__(self):
        rv  = f"From {self._Z1} Ω to {self._Z2} Ω\n\n"
        rv += f"normalized output = {self._Z1}Ω/{self._Z2}Ω = {self._normalized_impedance}\n\n"
        for solution in self._solutions:
            rv += f"{solution}"
        return rv



if __name__ == '__main__':
    pass
    

