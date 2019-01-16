
from gmm import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf
# 导入ratings.csv文件

ratings_df = pd.read_csv('C:/Users/Administrator/PycharmProjects/rec/data/ratings.csv')
print(ratings_df.tail())

#tail命令用于输入文件中的尾部内容。tail命令默认在屏幕上显示指定文件的末尾5行。

#导入movies.csv文件

movies_df = pd.read_csv('C:/Users/Administrator/PycharmProjects/rec/data/movies.csv')
print(movies_df.tail())


# 将movies_df中的movieId替换为行号

movies_df['movieRow'] = movies_df.index
#生成一列‘movieRow’，等于索引值index

print(movies_df.tail())

#筛选movies_df中的特征

movies_df = movies_df[['movieRow','movieId','title']]
#筛选三列出来
movies_df.to_csv('C:/Users/Administrator/PycharmProjects/rec/data/moviesProcessed.csv', index=False, header=True, encoding='utf-8')
#生成一个新的文件moviesProcessed.csv
print(movies_df.tail())


#根据movieId，合并rating_df和movie_df

ratings_df = pd.merge(ratings_df, movies_df, on='movieId')
# ratings_df.head()
print(ratings_df.head())

# 筛选ratings_df中的特征

ratings_df = ratings_df[['userId','movieRow','rating']]
#筛选出三列
ratings_df.to_csv('C:/Users/Administrator/PycharmProjects/rec/data/ratingsProcessed.csv', index=False, header=True, encoding='utf-8')
#导出一个新的文件ratingsProcessed.csv

print(ratings_df.head())

#创建电影评分矩阵rating和评分纪录矩阵record

userNo = ratings_df['userId'].max() + 1
#userNo的最大值
movieNo = ratings_df['movieRow'].max() + 1
print(userNo)
print(movieNo)
#movieNo的最大值
rating = np.zeros((movieNo,userNo))
#创建一个值都是0的数据
flag = 0
ratings_df_length = np.shape(ratings_df)[0]
#查看矩阵ratings_df的第一维度是多少
for index,row in ratings_df.iterrows():
    #interrows（），对表格ratings_df进行遍历
    rating[int(row['movieRow']),int(row['userId'])] = row['rating']
    #将ratings_df表里的'movieRow'和'userId'列，填上row的‘评分’
    flag += 1
# record = rating > 0
record = rating
record
record = np.array(record, dtype = float)
#更改数据类型，0表示用户没有对电影评分，1表示用户已经对电影评分


# print(record)
#
# for i in record[1]:
#     print(i)

# 设置调试模式
DEBUG = True

# 载入数据
# Y = np.loadtxt("gmm.data")
matY = np.matrix(record, copy=True)

# 模型个数，即聚类的类别个数
K = 4

# 计算 GMM 模型参数
mu, cov, alpha = GMM_EM(matY, K, 100)

# 根据 GMM 模型，对样本数据进行聚类，一个模型对应一个类别
N = record.shape[0]
# 求当前模型参数下，各模型对样本的响应度矩阵
gamma = getExpectation(matY, mu, cov, alpha)
# 对每个样本，求响应度最大的模型下标，作为其类别标识
category = gamma.argmax(axis=1).flatten().tolist()[0]
# 将每个样本放入对应类别的列表中
class1 = np.array([record[i] for i in range(N) if category[i] == 0])
class2 = np.array([record[i] for i in range(N) if category[i] == 1])
class3 = np.array([record[i] for i in range(N) if category[i] == 2])
class4 = np.array([record[j] for j in range(N) if category[j] == 3])

# # 绘制聚类结果
# plt.plot(class1[:, 0], class1[:, 1], 'rs', label="user-cluster1")
# plt.plot(class2[:, 0], class2[:, 1], 'bo', label="user-cluster2")
# plt.plot(class3[:, 0], class3[:, 1], 'gx', label="user-cluster3")
# plt.plot(class4[:, 0], class4[:, 1], 'yd', label="user-cluster4")
# plt.legend(loc="best")
# plt.title("GMM Clustering By EM Algorithm")
# plt.show()

for i in class1:
    print("dddd")
    print(i)
