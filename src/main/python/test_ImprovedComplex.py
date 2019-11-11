#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Nov 10 11:00:27 CET 2019

@author(s)   : Francesco Urbani
@file        : test_ImprovedComplex.py
@descritpion : test suite for ImprovedComplex

"""



""" $ pytest test_ImprovedComplex.py -v """
import pytest
from ImprovedComplex import ImprovedComplex

@pytest.fixture
def get_sum_test_data():
        return [1+2j, 1-32j, -23+43j, 0]

def test_Complex(get_sum_test_data):
    for data in get_sum_test_data:
        assert complex(ImprovedComplex(data)) == data

