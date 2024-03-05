import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

#setting the path to the directory containing the pics
path = '/home/jean-pierre/scratch/allWoods200_normalized_centered'
pathStore = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/1MAIN_processing/KMEANS/allWoods200_normalized_centered'

datasets = [
    ['20201117_rotated__1pi2',0],
    ['20201117_rotated__2pi4',1],    
    ['20201117_rotated__3SamsungGalaxyA5',2],
    ['20201117_rotated__4XiaomiRedmi4X',3],
    ['20201119_rotated__1XiaomiRedmi4X',4],
    ['20201119_rotated__2pi2',5],
    ['20201119_rotated__3pi4',6],
    ['20201119_rotated__4SamsungGalaxyA5_sampled',7],
	['20201126_rotated__3XiaomiRedmi2_sampled',8],
    ['20201126_rotated__4pi4_c4_sampled',9],
	['20201126_rotated__4pi4_c5',10],
	['20201127_rotated__2pi4',11],
	['20201203_rotated__1pi4_sampled',12],
	['20201203_rotated__3pi2',13],
	['20201203_rotated__4SamsungGalaxyA5',14],
	['unilyon_and_others__20071123_0756_Ain1',15],
	['unilyon_and_others__20071123_0956_Ain2',16],
	['unilyon_and_others__20191125_Allier1',17],
	['unilyon_and_others__20191223_Allier2',18],
	['unilyon_and_others__randomWoodImages',19]
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
#np.save(os.path.join(pathStore,'data_in_array_greyscale_allWoods200_normalized_centered_names'),imageNames)


#print(np.array(training_data))
#print(imageNames)
#loading the saved file once again
#saved = np.load(os.path.join(path,'features_greyscale_allWoods200.npy'))

#plt.imshow(saved[0].reshape(80,80))
#plt.imshow(np.array(training_data[0]).reshape(80,80))