#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Feb 18 18:12:01 CET 2019

@author(s)   : Francesco Urbani
@file        : about.py
@descritpion : About window

               
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from about_ui import Ui_MainWindow


import check_update



DESCRIPTION = """
<b>syRF</b> is an open source CAD tool<br> 
to help you design RF and microwave<br>
circuits.
"""
# It runs on any OS, since it's written in<br>
# Python.<br>
# It's tailored to fully cover the class RF Electronics<br> 
# from the University of Pisa, yet it is still a <br>
# valuable tool for anyone else.


LINKS = """
<a href="https://urbanij.github.io/syRF/">Home Page</a><br>
<a href="https://github.com/urbanij/syRF/issues">Report a bug</a><br>
<a href="https://github.com/urbanij/syRF/graphs/contributors">Credits</a><br>
"""



class mainProgram(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainProgram, self).__init__(parent)
        self.setupUi(self)

        self.label_version.setText("v.{}".format(check_update.get_version()))

        self.label_links.setOpenExternalLinks(True)
        self.label_links.setText(LINKS)
        self.label_description.setText(DESCRIPTION)



    # A key has been pressed!
    def keyPressEvent(self, event):
        # Did the user press the Escape key?
        if event.key() == QtCore.Qt.Key_Escape or event.key() == QtCore.Qt.Key_W:
            self.close()


