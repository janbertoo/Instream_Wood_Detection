from yellowbrick.cluster import SilhouetteVisualizer
from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()
X = iris.data
print('X')
print(X[0])

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
print('X_train')
print(X_train[0])
print('X_train_concatenated')
print(X_train_concatenated[0])
#X_train = X_train_concatenated


fig, ax = plt.subplots(2, 2, figsize=(15,8))
for i in [2, 3, 4, 5]:
    '''
    Create KMeans instance for different number of clusters
    '''
    km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=100, random_state=42)
    q, mod = divmod(i, 2)
    '''
    Create SilhouetteVisualizer instance with KMeans instance
    Fit the visualizer
    '''
    visualizer = SilhouetteVisualizer(km, colors='yellowbrick', ax=ax[q-1][mod])
    visualizer.fit(X_train)

plt.savefig('/home/jean-pierre/ownCloud/phd/code_code_code_code_code/KMEANS/example.png')