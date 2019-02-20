#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mar 19 15:38:35 2018

@author(s)   : Francesco Urbani
@file        : main.py
@descritpion : The main file

"""


import check_update

                




def setup_menu_bar(self):
    ### setup menu bar
    ### Uncomment to disable native menubar on Mac
    self.menuBar.setNativeMenuBar(False)


    self.action_About_2.triggered.connect(self.open_about_window)
    self.action_Exit.triggered.connect(self.quit_app)

    self.action_Lumped_Matching.triggered.connect(self.launch_lumped_matching)
    self.actionMicrostrip_Matching.triggered.connect(self.launch_microstrip_matching)
    self.action_Smith_Chart.triggered.connect(self.launch_smith_chart)

    self.actionrect2polar.triggered.connect(self.launch_rect2polar)
    self.action_lambda4.triggered.connect(self.launch_lambda4)

    self.actionY_formulas.triggered.connect(self.open_Y_formulas)
    self.actionS_formulas.triggered.connect(self.open_S_formulas)
    self.action_Datasheet_Y.triggered.connect(self.open_datasheet_Y)
    self.action_Datasheet_S.triggered.connect(self.open_datasheet_S)



    
        


def init_ui(self):
    # on startup check on remote repo whether there is a 
    # new commit and notify the user by updating the label
    self.label_updates.setText(check_update.check())

    # set window title, overwriting window title in syRF_ui.py
    self.setWindowTitle("syRF")


    setup_menu_bar(self)


    # self.tabWidget.setCurrentIndex(1)
    self.checkBox.setChecked(True)
    self.checkBox_2.setChecked(True)

    self.f0_box_2.setFocus()  # set focus on frequency of Y tab on startup



    self.radioButton_CE.setChecked(True) # radioButton is checked on startup. Common emitter is the default config.
    self.radioButton_MRF571.setChecked(True) # radioButton_MRF571 is the default
    self.radioButton_5.setChecked(True) # insert impedance as Z is the default
    self.Fill_ys_yl_opt_button.setEnabled(False)

    # self.Z0_box.setEnabled(False) # Z0 is disabled by default, i.e. it's fixed @ 50 ohm
    self.plot_isc_button_2.setEnabled(False)

