import os
import sklearn
import keras
from keras.datasets import fashion_mnist 
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from yellowbrick.cluster import SilhouetteVisualizer
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import random

import tensorflow as tf
from tensorflow.keras import layers, losses
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Model

path = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/1MAIN_processing/KMEANS/allWoods200_normalized_centered_autoencoded/'

#load the downsampled dataset
Clus_dataSet = np.load(os.path.join(path,'dataset_after_dim_reduction.npy'))
print(len(Clus_dataSet))
print(len(Clus_dataSet[0]))

nameBaseFile = os.path.join(path,'data_in_array_greyscale_allWoods200_normalized_centered.npy')

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


latent_dim = 64 

class Autoencoder(Model):
  def __init__(self, latent_dim):
    super(Autoencoder, self).__init__()
    self.latent_dim = latent_dim   
    self.encoder = tf.keras.Sequential([
      layers.Flatten(),
      layers.Dense(latent_dim, activation='relu'),
    ])
    self.decoder = tf.keras.Sequential([
      layers.Dense(784, activation='sigmoid'),
      layers.Reshape((28, 28))
    ])

  def call(self, x):
    encoded = self.encoder(x)
    decoded = self.decoder(encoded)
    return decoded

autoencoder = Autoencoder(latent_dim)

encoded_imgs = autoencoder.encoder(X_train).numpy()

print(encoded_imgs.shape)
print(encoded_imgs[0])

#encoded_imgs = encoded_imgs / 255

#load the file that contains that names of all the pictures
pictureNamesBaseFile = os.path.join(path,'data_in_array_greyscale_allWoods200_normalized_centered_names.npy')
pictureNames = np.load(pictureNamesBaseFile)

#LOOP LOOP LOOP LOOP through amount of clusters
for n in range(2,26):
    #define amount of clusters
    number_of_clusters = n
    print('starting with '+str(number_of_clusters)+' clusters')
    #do the KMeans analysis
    k_means = KMeans(init = 'k-means++', n_clusters = number_of_clusters, n_init = 35)
    k_means.fit(encoded_imgs)

    #collect the label for each picture in a variable
    k_means_labels = k_means.labels_

    #create a list of individual silhouette scores per cluster
    sample_silhouette_values = sklearn.metrics.silhouette_samples(encoded_imgs, k_means_labels)

    means_lst = []
    for label in range(number_of_clusters):
        means_lst.append(sample_silhouette_values[k_means_labels == label].mean())
    
    #collect the silhouette score of the total KMeans analysis
    score = silhouette_score(encoded_imgs, k_means.labels_, metric='euclidean')
    print("list of labels are: " + str(np.unique(k_means_labels)))

    #save the list of individual silhouette scores per cluster
    np.save(path+'silhouette_scores_per_cluster_clus_nums_'+str(number_of_clusters)+'silhouette_'+str(score)+'.npy', means_lst)
    
    #create a variable to store the picture names in per cluster
    pictureNamesAndClusters = []

    #number_of_labels = len(np.unique(k_means_labels)) 

    #loop through all the labels and assign a label to every picture in the dataset
    for i in range(len(encoded_imgs)):
        pictureNamesAndClusters.append((pictureNames[i],k_means_labels[i]))
    
    #print(pictureNamesAndClusters)
    #create numpy files of all pictures names with their respective clusters number and total silhouette score
    np.save(path+'pictureNamesAndClusters_clus_nums_'+str(number_of_clusters)+'silhouette_'+str(score)+'.npy', pictureNamesAndClusters)

    #CREATE 100 EXAMPLE IMAGES OF ALL THE CLUSTERS
    #2D matrix  for an array of indexes of the given label
    cluster_index= [[] for i in range(number_of_clusters)]
    for i, label in enumerate(k_means_labels,0):
        for n in range(number_of_clusters):
            if label == n:
                cluster_index[n].append(i)
            else:
                continue
    
    if not os.path.exists(path+'images_'+str(number_of_clusters)+'_clusters'):
        os.makedirs(path+'images_'+str(number_of_clusters)+'_clusters')

    for m in range(number_of_clusters):
    #Visualisation for clusters = clust
        plt.figure(figsize=(20,20));
        #clust = m #enter label number to visualise
        #print(len(cluster_index[m]))
        num = 100 #num of data to visualize from the cluster
        #randomizer = 500

        if len(cluster_index[m]) < num:
            num == len(cluster_index[m])
            #randomizer = 0
        sampleList = random.sample(range(len(cluster_index[m])), num)
        for i in range(1,num): 
            plt.subplot(10, 10, i); #(Number of rows, Number of column per row, item number)
            plt.imshow(X[cluster_index[m][sampleList[i]]].reshape(X_train.shape[1], X_train.shape[2]), cmap = plt.cm.binary);

        plt.savefig(path+'images_'+str(number_of_clusters)+'_clusters/clustnumb'+str(number_of_clusters)+'cluster'+str(m+1)+'examples.png')
    
    plt.clf()