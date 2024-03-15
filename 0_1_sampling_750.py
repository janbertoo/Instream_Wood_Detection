import os
import random
import pickle
import shutil

#here we will select 750 random images per dataset. Even if the dataset does not contect 750 images. We will select doubles.
amountInSelection = 750

database_base_path = '/home/jean-pierre/scratch/'

paths = [
    database_base_path+'20201117_rotated/1pi2/labeled_20201117_1pi2_c3',
    database_base_path+'20201117_rotated/2pi4/labeled_20201117_2pi4_c1',
    database_base_path+'20201117_rotated/3SamsungGalaxyA5/labeled_20201117_3SamsungGalaxyA4_OC',
    database_base_path+'20201117_rotated/4XiaomiRedmi4X/labeled_20201117_4XiaomiRedmi4X_OC',
    database_base_path+'20201119_rotated/1XiaomiRedmi4X/labeled_20201119_1XiaomiRedmi4X_OC',
    database_base_path+'20201119_rotated/2pi2/labeled_20201119_2pi2_c3',
    database_base_path+'20201119_rotated/3pi4/labeled_20201119_3pi4_c3',
    database_base_path+'20201119_rotated/4SamsungGalaxyA5_sampled/labeled_20201119_4SamsungGalaxyA_OC_sampled',
    database_base_path+'20201126_rotated/3XiaomiRedmi2_sampled/labeled_20201126_3XiaomiRedmi2_OC2_sampled',
    database_base_path+'20201126_rotated/4pi4_c4_sampled/labeled_20201126_4pi4_c4_sampled',
    database_base_path+'20201126_rotated/4pi4_c5/labeled_20201126_4pi4_c5',
    database_base_path+'20201127_rotated/2pi4/labeled_20201127_2pi4_c2',
    database_base_path+'20201203_rotated/1pi4_sampled/labeled_20201203_1pi4_c20_sampled',
    database_base_path+'20201203_rotated/3pi2/labeled_20201203_3pi2_c4',
    database_base_path+'20201203_rotated/4SamsungGalaxyA5/labeled_20201203_4SamsungGalaxyA5_OC',
    database_base_path+'unilyon_and_others/20071123_0756_Ain1/labeled_20071123_0756_Ain1',
    database_base_path+'unilyon_and_others/20071123_0956_Ain2/labeled_20071123_0956_Ain2',
    database_base_path+'unilyon_and_others/20191125_Allier1/labeled_20191125_Allier1',
    database_base_path+'unilyon_and_others/20191223_Allier2/labeled_20191223_Allier2',
    database_base_path+'unilyon_and_others/randomWoodImages/labeled_2022_randomWoodImages'
]

#loop through all the paths above to do the same thing for each dataset
for path in paths:
    #define the folde to select from
    jpgFolder = os.path.join(path,'jpgs')
    #create empty list to store all jpgs in
    jpgList = []
    #loop trough all files in folder and append the jpgs list if the file is a jpgs
    for file in os.listdir(jpgFolder):
        if file[-4:] == '.jpg':
            jpgList.append(file)
    #create an empty variable for the selected jpgs to be stored in
    selectedJpgList = []
    #randomly select 750 jpgs for the random list
    for i in range(amountInSelection):
        selectedJpgList.append(jpgList[random.randrange(0,len(jpgList))])
    selectedJpgList.sort()

    output = open(os.path.join(path,str(amountInSelection)+'_selected.pickle'), 'wb')
    pickle.dump(selectedJpgList, output)

    #create folder to copy the files in
    newFolderName = os.path.join(path,'jpgs_'+str(amountInSelection)+'_selected')

    #create the jpgs folder
    try:
        os.mkdir(newFolderName)
    except:
        print('folder already exists')
        shutil.rmtree(newFolderName)
        os.mkdir(newFolderName)

    newTxtFolderName = os.path.join(path,'txts_'+str(amountInSelection)+'_selected')

    #create the txts folder
    try:
        os.mkdir(newTxtFolderName)
    except:
        print('folder already exists')
        shutil.rmtree(newTxtFolderName)
        os.mkdir(newTxtFolderName)
    
    #now copy the selected files from the jpgs folder to the newly created folder
    count = 1
    for selectedJpg in selectedJpgList:
        orJpgPath = os.path.join(path,'jpgs',selectedJpg)
        while True:
            outJpgPath = os.path.join(path,'jpgs_'+str(amountInSelection)+'_selected',selectedJpg.replace('.jpg',('-'+str(count)+'.jpg')))
            if os.path.exists(outJpgPath) == False:
                shutil.copy(orJpgPath,outJpgPath)
                shutil.copy( (orJpgPath.replace('/jpgs/','/txts/')).replace('.jpg', '.txt'),(outJpgPath.replace('/jpgs','/txts')).replace('.jpg', '.txt') )
                count = 1
                break
            count = count + 1

