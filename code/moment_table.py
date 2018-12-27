#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:00:56 2017

@author: arushigupta148
"""
import pandas as pd
from moments import moment

X = pd.DataFrame(columns=["gyradius-x","gyradius-y","gyradius-xy","skewness-x","skewness-y","kurtosis-x","kurtosis-y"])
for i in range(0,9):
    print "loop - ",i
    filename = 'til' + str(i) + ".png"
    new_list = moment(filename)
    print "list is - ",new_list
    X.loc[i] = new_list

X.to_csv("Data_Table_Preprocessed1.csv")