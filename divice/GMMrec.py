import numpy as np
import pandas as pd
from sklearn import cross_validation as cv
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

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

from sklearn.mixture import GaussianMixture

gmm = GaussianMixture(n_components=10).fit(train_data_matrix)

labels = gmm.predict(train_data_matrix)
for i in range(10):
    print(i)
    members = labels == i
    print(labels)

    print(members)