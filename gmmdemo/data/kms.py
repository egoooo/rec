# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 从磁盘读取城市经纬度数据
X = []
# f = open('height_weight.txt',encoding='utf-8')
# for v in f:
#     X.append([int(v.split()[0]), int(v.split()[1])])
f = open('julei.txt',encoding='utf-8')
for v in f:
    X.append([int(v.split(',')[0]), int(v.split(',')[1])])
# 转换成numpy array
X = np.array(X)
# 类簇的数量
n_clusters = 3
# 现在把数据和对应的分类书放入聚类函数中进行聚类
cls = KMeans(n_clusters).fit(X)
# X中每项所属分类的一个列表
cls.labels_
# 画图
markers = ['^', 'x', 'o', '*', '+']
colors=['k','r','g','b']
for i in range(n_clusters):
    print(i)
    members = cls.labels_ == i
    print(cls.labels_)
    print(members)
    print(X[members, 0])
    plt.scatter(X[members, 0], X[members, 1], s=60, marker=markers[i], c=colors[i], alpha=0.5)
plt.title(' ')
plt.show()