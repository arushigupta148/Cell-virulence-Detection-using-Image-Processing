#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:30:05 2017

@author: arushigupta148
"""

from imutils import contours
import imutils
from skimage import measure
from PIL import *
import numpy as np
import cv2
from matplotlib import pyplot as plt
import scipy
from scipy import ndimage
from PIL import Image,ImageEnhance
from pylab import *
from skimage import data, io, filter

def func2(filename,image):
    im1=cv2.imread(filename,0)
    ret,thresh = cv2.threshold(im1,127,255,0)
    cont, contour, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    out = np.zeros_like(thresh)
    cv2.drawContours(out, contour, -1, 255, 3)
    cnt=contour[0]
    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (x,y)
    print center
    print radius
    im = cv2.bitwise_not(im1)
    imshow(im,cmap=cm.gray)
    show()


    #extract only boundaries
    arr=np.array(im)
    print arr
    ori=np.array(image)
    print ori
    print arr.shape
    new=np.zeros([arr.shape[0],arr.shape[1]])
    
    for i in range(len(arr)):
        for j in range(arr.shape[1]):
            if arr[i][j]>=225:
                new[i][j]=255
            else:
                new[i][j]=ori[i][j]
    print new
    matplotlib.image.imsave('pic4.jpg',new,cmap=cm.gray)
    matplotlib.image.imsave('new.jpg',new,cmap=cm.gray)
    
    
    #invert image to extract each cell in test.py
    image=cv2.imread('new.jpg',0)
    im1 = cv2.bitwise_not(image)
    imshow(im1,cmap=cm.gray)
    show()
    
    
    contrast =10
    enhancer = ImageEnhance.Contrast(Image.fromarray(im1))
    con = enhancer.enhance(contrast)
    imshow(con,cmap=cm.gray)
    show()
    matplotlib.image.imsave('test.jpg',con,cmap=cm.gray)

    image=cv2.imread('test.jpg',0)
    array1=np.array(image)
    
    thresh = cv2.threshold(array1, 200, 255, cv2.THRESH_BINARY)[1]
    labels = measure.label(thresh, neighbors=8, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")
     
    # loop over the unique components
    for label in np.unique(labels):
    	# if this is the background label, ignore it
    	if label == 0:
    		continue
     
    	# otherwise, construct the label mask and count the
    	# number of pixels 
    	labelMask = np.zeros(thresh.shape, dtype="uint8")
    	labelMask[labels == label] = 255
    	numPixels = cv2.countNonZero(labelMask)
     
    	# if the number of pixels in the component is sufficiently
    	# large, then add it to our mask of "large blobs"
    	if numPixels > 10:
    		mask = cv2.add(mask, labelMask)
            
    
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    cnts = contours.sort_contours(cnts)[0]
    
    # loop over the contours
    image1=cv2.imread('new.jpg')
    size=128,128
    for (i, c) in enumerate(cnts):
        (x,y,w,h)=cv2.boundingRect(c)
        print x,y,w,h
        ((cX,cY),radius)=cv2.minEnclosingCircle(c)
        cv2.circle(image1, (int(cX), int(cY)), int(radius),(255, 0, 255), 3)
        cv2.putText(image1, "#{}".format(i + 1), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 255), 9)
        img = Image.open('new.jpg')
        box = (x, y, x+w, y+h)
        area = img.crop(box)
        area.thumbnail(size, Image.ANTIALIAS)
        til = Image.new("RGB",(300,300),"white")
        til.paste(area,(100,100))
        til.save("til" + str(i) + ".png")
    
    imshow(image1,cmap=cm.gray)
    show()
    matplotlib.image.imsave('pic5.jpg',image1,cmap=cm.gray)
    return i