import os
import cv2
import shutil
import sys

#define a version name for the data trimming attempt, thats useful for finetuning the algorithm
version = 'trimmedV2'

threshold1 = 0.02 #this is the x location variable, 1 is the complete width of the image, 0 is 0
threshold2 = 0.02 #this is the y location variable, 1 is the complete hiegth of the image, 0 is 0
threshold3 = 0.15 #this is the bounding box width variable, 1 is the complete width of the image, 0 is 0
threshold4 = 0.15 #this is the bounding box height variable, 1 is the complete width of the image, 0 is 0

#define a version name for the data trimming attempt, thats useful for finetuning the algorithm
version = 'trimmedV1'

threshold1 = 0.01 #this is the x location variable, 1 is the complete width of the image, 0 is 0
threshold2 = 0.01 #this is the y location variable, 1 is the complete hiegth of the image, 0 is 0
threshold3 = 0.075 #this is the bounding box width variable, 1 is the complete width of the image, 0 is 0
threshold4 = 0.075 #this is the bounding box height variable, 1 is the complete width of the image, 0 is 0

#define a version name for the data trimming attempt, thats useful for finetuning the algorithm
version = 'trimmedV3'

threshold1 = 0.04 #this is the x location variable, 1 is the complete width of the image, 0 is 0
threshold2 = 0.04 #this is the y location variable, 1 is the complete hiegth of the image, 0 is 0
threshold3 = 0.3 #this is the bounding box width variable, 1 is the complete width of the image, 0 is 0
threshold4 = 0.3 #this is the bounding box height variable, 1 is the complete width of the image, 0 is 0

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

label='singlewood'

#create empty variable to store the paths to the data in
jpgs = []
txts = []

#loop trough all the datasets to be trimmed
for path in paths:
	print('path is '+path)
	jpgsFolder = os.path.join(path+'/jpgs')
	txtsFolder = os.path.join(path+'/txts')
	print('jpgs folder  = '+jpgsFolder)
	print('txts folder  = '+txtsFolder)
	#create new folder for the trimmed data to be placed
	##define the folders
	NONremovedjpgsFolder = os.path.join(path+'/jpgs_'+version+'_not_removed')
	NONremovedtxtsFolder = os.path.join(path+'/txts_'+version+'_not_removed')
	removedjpgsFolder = os.path.join(path+'/jpgs_'+version+'_removed')
	removedtxtsFolder = os.path.join(path+'/txts_'+version+'_removed')
	print('creating '+removedjpgsFolder)
	##create the jpgs_removed folder
	try:
		os.mkdir(removedjpgsFolder)
	except:
		print('jpgs_removed folder already exists')
		shutil.rmtree(removedjpgsFolder)
		os.mkdir(removedjpgsFolder)
	print('creating '+removedtxtsFolder)
	##create the txts_removed folder
	try:
		os.mkdir(removedtxtsFolder)
	except:
		print('txts_removed folder already exists')
		shutil.rmtree(removedtxtsFolder)
		os.mkdir(removedtxtsFolder)
	##create the jpgs_not_removed folder
	try:
		os.mkdir(NONremovedjpgsFolder)
	except:
		print('jpgs_not_removed folder already exists')
		shutil.rmtree(NONremovedjpgsFolder)
		os.mkdir(NONremovedjpgsFolder)
	print('creating '+removedtxtsFolder)
	##create the txts_not_removed folder
	try:
		os.mkdir(NONremovedtxtsFolder)
	except:
		print('txts_not_removed folder already exists')
		shutil.rmtree(NONremovedtxtsFolder)
		os.mkdir(NONremovedtxtsFolder)

	#go through all the files in the jpgs folder
	for jpg in os.listdir(jpgsFolder):
		jpg_splitted = jpg.split('.')
		#print(jpg)
		if(jpg_splitted[-1]=="jpg"):
			image_name=jpg_splitted[-2]
			image_ext="."+jpg_splitted[-1]
			image_ext_txt=".txt"
		else:
			continue

		#create jpg and txt file names and paths
		jpgFileName = image_name+image_ext
		txtFileName = image_name+image_ext_txt

		jpgFilePath = os.path.join(jpgsFolder,jpgFileName)
		txtFilePath = os.path.join(txtsFolder,txtFileName)

		#fill the jpgs and txts variables
		jpgs.append(jpgFilePath)
		txts.append(txtFilePath)

