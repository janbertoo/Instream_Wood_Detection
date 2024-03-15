import os
import cv2
import albumentations as A
from tqdm import tqdm
import shutil
from multiprocessing import Pool
import random

folderToAugmentJpgs = 'jpgs'
folderToAugmentTxts = 'txts'
augmentationExtension = 'only_mirrored_random'


#define the transformations that we want to do
transform = A.Compose([ A.HorizontalFlip(p=0.5) ], bbox_params=A.BboxParams(format='yolo'))

label='singlewood'

folderAfterAugmentationJpgs = folderToAugmentJpgs+'_'+augmentationExtension
folderAfterAugmentationTxts = folderToAugmentTxts+'_'+augmentationExtension

coresAmount = os.cpu_count()
#coresAmount = 1

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

#create new txt files from bboxes (formatted: [(xcoor,ycoor,xwidth,yheight,'label'),(xcoor,ycoor,xwidth,yheight,'label'),(xcoor,ycoor,xwidth,yheight,'label')])
def saveNewYoloBboxes(newTxtFilename, newBboxesYolo):
	#create text file
	newTxtFile = open(newTxtFilename,"w")
	
	#Loop through new bboxes
	for newbbox in newBboxesYolo:
		#write 6 digit floats per coordinate
		newTxtFile.write("0 "+str("%.6f" % newbbox[0])+" "+str("%.6f" % newbbox[1])+" "+str("%.6f" % newbbox[2])+" "+str("%.6f" % newbbox[3])+"\n")
	newTxtFile.close()



#loop through all paths
#for path in paths:
def augmentAllImagesInPath(path):
    #create the directories to store the files in
    try:
        os.mkdir(os.path.join(path,folderAfterAugmentationJpgs))
    except:
        shutil.rmtree(os.path.join(path,folderAfterAugmentationJpgs))
        os.mkdir(os.path.join(path,folderAfterAugmentationJpgs))
    try:
        os.mkdir(os.path.join(path,folderAfterAugmentationTxts))
    except:
        shutil.rmtree(os.path.join(path,folderAfterAugmentationTxts))
        os.mkdir(os.path.join(path,folderAfterAugmentationTxts))
    #loop through all files in the 'jpgs' folder
    print(os.path.join(path,folderToAugmentJpgs))
    for jpg in os.listdir(os.path.join(path,folderToAugmentJpgs)):
        #print(jpg)
        #create empty variable to store the labels in
        yolo_coors = []
        #determine the jpg and text files
        if jpg[-4:] == '.jpg':
            #print('jpg')
            jpgFileName = jpg
            txtFileName = jpg.replace('.jpg', '.txt')

            jpgFileNameAugmented = jpgFileName.replace('.jpg', '_'+augmentationExtension+'.jpg')
            txtFileNameAugmented = txtFileName.replace('.txt', '_'+augmentationExtension+'.txt')

            jpgFilePath = os.path.join(path,folderToAugmentJpgs,jpgFileName)
            txtFilePath = os.path.join(path,folderToAugmentTxts,txtFileName)

            augmentedJpgPath = os.path.join(path,folderAfterAugmentationJpgs,jpgFileNameAugmented)
            augmentedTxtPath = os.path.join(path,folderAfterAugmentationTxts,txtFileNameAugmented)
            
            #read txt file
            #print(txtFilePath)
            with open(txtFilePath) as f:
                lines = f.readlines()
            for line in lines:
                coordinates = line.split(' ')
                yolo_coors.append([float(coordinates[1]),float(coordinates[2]),float(coordinates[3]),float(coordinates[4].split('\n')[0]),label])
            #print(yolo_coors)
            #read image
            image = cv2.imread(jpgFilePath)


            #print(' ')
            #print('Something went wrong with image '+jpgFileName+'     SKIPPING #################################################')
            #transformed_image_2 = image[:, ::-1, :]
            choices = [True,False]
            pick = random.choice(choices)
            if pick == True:
                #print('mirrored')
                transformed_image_2 = cv2.flip(image,1)
                #print(transformed_image_2)
                transformed_bboxes_2 = []
                for bb in yolo_coors:
                    transformed_bboxes_2.append((1-bb[0],bb[1],bb[2],bb[3]))
                #print(transformed_bboxes_2)
            else:
                transformed_image_2 = image
                transformed_bboxes_2 = []
                for bb in yolo_coors:
                    transformed_bboxes_2.append((bb[0],bb[1],bb[2],bb[3]))

            cv2.imwrite(augmentedJpgPath,transformed_image_2)
            saveNewYoloBboxes(augmentedTxtPath,transformed_bboxes_2)

            continue

            

            


if __name__ == '__main__':
    with Pool(coresAmount) as p:
        p.map(augmentAllImagesInPath, paths)

