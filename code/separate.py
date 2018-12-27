
import numpy as np
import cv2
from matplotlib import pyplot as plt
from pylab import *
def func4(filename):
    img=cv2.imread(filename)
    pic = cv2.imread(filename,0)
    
    blurred = cv2.GaussianBlur(pic, (11, 11), 0)
    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
    kernel = np.ones((3,3),np.uint8)
    thresh = cv2.erode(thresh, kernel, iterations=1)
    thresh = cv2.dilate(thresh, kernel, iterations=4)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    imshow(closing,cmap=cm.gray)
    show()
    matplotlib.image.imsave('pic2.jpg',closing,cmap=cm.gray)
    """
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    
    # sure background area
    sure_bg = cv2.dilate(opening,kernel,iterations=3)
    imshow(sure_bg,cmap=cm.gray)
    show()
    
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.4*dist_transform.max(),255,0)
    imshow(dist_transform,cmap=cm.gray)
    show()
    imshow(sure_fg,cmap=cm.gray)
    show()
    
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg,sure_fg)
    imshow(sure_fg,cmap=cm.gray)
    show()
    imshow(unknown,cmap=cm.gray)
    show()
    
    ret, markers = cv2.connectedComponents(sure_fg)
    
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers+1
    
    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0
    imshow(markers,cmap=cm.gray)
    show()
    
    markers = cv2.watershed(img,markers)
    img[markers == -1] = [255,0,0]
    imshow(img,cmap=cm.gray)
    show()
    """
    return closing