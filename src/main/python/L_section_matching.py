#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 19 15:38:35 2018

@author(s)   : Francesco Urbani
@file        : L_section_matching_tab.py
@descritpion : 

"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import cmath
import matching_network as mn


msg_error = ""  # display nothing if error occurs
# msg_error = "<font color='#E8E8E8'>ERR</font>"


######################################################################
"""
piece of code needed to remove ascii formatting from the 
output of `mn.L_section_matching(input_impedance, output_impedance, f0).match()`
"""
import re


def plain_text(text):
    # 7-bit C1 ANSI sequences
    ansi_escape = re.compile(
        r"""
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
        """,
        re.VERBOSE,
    )
    result = ansi_escape.sub("", text)
    return result


######################################################################


def compute_L_section_matching(self):

    # read frequency
    try:
        f0 = float(self.f0_box.text())
        f0 = f0 * 1e6  # MHz / Hz conversion
    except Exception as e:
        f0 = None

    # read input impedance/admittance
    input_unit = self.comboBox.currentText()
    # set label right
    label_72_txt = (
        "Input (Y<sub>L</sub>)"
        if input_unit == "Admittance [mS]"
        else "Input (Z<sub>L</sub>)"
    )
    self.label_72.setText(label_72_txt)

    try:
        input_impedance = complex(self.input_box.text())
        if input_unit == "Admittance [mS]":
            input_admittance = input_impedance
            input_impedance = (input_admittance * 1e-3) ** (-1)
        else:
            # input_admittance in mS
            input_admittance = input_impedance ** (-1) * 1e3  # 1e3 shifts from S to mS
    except Exception as e:
        input_impedance = msg_error
        input_admittance = msg_error

    # read output impedance/admittance
    output_unit = self.comboBox_2.currentText()
    # set label right
    label_73_txt = (
        "Output (Y<sub>0</sub>)"
        if output_unit == "Admittance [mS]"
        else "Output (Z<sub>0</sub>)"
    )
    self.label_73.setText(label_73_txt)

    try:
        output_impedance = complex(self.output_box.text())
        if output_unit == "Admittance [mS]":
            output_admittance = output_impedance
            output_impedance = (output_admittance * 1e-3) ** (-1)
        else:
            output_admittance = output_impedance ** (-1) * 1e3
    except Exception as e:
        output_impedance = msg_error
        output_admittance = msg_error

    try:
        mn1 = mn.L_section_matching(input_impedance, output_impedance, f0).match()
        result = str(mn1)
        result = plain_text(result)
    except Exception as e:
        result = "insert correct inputs"

    self.textBrowser.setText(f"{result}")

    self.imp_input_box.setText(str(input_impedance))
    self.adm_input_box.setText(str(input_admittance))
    self.imp_output_box.setText(str(output_impedance))
    self.adm_output_box.setText(str(output_admittance))


def clean_all_L_section_matching(self):
    pass


######### not used ?
def to_eng_form(x):
    si_prefixes = {
        9: "P",
        9: "G",
        6: "M",
        3: "k",
        0: "",
        -3: "m",
        -6: "u",
        -9: "n",
        -12: "p",
        -15: "f",
    }
    for e in sorted(si_prefixes, reverse=True):
        if x >= 10**e:
            return x / 10**e, si_prefixes[e]
    return x, ""
