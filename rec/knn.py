from surprise import KNNWithMeans, evaluate, Dataset

# 默认载入movielens数据集
data = Dataset.load_builtin('ml-100k')
print(data)
# k折交叉验证(k=3)
data.split(n_folds=3)

sim_options = {'name': 'pearson',
               'shrinkage': 0 , # no shrinkage
               'user_based': False
               }
algo = KNNWithMeans(k=60,sim_options=sim_options)
perf = evaluate(algo, data=data, measures=['RMSE', 'MAE'])
print(perf)
