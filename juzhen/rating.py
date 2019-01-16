import numpy as np
import pandas as pd
from sklearn import cross_validation as cv

header = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('C:/Users/Administrator/PycharmProjects/rec/data/u.data', sep='\t', names=header)
# df.sort_values(by='user_id')
print(df)

# 计算唯一用户和电影的数量标准化矩阵
n_users = df.user_id.unique().shape[0]
print(n_users)
n_items = df.item_id.unique().shape[0]
print(n_items)
# 使用scikit-learn库将数据集分割成测试和训练。Cross_validation.train_test_split根据测试样本的比例（test_size）

train_data, test_data = cv.train_test_split(df, test_size=0.2)
print(train_data)

train_data_matrix = np.zeros((n_users, n_items))
for line in train_data.itertuples():
    #print(line)
    train_data_matrix[line[1] - 1, line[2] - 1] = line[3]
    #减1的原因是user_id', 'item_id'，都是从1开始计数的，而矩阵是从0开始计数的。

print('train_data_matrix\n%s'%train_data_matrix)
test_data_matrix = np.zeros((n_users, n_items))
for line in test_data.itertuples():
    test_data_matrix[line[1] - 1, line[2] - 1] = line[3]

# 计算相似度
# 使用sklearn的pairwise_distances函数来计算余弦相似性
from sklearn.metrics.pairwise import pairwise_distances
item_similarity = pairwise_distances(train_data_matrix.T, metric='cosine')
print(item_similarity)
user_similarity=pairwise_distances(train_data_matrix,metric="cosine")
print("user_sim")
print(user_similarity)
print(user_similarity.shape)

# def predict(ratings, similarity, type='user'):
#     # 基于用户相似度矩阵的
#     if type == 'user':
#         mean_user_rating = ratings.mean(axis=1)
#         # You use np.newaxis so that mean_user_rating has same format as ratings
#         ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
#         pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array(
#             [np.abs(similarity).sum(axis=1)]).T
#     # 基于物品相似度矩阵
#     elif type == 'item':
#         pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])#求评价均值
#     return pred
#
#
# # 预测结果
# item_prediction = predict(train_data_matrix, item_similarity, type='item')
# user_prediction = predict(train_data_matrix, user_similarity, type='user')
# print(item_prediction[0:8])
# # print(user_prediction)
#
# # 评估指标，均方根误差
# # 使用sklearn的mean_square_error (MSE)函数，其中，RMSE仅仅是MSE的平方根
# # 只是想要考虑测试数据集中的预测评分，因此，使用prediction[ground_truth.nonzero()]筛选出预测矩阵中的所有其他元素
# from sklearn.metrics import mean_squared_error
# from math import sqrt
#
# def rmse(prediction, ground_truth):
#     prediction = prediction[ground_truth.nonzero()].flatten()#取测试矩阵相同的部分计算RMSE
#     ground_truth = ground_truth[ground_truth.nonzero()].flatten()
#     return sqrt(mean_squared_error(prediction, ground_truth))
#
# # print('User-based CF RMSE: ' + str(rmse(user_prediction, test_data_matrix)))
# print('Item-based CF RMSE: ' + str(rmse(item_prediction, test_data_matrix)))

