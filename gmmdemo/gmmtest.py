
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import numpy as np
import  pandas as pd

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

# x = np.loadtxt("gmm.data")
x=record
gmmModel = GaussianMixture(n_components=5, covariance_type='diag', random_state=0)
gmmModel.fit(x)
labels = gmmModel.predict(x)
print(labels)
for i in range(1,len(labels)):
    if labels[i] == 0:
        plt.scatter(x[i, 0], x[i, 1], s=15, c='red')
    elif labels[i] == 1:
        plt.scatter(x[i, 0], x[i, 1], s=15, c='blue')
    elif labels[i] == 2:
        plt.scatter(x[i, 0], x[i, 1], s=15, c='green')
    elif labels[i] == 3:
        plt.scatter(x[i, 0], x[i, 1], s=15, c='cyan')
    elif labels[i] == 4:
        plt.scatter(x[i, 0], x[i, 1], s=15, c='magenta')

print("fff", gmmModel.means_)
print("kkk", gmmModel.covariances_)
plt.title('Gaussian Mixture Model')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


