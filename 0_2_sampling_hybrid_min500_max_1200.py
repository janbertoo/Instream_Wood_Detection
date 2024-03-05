import os
import random
import shutil
import numpy as np
import pickle

minImgs = 500
maxImgs = 1200

newFolderName = 'jpgs_'+str(minImgs)+'_'+str(maxImgs)+'_MinMax'

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
paths = [
    '/home/jean-pierre/scratch/unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages'
]
'''
#samplesPerDataset = [1429,601,1076,478,344,2478,2146,191,18,138,1046,1034,157,2340,1236,116,81,176,134,9]

#define folder to be counted
originalToCount = 'jpgs'
#create empty variable to store the folder and the amount of jpgs in
samplesPerDataset = []

#get a list of the amount of samples per dataset
for path in paths:
    count = 0
    jpgsFolder = os.path.join(path,originalToCount)
    files = os.listdir(jpgsFolder)
    for filee in os.listdir(os.path.join(path,originalToCount)):
        if filee[-4:] == '.jpg':
            count = count + 1
    samplesPerDataset.append((path,count))

samplesPerDatasetAdjusted = []

for dataset in samplesPerDataset:
    #print(dataset[1])
    number = dataset[1]
    if number < minImgs:
        samplesPerDatasetAdjusted.append((dataset[0],minImgs))
    if minImgs <= number < maxImgs:
        samplesPerDatasetAdjusted.append((dataset[0],number))
    if number > maxImgs:
        samplesPerDatasetAdjusted.append((dataset[0],maxImgs))

print(samplesPerDatasetAdjusted)

#create folder and copy the correct amount of images into the folder
for pathAndNumber in samplesPerDatasetAdjusted:
    #define new path name
    newPathName = os.path.join(pathAndNumber[0],newFolderName)
    #create new folder
    try:
        os.mkdir(newPathName)
    #if folder already exists, delete it and create it
    except:
        print('folder already exists')
        shutil.rmtree(newPathName)
        os.mkdir(newPathName)
    
    #define new path name
    newTxtPathName = newPathName.replace('/jpgs','/txts')
    #create new folder
    try:
        os.mkdir(newTxtPathName)
    #if folder already exists, delete it and create it
    except:
        print('folder already exists')
        shutil.rmtree(newTxtPathName)
        os.mkdir(newTxtPathName)
    
    #create empty list to store all the jpgs in that are in the '/jpgs/' folder of that specific dataset
    jpgList = []
    #fille the list
    for filee in os.listdir(os.path.join(pathAndNumber[0],originalToCount)):
        if filee[-4:] == '.jpg':
            jpgList.append(filee)
    
    # create empty list to store the selected jpgs for the experiment
    selectedJpgList = []
    
    #in case the amount of jpgs to be picked is larger then the amount of jpg available, first add all jpgs to the list and then randomly fill the list with duplicates
    if len(jpgList) < pathAndNumber[1]:
        selectedJpgList = jpgList
        for i in range(pathAndNumber[1]-len(jpgList)):
            selectedJpgList.append(jpgList[random.randrange(0,len(jpgList))])
    
    #in case the amount of jpgs are exactly the same as the required amount to be picked, put all jpgs in selected jpgs list
    if len(jpgList) == pathAndNumber[1]:
        selectedJpgList = jpgList
    
    #in case the amount of jpgs is larger than the amount to be picked, randomly pick the amount without duplicates
    if len(jpgList) > pathAndNumber[1]:
        selectedJpgList = np.random.choice(jpgList, pathAndNumber[1], replace = False)
    
    selectedJpgList.sort()

    #store the selected images in the respective folder
    output = open(os.path.join(path,newFolderName+'_selected.pickle'), 'wb')
    pickle.dump(selectedJpgList, output)

    print(len(selectedJpgList))

    #now copy the selected files from the jpgs folder to the newly created folder
    count = 1
    for selectedJpg in selectedJpgList:
        orJpgPath = os.path.join(pathAndNumber[0],'jpgs',selectedJpg)
        while True:
            outJpgPath = os.path.join(pathAndNumber[0],newFolderName,selectedJpg.replace('.jpg',('-'+str(count)+'.jpg')))
            if os.path.exists(outJpgPath) == False:
                shutil.copy(orJpgPath,outJpgPath)
                shutil.copy( (orJpgPath.replace('/jpgs/','/txts/')).replace('.jpg', '.txt'),(outJpgPath.replace('/jpgs','/txts')).replace('.jpg', '.txt') )
                count = 1
                break
            count = count + 1

