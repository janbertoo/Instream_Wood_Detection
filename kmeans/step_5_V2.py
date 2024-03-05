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

dataName = '2-4-6-8'
dataClusters = [2,4,6,8]

path = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/KMEANS/allWoods200_normalized_centered/'

#load the downsampled dataset
Clus_dataSet = np.load(path+'dataset_after_dim_reduction.npy')
print(len(Clus_dataSet))
print(len(Clus_dataSet[0]))

nameBaseFile = path+'data_in_array_greyscale_allWoods200_normalized_centered.npy'


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


#load the file that contains that names of all the pictures
pictureNamesBaseFile = path+'data_in_array_greyscale_allWoods200_normalized_centered_names.npy'
pictureNames = np.load(pictureNamesBaseFile)


savepath = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/KMEANS/step_5/'


#initiate figure
fig, ax = plt.subplots(2, 2, figsize=(15,8))
#LOOP LOOP LOOP LOOP through amount of clusters
count = 0
for n in dataClusters:    
    #define amount of clusters
    number_of_clusters = n
    print('starting with '+str(number_of_clusters)+' clusters')
    #do the KMeans analysis
    k_means = KMeans(init = 'k-means++', n_clusters = number_of_clusters, n_init = 35)
    #q, mod = divmod(n, 2)
    #k_means.fit(Clus_dataSet)
    if count == 0:
        q, mod = (1, 0)
    if count == 1:
        q, mod = (1, 1)
    if count == 2:
        q, mod = (2, 0)
    if count == 3:
        q, mod = (2, 1)
    count = count + 1

    visualizer = SilhouetteVisualizer(k_means, colors='yellowbrick', ax=ax[q-1][mod])
    visualizer.fit(Clus_dataSet)

    #create a list of labels
    k_means_labels = visualizer.labels_
    #create a list of individual silhouette scores per cluster
    sample_silhouette_values = sklearn.metrics.silhouette_samples(Clus_dataSet, k_means_labels)

    means_lst = []
    for label in range(number_of_clusters):
        means_lst.append(sample_silhouette_values[k_means_labels == label].mean())
    
    #collect the silhouette score of the total KMeans analysis
    score = silhouette_score(Clus_dataSet, k_means.labels_, metric='euclidean')
    print("list of labels are: " + str(np.unique(k_means_labels)))

    #save the list of individual silhouette scores per cluster
    np.save(savepath+'silhouette_scores_per_cluster_clus_nums_'+str(number_of_clusters)+'silhouette_'+str(score)+'.npy', means_lst)
    print('mean_lst:')
    print(means_lst)

    plt.xlabel('silhouette score')
    plt.ylabel('images per cluster')


ax[0, 0].set_title(str(dataClusters[0])+' clusters')
ax[0, 1].set_title(str(dataClusters[1])+' clusters')
ax[1, 0].set_title(str(dataClusters[2])+' clusters')
ax[1, 1].set_title(str(dataClusters[3])+' clusters')
fig.suptitle('Visualization of Silhouette Scores per Cluster for '+str(dataClusters[0])+', '+str(dataClusters[1])+', '+str(dataClusters[2])+' and '+str(dataClusters[3])+' Clusters', fontsize=16)
plt.savefig(savepath+'silhouetteVIS'+dataName+'.png')