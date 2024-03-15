import cv2
import os
import numpy as np
import shutil
from multiprocessing import Pool
#from keras.preprocessing.image import ImageDataGenerator

#the following path contains all the cropped bounding boxes
orPath = '/home/jean-pierre/scratch/allWoods200'
newPath =  '/home/jean-pierre/scratch/allWoods200_normalized_centered'

pixelRange = 256

coresAmount = os.cpu_count()

try:
    os.mkdir(newPath)
except:
    shutil.rmtree(newPath)
    os.mkdir(newPath)

orPaths = []

for file in os.listdir(orPath):
    orPaths.append(file)

def normalizecenter(file):
    if file[-4:] == '.jpg':
        image = cv2.imread(os.path.join(orPath,file), cv2.IMREAD_GRAYSCALE)
        mean = np.mean(image)
        image = image - mean
        min = np.min(image)
        max = np.max(image)

        if max > abs(min):
            multiplicationRatio = ( pixelRange / 2 ) / ( max )
        else:
            multiplicationRatio = ( pixelRange / 2 ) / ( abs(min) )
        
        image = ( image * multiplicationRatio ) + ( pixelRange / 2 )

        for n in range(len(image)):
            for m in range(len(image[0])):
                image[n,m] = int(round(image[n,m]))
        #print(os.path.join(newPath,file))
        cv2.imwrite(os.path.join(newPath,file), image)

if __name__ == '__main__':
    with Pool(coresAmount) as p:
        p.map(normalizecenter, orPaths)
