import os
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras import layers, losses
import numpy as np
from clustimage import Clustimage
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt
#plt.style.use('ggplot')
plt.style.use('seaborn')

path = '/home/jean-pierre/ownCloud/phd/code_code_code_code_code/1MAIN_processing/KMEANS/allWoods200_normalized_centered/'

nameBaseFile = os.path.join(path,'data_in_array_greyscale_allWoods200_normalized_centered_with_cluster_data.npy')
nameBaseFileClusters = os.path.join(path,'data_in_array_greyscale_allWoods200_normalized_centered_with_cluster_clusters.npy')

X_train = np.load(nameBaseFile)
labels = np.load(nameBaseFileClusters)

print(X_train)
print(labels)

class MyData:
    def __init__(self, data, labels):
        self.data = data
        self.labels_ = labels

my_variable = MyData(X_train, labels)

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

#encoded_imgs = autoencoder.encoder(X_train).numpy()
encoded_imgs = autoencoder.encoder(my_variable.data).numpy()

my_variable = MyData(encoded_imgs, labels)

tfs_embedded = TSNE(n_components=2, perplexity=40, verbose=2).fit_transform(my_variable.data)

# Get unique labels and corresponding colors
unique_labels = np.unique(my_variable.labels_)
label_colors = plt.cm.rainbow(np.linspace(0, 1, len(unique_labels)))

# Scatter plot the transformed data with label colors
for label, color in zip(unique_labels, label_colors):
    mask = (my_variable.labels_ == label)
    plt.scatter(tfs_embedded[mask, 0], tfs_embedded[mask, 1], marker = "x", color=color, label=str(label))#, cmap='tab20')

plt.xticks(size = 30)
plt.yticks(size = 30)

# Add legend showing the label-color mapping
plt.legend(title='Labels', fontsize=30)
plt.title("T-Distributed Stochastic Neighbor Embedding Visualisation", fontsize=50)
plt.show()
#plt.savefig('/home/jean-pierre/Pictures/test.svg')