#sort both variables to get a correct timeseries
jpgs_sorted = sorted(jpgs)
txts_sorted = sorted(txts)
#print(jpgs_sorted)
#print(len(jpgs_sorted))
#check whether both lists are of the same size
if len(jpgs_sorted) != len(txts_sorted):
	print('jpgs length and txts length are not of the same size!, aborting')
	sys.exit()

#create variable of yolo coordinates that will be remembered temporarily
remembered_yolo_coords = []

#create empty variable for the jpgs and txts that can be removed
jpgs_to_remove = []
txts_to_remove = []

jpgs_to_not_remove = []
txts_to_not_remove = []

count = 1

#loop through all the sorted files
for i in range(len(jpgs_sorted)):
	#create empty variable to store the coordinates in
	yolo_coords = []

	#define the image we are working with in this iteration
	jpg = jpgs_sorted[i]
	
	txt = txts_sorted[i]

	#read txt file with the information regarding the labels
	with open(txt) as f:
		lines = f.readlines()
	#each line in the txt file contains a label, so here we are going through the lines to store all coordinates in our variable
	for line in lines:
		coordinates = line.split(' ')
		yolo_coords.append([float(coordinates[1]),float(coordinates[2]),float(coordinates[3]),float(coordinates[4].split('\n')[0]),label])

	#sort the labels in the txt file based on location
	yolo_coords.sort()

	#create variable to indicate whether the label is in approximately the same location as it was (stuck)
	same = False

	#if the amount if labels in the last file is the same as in the current file, we are going to inspect
	if len(remembered_yolo_coords) == len(yolo_coords):
		same = True
		#loop through the coordinates, and check wether all of the labels are the same as in the previous txt file
		for i in range(len(yolo_coords)):
			
			#if same == False:
			#	break

			#if the label in the current txt file is within the same threshold as the same label in the previous txts file, we will continue
			if abs( (yolo_coords[i][0] - remembered_yolo_coords[i][0]) ) <= threshold1 and abs( (yolo_coords[i][1] - remembered_yolo_coords[i][1]) ) <= threshold2 and abs( ( (yolo_coords[i][2] - remembered_yolo_coords[i][2]) ) / float(yolo_coords[i][2]) ) <= threshold3 and abs( ( (yolo_coords[i][3] - remembered_yolo_coords[i][3]) ) / float(yolo_coords[i][3]) ) <= threshold4:
				same = True
			else:
				same = False
				break

	#if all labels in the txt file are the same as the lavels in the previous txt file, we mark this image as 'to be removed'
	if same == True:
		count = count + 1
		if count > 2:
			#print(jpg)
			jpgs_to_remove.append(jpg)
			txts_to_remove.append(txt)
		else:
			#print(jpg)
			jpgs_to_not_remove.append(jpg)
			txts_to_not_remove.append(txt)

	#only if all the labels are NOT the same as in the previous image, we remember the new coordinates
	else:
		#print(jpg)
		jpgs_to_not_remove.append(jpg)
		txts_to_not_remove.append(txt)
		remembered_yolo_coords = yolo_coords
		count = 1

print(count)
print('length jpgs to remove = '+str(len(jpgs_to_remove)))
print(len(jpgs_to_remove))
print(len(jpgs_to_not_remove))

#copy the jpgs and txts that need to be removed into the _removed folder and the ones that need to stay in the _not_removed folder
for i in range(len(jpgs_to_remove)):
	shutil.copy(jpgs_to_remove[i],jpgs_to_remove[i].replace('/jpgs/','/jpgs_'+version+'_removed/'))
	shutil.copy(txts_to_remove[i],txts_to_remove[i].replace('/txts/','/txts_'+version+'_removed/'))
for i in range(len(jpgs_to_not_remove)):
	shutil.copy(jpgs_to_not_remove[i],jpgs_to_not_remove[i].replace('/jpgs/','/jpgs_'+version+'_not_removed/'))
	shutil.copy(txts_to_not_remove[i],txts_to_not_remove[i].replace('/txts/','/txts_'+version+'_not_removed/'))
