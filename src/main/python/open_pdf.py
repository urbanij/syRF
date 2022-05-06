#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Feb 14 12:58:33 CET 2019

@author(s)   : Francesco Urbani
@file        : open_pdf
@descritpion : 

"""
import os
import sys


def open_pdf(file_path):
    try:
        if sys.platform == "linux":
            os.system("xdg-open {}".format(file_path))
        elif sys.platform == "darwin":
            os.system("open {}".format(file_path))
        elif sys.platform[:3] == "win":
            os.system('start "" {}'.format(file_path))
    except Exception as e:
        print("Can't open the pdf {}.".format(file_path))
