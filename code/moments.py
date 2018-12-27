#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:36:49 2017

@author: arushigupta148
"""
import cv2
import math
import numpy as np
from numpy import mgrid, sum

def moment(filename):
    
    image=cv2.imread(filename,0)
    image=np.array(image)
    
    arr=cv2.moments(image)
    
    gx=math.sqrt(arr['mu20']/arr['m00'])
    gy=math.sqrt(arr['mu02']/arr['m00'])
    gxy=math.sqrt((arr['mu20']+arr['mu02'])/arr['m00'])
    
    
    sx=arr['mu30']/(arr['mu20']**2)**(1./3)    
    sy=arr['mu03']/(arr['mu02']**2)**(1./3)
    
    """
    kx=(arr['mu40']/(arr['mu20']**2))-3
    print kx
    
    ky=(arr['mu04']/(arr['mu02']**2))-3
    print ky
    """
    assert len(image.shape) == 2 # only for grayscale images        
    x, y = mgrid[:image.shape[0],:image.shape[1]]
    moments = {}
    moments['mean_x'] = sum(x*image)/sum(image)
    moments['mean_y'] = sum(y*image)/sum(image)
    
    moments['mu40'] = sum((x-moments['mean_x'])**4*image) 
    kx=(moments['mu40']/(arr['mu20']**2))-3
       
    moments['mu04'] = sum(x**4*image)
    ky=(moments['mu04']/(arr['mu02']**2))-3
    return gx,gy,gxy,sx,sy,kx,ky