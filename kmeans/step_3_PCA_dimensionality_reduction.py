import os
import sklearn
import keras
from keras.datasets import fashion_mnist 
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from yellowbrick.cluster import SilhouetteVisualizer
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator

nameBaseFile = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/1MAIN_processing/KMEANS/allWoods200_normalized_centered/data_in_array_greyscale_allWoods200_normalized_centered.npy'
storeFileIn = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/1MAIN_processing/KMEANS/allWoods200_normalized_centered/dataset_after_dim_reduction.npy'



X_train = np.load(nameBaseFile)

X_train_concatenated = np.concatenate(X_train)

X_train = []

for image in X_train_concatenated:

	image2 = []
	for number in image:
		image2.append(number)
	image2=np.concatenate(image2)
	X_train.append(image2)

X = np.asarray(X_train)

X_train = X_train_concatenated

print(X.shape)
print(X_train.shape)
print(type(X[0][0]))

Clus_dataSet = StandardScaler().fit_transform(X) #(mean = 0 and variance = 1)

variance = 0.98

pca = PCA(variance)

pca.fit(Clus_dataSet)

print("Number of components before PCA  = " + str(X.shape[1]))
print("Number of components after PCA 0.98 = " + str(pca.n_components_))

Clus_dataSet = pca.transform(Clus_dataSet)
print(Clus_dataSet)

np.save(storeFileIn, Clus_dataSet)
