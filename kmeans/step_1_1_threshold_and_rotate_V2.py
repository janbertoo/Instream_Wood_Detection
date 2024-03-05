import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import atan2, cos, sin, sqrt, pi

testIm = '/home/jean-pierre/scratch/allWoods200/20201117_rotated__1pi2__image000036_cut1.jpg'

testIm = '/home/jean-pierre/scratch/allWoods200/20201117_rotated__1pi2__image000514_cut1.jpg'

testIm = '/home/jean-pierre/scratch/allWoods200/20201117_rotated__1pi2__image000603_cut2.jpg'


def detect45or135(imPath):
    try:
        #read in grayscale    
        img = cv2.imread(testIm, cv2.IMREAD_GRAYSCALE)
    except:
        print("Something went wrong, "+imPath+" can not be read")
    #blur the image
    blur = cv2.GaussianBlur(img,(5,5),0)
    #create thresholds
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    #calculate X-edges
    resX=cv2.Sobel(th3,cv2.CV_64F,0,1,ksize=3)
    X = np.sum(resX == 255)

    #calculate Y-edges
    resY=cv2.Sobel(th3,cv2.CV_64F,1,0,ksize=3)
    Y = np.sum(resY == 255)

    alpha = 45
    tot45 = sqrt((Y*sin(alpha))**2 + (X*cos(alpha))**2)

    alpha = 135
    tot135 = sqrt((Y*sin(alpha))**2 + (X*cos(alpha))**2)

    if tot45 > tot135:
        angle = 135
    elif tot135 > tot45:
        angle = 45
    else:
        angle = 0
    
    return(angle)
    





img = cv2.imread(testIm, cv2.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

resX=cv2.Sobel(th3,cv2.CV_64F,0,1,ksize=3)
X = np.sum(resX == 255)

resY=cv2.Sobel(th3,cv2.CV_64F,1,0,ksize=3)
Y = np.sum(resY == 255)

alpha = 45

#print(sin(90))
tot = sqrt((Y*sin(alpha))**2 + (X*cos(alpha))**2)
print(tot)
#cv2.imshow(tot)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
resX=cv2.Sobel(th3,cv2.CV_64F,0,1,ksize=3)
X = np.sum(resX == 255)

resY=cv2.Sobel(th3,cv2.CV_64F,1,0,ksize=3)
Y = np.sum(resY == 255)

alpha = 135

#print(sin(90))
tot = sqrt((Y*sin(alpha))**2 + (X*cos(alpha))**2)
print(tot)