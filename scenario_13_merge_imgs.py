import os
import cv2
import numpy as np

#jpgsfolder = '/home/jean-pierre/Desktop/test_merge/labeled_data_all/20201117_rotated/1pi2/labeled_20201117_1pi2_c3/jpgs'

def merge_jpgs_in_folder(jpgsfolder):
	newjpgsfolder = jpgsfolder.replace('/jpgs','/jpgs_merged')
	
	if os.path.exists(newjpgsfolder) == False:
		os.mkdir(newjpgsfolder)

	jpgslist = []
	for file in os.listdir(jpgsfolder):
		if file[-4:] == '.jpg':
			jpgslist.append(os.path.join(jpgsfolder,file))

	jpgslist.sort()
	#print(jpgslist)

	for i in range(1,len(jpgslist)-1):
		im0 = jpgslist[i-1]
		im1 = jpgslist[i]
		im2 = jpgslist[i+1]

		newim1 = im1.replace('/jpgs','/jpgs_merged')
		print('Creating '+newim1)
			
		try:
			

			

			read_im0 = cv2.imread(im0, cv2.IMREAD_GRAYSCALE)
			read_im1 = cv2.imread(im1, cv2.IMREAD_GRAYSCALE)
			read_im2 = cv2.imread(im2, cv2.IMREAD_GRAYSCALE)

			newim_data = np.zeros((len(read_im1),len(read_im1[0]),3), np.uint8)

			for i in range(len(read_im1)):
				for j in range(len(read_im1[0])):
					#for k in range(len(testimCOL[0][0])):
					newim_data[i][j][0] = read_im0[i][j]
					newim_data[i][j][1] = read_im1[i][j]
					newim_data[i][j][2] = read_im2[i][j]

			cv2.imwrite(newim1,newim_data)
		except:
			print(newim1+' DIDNT WORK !!!!!!!!!!!, MAYBE  AN IMAGE WAS CORRUPTED OR SOMETHING ...')

#merge_jpgs_in_folder(jpgsfolder)

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

for jpgsfolder in paths:
	merge_jpgs_in_folder(jpgsfolder)
