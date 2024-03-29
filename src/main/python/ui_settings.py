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

    self.menuBar.setNativeMenuBar(True)

    self.actionCheck_for_Updates.triggered.connect(self.check_for_updates)
    self.action_Exit.triggered.connect(self.quit_app)

    self.action_LumpedMatching.triggered.connect(self.launch_lumped_matching)
    self.actionMicrostripMatching.triggered.connect(self.launch_microstrip_matching)
    self.action_IntegratedMatching.triggered.connect(self.launch_integrated_matching)
    self.action_Smith_Chart.triggered.connect(self.launch_smith_chart)
    self.actionrect2polar.triggered.connect(self.launch_rect2polar)
    self.action_gamma2imp.triggered.connect(self.launch_gamma2impedance)
    self.action_lambda4_transformer.triggered.connect(self.launch_lambda4)
    self.actionStub.triggered.connect(self.launch_stub_matching)

    self.actionY_formulas.triggered.connect(self.open_Y_formulas)
    self.actionS_formulas.triggered.connect(self.open_S_formulas)
    self.action_Datasheet_Y.triggered.connect(self.open_datasheet_Y)
    self.action_Datasheet_S.triggered.connect(self.open_datasheet_S)

    self.action_About_2.triggered.connect(self.open_about_window)


def init_ui(self):

    # set window title, overwriting window title in syRF_ui.py
    self.setWindowTitle("syRF")

    setup_menu_bar(self)

    # self.tabWidget.setCurrentIndex(1)
    self.radiobutton_2n4957.setChecked(True)
    self.radioButton1_MRF571.setChecked(True)

    self.f0_box_2.setFocus()  # set focus on frequency of Y tab on startup

    self.radioButton_CE.setChecked(
        True
    )  # radioButton is checked on startup. Common emitter is the default config.
    self.radioButton_MRF571.setChecked(True)  # radioButton_MRF571 is the default
    self.radioButton_5.setChecked(True)  # insert impedance as Z is the default
    self.Fill_ys_yl_opt_button.setEnabled(False)

    # self.Z0_box.setEnabled(False) # Z0 is disabled by default, i.e. it's fixed @ 50 ohm
    self.plot_isc_button_2.setEnabled(False)

    # on startup check on remote repo whether there is a
    # new commit and notify the user by updating the label

    # self.label_updates.setText(check_update.check())

    #### comment this out to skip the update check on startup.
    # check_update.check(self)
