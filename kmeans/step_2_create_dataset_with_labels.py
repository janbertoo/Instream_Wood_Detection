import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

#setting the path to the directory containing the pics
path = '/home/jean-pierre/scratch/allWoods200_normalized_centered'
pathStore = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/1MAIN_processing/KMEANS/allWoods200_normalized_centered'

datasets = [
    ['20201117_rotated__1pi2','20201117_1pi2'],
    ['20201117_rotated__2pi4','20201117_2pi4'],    
    ['20201117_rotated__3SamsungGalaxyA5','20201117_3SG5'],
    ['20201117_rotated__4XiaomiRedmi4X','20201117_4XR4'],
    ['20201119_rotated__1XiaomiRedmi4X','20201119_1XR4'],
    ['20201119_rotated__2pi2','20201119_2pi2'],
    ['20201119_rotated__3pi4','20201119_3pi4'],
    ['20201119_rotated__4SamsungGalaxyA5_sampled','20201119_4SG5'],
	['20201126_rotated__3XiaomiRedmi2_sampled','20201126_3XR2s'],
    ['20201126_rotated__4pi4_c4_sampled','20201126_4pi4c4s'],
	['20201126_rotated__4pi4_c5','20201126_4pi4c5'],
	['20201127_rotated__2pi4','20201127_2pi4'],
	['20201203_rotated__1pi4_sampled','20201203_1pi4s'],
	['20201203_rotated__3pi2','20201203_3pi2'],
	['20201203_rotated__4SamsungGalaxyA5','20201203_4SG5'],
	['unilyon_and_others__20071123_0756_Ain1','others_Ain1'],
	['unilyon_and_others__20071123_0956_Ain2','others_Ain2'],
	['unilyon_and_others__20191125_Allier1','others_Allier1'],
	['unilyon_and_others__20191223_Allier2','others_Allier2'],
	['unilyon_and_others__randomWoodImages','others_random']
]

#appending the pics to the training data list
training_data = []
imageNames = []
clusters = []
for img in os.listdir(path):
	for dataset in datasets:
		if dataset[0] in img:
			cluster = dataset[1]
	
	if img[-4:] == '.jpg':
		pic = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
		#pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
		pic = cv2.resize(pic,(80,80))
		training_data.append([pic])
		#print(img)
		imageNames.append(img)
		clusters.append(cluster)
	else:
		print(img+' is not an image, skipping')
	
	cluster = None

print(training_data)

#converting the list to numpy array and saving it to a file using #numpy.save
np.save(os.path.join(pathStore,'data_in_array_greyscale_allWoods200_normalized_centered_with_cluster_data'),np.array(training_data))
np.save(os.path.join(pathStore,'data_in_array_greyscale_allWoods200_normalized_centered_with_cluster_clusters'),clusters)

