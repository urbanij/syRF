# @date        : Fri Mar 20 11:11:30 CET 2020
# @author(s)   : Francesco Urbani
# @file        : 
# @descritpion : Python calculations for 1 stage L-section matching network
#                RF Electronics class, Spring 2020
# 

PI = 3.141592653589793

class Component:
    def __init__(self, impedance, frequency):
        self._impedance = impedance
        self._component_type = "L" if impedance > 0 else "C"
        self._component_value = impedance/(2*PI*frequency) if self._impedance > 0 else -1/(2*PI*frequency*self._impedance)
    
    def __repr__(self):
        rv = f"{self._component_type}: X = {self._impedance:.4g} Ω, \t{self._component_value:.4g}"
        rv += " H" if self._impedance > 0 else " F"
        return rv

class L_section_matching:
    def __init__(self, input_impedance, output_impedance, frequency=None):
        self._Z_1 = input_impedance
        self._Z_2 = output_impedance
        self._conversion_type = "down_conversion" if self._Z_1.real >= self._Z_2.real else "up_conversion"
        
        self._frequency=frequency
        self._shunt_element = ()
        self._series_element = ()

    def match(self):
        R_1 = self._Z_1.real
        X_1 = self._Z_1.imag
        R_2 = self._Z_2.real
        X_2 = self._Z_2.imag

        if R_1 >= R_2:
            """
            shunt - series configuration (down coversion)
            
            %                                jX_b
            %                            +--------+
            %             +-----------+--+        +----+
            %             |           |  +--------+
            %             |           |
            %             |           |
            %            +++         +++
            % Z_1 =      | |         | | jX_a          Z_2 = R_2 + jX_2
            % R_1 + jX_1 | |         | |
            %            +++         +++
            %             |           |
            %             |           |
            %             |           |
            %             +-----------+----------------+
            
            """

            X_a_1 = (R_1*X_2 + R_2*X_1 - R_1*(X_2 - ((R_2*(R_1**2 - R_2*R_1 + X_1**2))/R_1)**(1/2)))/(R_1 - R_2)
            X_b_1 = X_2 - ((R_2*(R_1**2 - R_2*R_1 + X_1**2))/R_1)**(1/2)

            X_a_2 = (R_1*X_2 + R_2*X_1 - R_1*(X_2 + ((R_2*(R_1**2 - R_2*R_1 + X_1**2))/R_1)**(1/2)))/(R_1 - R_2)
            X_b_2 = X_2 + ((R_2*(R_1**2 - R_2*R_1 + X_1**2))/R_1)**(1/2)
     

        if R_1 < R_2:
            """ series - shunt configuration (up conversion)
            
            %                       jX_b
            %                      +--------+
            %              +-------+        +----+--------------+
            %              |       +--------+    |
            %              |                     |
            %              |                     |
            %             +++                   +++
            % Z_1 =       | |                   | | jX_a          Z_2 = R_2 + jX_2
            % R_1 + jX_ 1 | |                   | |
            %             +++                   +++
            %              |                     |
            %              |                     |
            %              |                     |
            %              +---------------------+---------------+
            """

            X_a_1 = (R_1*X_2 + (R_1*R_2*(R_2**2 - R_1*R_2 + X_2**2))**(1/2))/(R_1 - R_2)
            X_b_1 = -(R_2*X_1 - (R_1*R_2*(R_2**2 - R_1*R_2 + X_2**2))**(1/2))/R_2

            X_a_2 = (R_1*X_2 - (R_1*R_2*(R_2**2 - R_1*R_2 + X_2**2))**(1/2))/(R_1 - R_2)
            X_b_2 = -(R_2*X_1 + (R_1*R_2*(R_2**2 - R_1*R_2 + X_2**2))**(1/2))/R_2


        self._shunt_element = Component(impedance=X_a_1, frequency=self._frequency), Component(impedance=X_a_2, frequency=self._frequency)
        self._series_element = Component(impedance=X_b_1, frequency=self._frequency), Component(impedance=X_b_2, frequency=self._frequency)
        
        return self
       
    def get_solutions(self):
        self.match()
        return f"{self._shunt_element},\n {self._series_element}"
    
        
    def __repr__(self):
        rv = f"From {self._Z_1} Ω to {self._Z_2} Ω\n\n"
        rv += "Down-conversion (shunt-series)" if self._conversion_type == "down_conversion" else "Up-conversion (series-shunt)"
        rv += "\n\n"
        if self._conversion_type == "down_conversion":
            rv += f"[shunt {self._shunt_element[0]}, series {self._series_element[0]}]\n"
            rv += f"[shunt {self._shunt_element[1]}, series {self._series_element[1]}]"                
        elif self._conversion_type == "up_conversion":
            rv += f"[series {self._series_element[0]}, shunt {self._shunt_element[0]}]\n"
            rv += f"[series {self._series_element[1]}, shunt {self._shunt_element[1]}]"              
        return rv






print (L_section_matching(input_impedance=100, output_impedance=10, frequency=32).match() )





