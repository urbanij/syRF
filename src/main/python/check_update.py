#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Feb 17 13:54:49 CET 2019

@author(s)   : Francesco Urbani
@file        : check_updates.py
@descritpion : 

"""

try:
    import requests
except ModuleNotFoundError as e:
    print(e)

LOCAL_VERSION_FILE = "../../../.version"
REMOTE_VERSION_URL = 'https://raw.githubusercontent.com/urbanij/syRF/master/.version'

import check_update_window
import new_update


def get_version():
    try:
        with open(LOCAL_VERSION_FILE ,  "r") as f:
            return (f.read()) 
    except FileNotFoundError as e:
        print ("File {} does not exists.".format(LOCAL_VERSION_FILE))
        return 


def get_remote_version():
    try:
        remote_version = requests.get(REMOTE_VERSION_URL).text
        return remote_version
    except NameError as e:
        print(e)
    except Exception as e:
        print ("Remote file at {} does not exists.".format(REMOTE_VERSION_URL))
        return 

    

    
def check(self, call=False): # call is true if the function is called from "Check for updates..." in menu bar
    local_version  = get_version()
    remote_version = get_remote_version()
    
    if (remote_version != local_version):
        # return "<font color='#BA0000'>New update available (v.{})</font>".format(remote_version)
        window = new_update.mainProgram(self)
        window.show()
    else:
        # return "<font color='#1A7C32'>syRF is up to date.</font>"
        # return ""
        if call :
            window = check_update_window.mainProgram(self)
            window.show()
        pass

