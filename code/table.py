#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:51:14 2017

@author: arushigupta148
"""
from cell import new1
import pandas as pd

X = pd.DataFrame(columns=["inner_radius","outer_radius","radius_ratio","inner_area", "outer_area", "area_ratio"])

for i in range(1,4):
    print "loop - ",i
    filename = 'cell' + str(i) + ".JPG"
    new_list = new1(filename)
    print "list is - ",new_list
    X.loc[i] = new_list

X.to_csv("Data_Table_Preprocessed.csv")
