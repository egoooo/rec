
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

#产生实验数据
from sklearn.datasets.samples_generator import make_blobs
X, y_true = make_blobs(n_samples=100, centers=4,
                       cluster_std=0.60, random_state=0)
print(X)
X = X[:, ::-1] #交换列是为了方便画图
print(X)

from sklearn.mixture import  GaussianMixture

gmm = GaussianMixture(n_components=4).fit(X)

labels = gmm.predict(X)
for i in range(4):
    print(i)
    members = labels== i
    print(labels)

    print(members)

plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis');
plt.show()
