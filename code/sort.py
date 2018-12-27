#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:47:39 2017

@author: arushigupta148
"""
from PIL import *
import numpy as np
import cv2
from matplotlib import pyplot as plt
import scipy
from scipy import ndimage
from PIL import Image,ImageEnhance
from pylab import *
from skimage import data, io, filter
import mahotas as mh
import mahotas.demos
import matplotlib
from cell import func1
from test import func2
from double import func3
from separate import func4
import pandas as pd
from matplotlib.pyplot import savefig
    
def func5(image,filename,count):
    outer = []
    inner = []
    total = []
    #backgound and noise removal
    print filename
    contrast = 1.0
    enhancer = ImageEnhance.Contrast(Image.fromarray(image))
    con = enhancer.enhance(contrast)
    
    f = mh.gaussian_filter(con, 5.5)
    T = mh.otsu(np.uint64(f))
    f = (f>T)
    imshow(f)
    show()

    labeled, n_nucleus  = mh.label(f)
    print('Found {} nuclei.'.format(n_nucleus))
    imshow(labeled)
    show()
    if count>0:
        count=count+1
    else:
        matplotlib.image.imsave('pic01.jpg',labeled,cmap=cm.gray)
    
    labeled = mh.labeled.remove_bordering(labeled)
    imshow(labeled)
    show()
    
    sizes = mh.labeled.labeled_size(labeled)
    print sizes
    too_small = np.where(sizes < 500)
    labeled = mh.labeled.remove_regions(labeled, too_small)
    imshow(labeled)
    show()

    relabeled, n_left = mh.labeled.relabel(labeled)
    print('After filtering and relabeling, there are {} nuclei left.'.format(n_left))
    imshow(relabeled)
    show()
    if count>0:
        matplotlib.image.imsave('pic3.jpg',relabeled,cmap=cm.gray)
    else:
        matplotlib.image.imsave('pic02.jpg',relabeled,cmap=cm.gray)
        count=count+1

    
    size= mh.labeled.labeled_size(relabeled)
    print sorted(size)
    matplotlib.image.imsave('2.jpg',relabeled)
    filenames="2.jpg"

    if count>0:
        cnt=24
    else:
        cnt=10

    value= n_left

    t=0
    r2=0
    a=127
    if value==0: 
        closing=func4(filename)
        value = func5(closing,filename,1) 
    elif sizes[1] >2000000:
        closing=func4(filename)
        value = func5(closing,filename,1) 
    elif n_nucleus>cnt:
            closing=func4(filename)
            value = func5(closing,filename,1) 
    elif value>30:
        closing=func4(filename)
        value= func5(closing,filename,0) 
    else:

        image=cv2.imread(filename,0)
        if value==1:
            r1,r2=func1(filenames,image)
            number=1
            t=r1-r2
            outer.append(t)
            inner.append(r2)
            r=r1/r2
            total.append(r1)
        elif value>5:
            count=count+1
            hr=value/2
            sort= sorted(zip(size), reverse=False)[0:hr+1]
            print sort
            m=max(sort)
            print m
            too_small = np.where(size > m)
            relabeled = mh.labeled.remove_regions(relabeled, too_small)
            imshow(relabeled)
            show()
            matplotlib.image.imsave('r.jpg',relabeled)
            matplotlib.image.imsave('pic4.jpg',labeled,cmap=cm.gray)
            name="r.jpg"
            range1 = func2(name,image)
            number=range1+1
            for i in range(range1+1):
                filename1 = "til" + str(i) + ".png"
                while(r2<=5):
                    if a<255:
                        r1,r2=func3(filename1,a)
                        a=a+40
                        print a
                        print r2
                    else:
                        break
                a=127
                t=r1-r2
                outer.append(t)
                inner.append(r2)
                r=r1/r2
                total.append(r1)
                r2=0
        else:
            range1 = func2(filenames,image)
            for i in range(range1+1):
                filename1 = "til" + str(i) + ".png"
                while(r2<=5):
                    if a<255:
                        r1,r2=func3(filename1,a)
                        a=a+40
                        print a
                        print r2
                    else:
                        break
                a=127
                t=r1-r2
                outer.append(t)
                inner.append(r2)
                r=r1/r2
                total.append(r1)
                r2=0

        df = pd.DataFrame()
        df["thickness"] = outer
        df["inner"] = inner
        df["total"] = total
        df.index+=1  
        print df
        df.to_csv("Dataframe.csv")
        number=len(outer)
        
        ind = np.arange(number) 
        width = 0.2     
        
        fig, ax = plt.subplots()
        ax.set_title('Thickness of virulent cells')
        labels = []
        for i in range(number):
            
            rects1 = ax.bar(ind, outer, width, color='r', align='center')
            rects2 = ax.bar(ind + width, inner, width, color='g', align='center')
            rects3 = ax.bar(ind + width+width, total, width, color='b', align='center')
            if outer[i] >= 1.7:
                labels.append("cell"+str(i+1))
            else:
                labels.append("cell"+str(i+1)+" (Incorrect)")
        
        ax.set_xticks((ind + width))
        ax.legend((rects1[0], rects2[0], rects3[0]), ('Capsule Thickness', 'Cell Radius','Overall Radius'))
        ax.set_xticklabels(labels)

        savefig("pic.jpg",bbox_inches="tight")
        plt.show()
        print value

    return value