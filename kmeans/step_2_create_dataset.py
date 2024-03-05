import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

#setting the path to the directory containing the pics
path = '/home/jean-pierre/scratch/allWoods200_normalized_centered'
pathStore = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/1MAIN_processing/KMEANS/allWoods200_normalized_centered'

#appending the pics to the training data list
training_data = []
imageNames = []
for img in os.listdir(path):
	if img[-4:] == '.jpg':
		pic = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
		#pic = cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
		pic = cv2.resize(pic,(80,80))
		training_data.append([pic])
		#print(img)
		imageNames.append(img)
	else:
		print(img+' is not an image, skipping')

#converting the list to numpy array and saving it to a file using #numpy.save
np.save(os.path.join(pathStore,'data_in_array_greyscale_allWoods200_normalized_centered'),np.array(training_data))
np.save(os.path.join(pathStore,'data_in_array_greyscale_allWoods200_normalized_centered_names'),imageNames)


#print(np.array(training_data))
#print(imageNames)
#loading the saved file once again
#saved = np.load(os.path.join(path,'features_greyscale_allWoods200.npy'))

#plt.imshow(saved[0].reshape(80,80))
#plt.imshow(np.array(training_data[0]).reshape(80,80))