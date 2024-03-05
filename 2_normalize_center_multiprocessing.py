import os
import cv2
import shutil
import sys
import numpy as np
from multiprocessing import Pool

#define a version name for the experiment
nameExtension = 'trimmedV2'
#define/detect amount of cores
#coresAmount = 4
coresAmount = os.cpu_count()

#define the range in which the pixels are categorized in the image (normally 255)
#if different from 255, change the np.uint8 to the correct value in the code down below
pixelRange = 255


#add all folder with labeled data in a separate 'jpgs' ('/path/to/folder/jpgs') folder and the corresponding YOLO labels in a 'txts' ('/path/to/folder/txts') folder
paths = [
	'/home/jean-pierre/scratch/20201117_rotated/1pi2/labeled_20201117_1pi2_c3'
]
'''

paths = [
    '/home/jean-pierre/scratch/20201117_rotated/1pi2/labeled_20201117_1pi2_c3',
    '/home/jean-pierre/scratch/20201117_rotated/2pi4/labeled_20201117_2pi4_c1',
    '/home/jean-pierre/scratch/20201117_rotated/3SamsungGalaxyA5/labeled_20201117_3SamsungGalaxyA4_OC',
    '/home/jean-pierre/scratch/20201117_rotated/4XiaomiRedmi4X/labeled_20201117_4XiaomiRedmi4X_OC',
    '/home/jean-pierre/scratch/20201119_rotated/1XiaomiRedmi4X/labeled_20201119_1XiaomiRedmi4X_OC',
    '/home/jean-pierre/scratch/20201119_rotated/2pi2/labeled_20201119_2pi2_c3',
    '/home/jean-pierre/scratch/20201119_rotated/3pi4/labeled_20201119_3pi4_c3',
    '/home/jean-pierre/scratch/20201119_rotated/4SamsungGalaxyA5_sampled/labeled_20201119_4SamsungGalaxyA_OC_sampled',
    '/home/jean-pierre/scratch/20201126_rotated/3XiaomiRedmi2_sampled/labeled_20201126_3XiaomiRedmi2_OC2_sampled',
    '/home/jean-pierre/scratch/20201126_rotated/4pi4_c4_sampled/labeled_20201126_4pi4_c4_sampled',
    '/home/jean-pierre/scratch/20201126_rotated/4pi4_c5/labeled_20201126_4pi4_c5',
    '/home/jean-pierre/scratch/20201127_rotated/2pi4/labeled_20201127_2pi4_c2',
    '/home/jean-pierre/scratch/20201203_rotated/1pi4_sampled/labeled_20201203_1pi4_c20_sampled',
    '/home/jean-pierre/scratch/20201203_rotated/3pi2/labeled_20201203_3pi2_c4',
    '/home/jean-pierre/scratch/20201203_rotated/4SamsungGalaxyA5/labeled_20201203_4SamsungGalaxyA5_OC',
    '/home/jean-pierre/scratch/unilyon_and_others/20071123_0756_Ain1/labeled_20071123_0756_Ain1',
    '/home/jean-pierre/scratch/unilyon_and_others/20071123_0956_Ain2/labeled_20071123_0956_Ain2',
    '/home/jean-pierre/scratch/unilyon_and_others/20191125_Allier1/labeled_20191125_Allier1',
    '/home/jean-pierre/scratch/unilyon_and_others/20191223_Allier2/labeled_20191223_Allier2',
    '/home/jean-pierre/scratch/unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages'
]
'''
orPaths = []

for path in paths:
    orPaths.append(os.path.join(path,'jpgs_'+nameExtension+'_not_removed'))

#create an empty variable in which to store the output paths
outPaths = []

#loop trough all the paths in the original paths file to create a normalized_centered folder to put the adjusted images in
for path in orPaths:
    outP = path+'_normalized_centered'
    print(outP)
    outPaths.append(outP)

#now make those paths
for path in outPaths:
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)


def readImageNormalizeCenterAndSave(orPathImg):
    if file[-4:] == '.jpg':
        #read the image into variable
        image = cv2.imread(orPathImg)

        #convert the colors from Blue Green Red (BGR) to Hue Saturation Value (HSV)
        imgHSVint = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #convert the type to float
        imgHSV = imgHSVint.astype(float)

        #calculate the average saturation of the image
        sat_mean = np.mean(imgHSV[:,:,2])
        #subtract the average saturation from the saturation of each individuel pixel
        imgHSV[:,:,2] = imgHSV[:,:,2] - sat_mean

        #determine the pixel with the smallest saturation
        min = np.min(imgHSV[:,:,2])
        #determine the pixel with the highest saturation
        max = np.max(imgHSV[:,:,2])

        #Determine whether the pixel with lowest saturation or the one with highest is the furthest away from 0
        #and then create a multiplication ratio based on the pixel furthest away
        if max > abs(min):
            multiplicationRatio = ( pixelRange / 2 ) / ( max )
        else:
            multiplicationRatio = ( pixelRange / 2 ) / ( abs(min) )
        
        #multiply the Hue band of each individual pixel with the multiplication ratio
        imgHSV[:,:,2] = ( imgHSV[:,:,2] * multiplicationRatio ) + ( pixelRange / 2 )
        imgHSV = np.float32(imgHSV)

        #convert the type back to uint8
        imgHSV = imgHSV.astype(np.uint8)

        #convert colors back from HSV to BGR
        image = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR)

        #create path to which to write the image to
        outPathImg = orPathImg.replace('/jpgs_'+nameExtension+'_not_removed/','/jpgs_'+nameExtension+'_not_removed_normalized_centered/')
        #write the image in the output folder
        cv2.imwrite(outPathImg, image)

listForMultiProcessing = []

#loop through the folders in the original paths
for folder in orPaths:
    #show which folder we are currently working on
    print(folder)
    #loop through the files in this specific folder
    for file in os.listdir(folder):
        print(file)
        #Define the original file path
        orFilePath = os.path.join(folder,file)
        #define the output path of the image
        #outFilePath = orFilePath.replace('/jpgs/','/jpgs_'+nameExtension+'_normalized_centered/')
        #now populate the list
        listForMultiProcessing.append(orFilePath)

print(listForMultiProcessing)
#launch a multiprocessing pool
print('starting muliPool')
if __name__ == '__main__':
    with Pool(coresAmount) as p:
        p.map(readImageNormalizeCenterAndSave, listForMultiProcessing)# (listForMultiProcessing)[0],(listForMultiProcessing)[1],(listForMultiProcessing)[2])