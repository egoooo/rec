import numpy as np # 快速操作结构数组的工具

import pandas as pd # 数据分析处理工具

import matplotlib.pyplot as plt # 画图工具

from sklearn import datasets # 机器学习库
from sklearn.mixture import GaussianMixture

scikit_iris=datasets.load_iris()
print(scikit_iris)
iris=pd.DataFrame(data=np.c_[scikit_iris['data'],scikit_iris['target']],columns=np.append(scikit_iris.feature_names, ['y']))
print(iris)
X = iris[scikit_iris.feature_names]
print(X)

# label

y = iris['y']

# 第一步，选择model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
# 第二步，fit X、y
knn.fit(X, y)
#第三步，predict新数据
p=knn.predict([[3, 2, 2, 5],[1,2,3,4],[2,2,2,2]])
print(p)


gmm = GaussianMixture(n_components=4).fit(X)

labels = gmm.predict(X)
for i in range(4):
    print(i)
    members = labels== i
    print(labels)

    print(members)

