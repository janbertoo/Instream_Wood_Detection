import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from math import atan2, cos, sin, sqrt, pi
from multiprocessing import Pool
import shutil

#the following path contains all the cropped bounding boxes
path = '/home/jean-pierre/scratch/allWoods200/'
newpath = '/home/jean-pierre/scratch/allWoods200_normalized_centered_rotated/'

if os.path.exists(newpath) == True:
    shutil.rmtree(newpath)
    os.mkdir(newpath)
else:
    os.mkdir(newpath)

coresAmount = os.cpu_count()

def detect45or135andRotateAndWrite(imName):
    path = '/home/jean-pierre/scratch/allWoods200_normalized_centered/'
    newpath = '/home/jean-pierre/scratch/allWoods200_normalized_centered_rotated/'
    try:
        #read in grayscale    
        img = cv2.imread(os.path.join(path,imName), cv2.IMREAD_GRAYSCALE)
    except:
        print("Something went wrong, "+imName+" can not be read")
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
        img = cv2.flip(img,1)
    else:
        angle = 0
    
    cv2.imwrite(os.path.join(newpath,imName), img)
    
    #return(angle)

jpgList = []

for file in os.listdir(path):
    if file[-4:] == '.jpg':
        jpgList.append(file)

if __name__ == '__main__':
    with Pool(coresAmount) as p:
        p.map(detect45or135andRotateAndWrite, jpgList)
