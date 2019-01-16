#可以正常运行，代码正确

from math import *

import pandas as pd
movies = pd.read_csv('C:/Users/Administrator/PycharmProjects/rec/data/movies.csv ')
ratings = pd.read_csv('C:/Users/Administrator/PycharmProjects/rec/data/ratings.csv')##这里注意如果路径的中文件名开头是r，要转义。
data = pd.merge(movies,ratings,on = 'movieId')#通过两数据框之间的movieId连接
data[['userId','rating','movieId','title']].sort_values('userId').to_csv('C:/Users/Administrator/PycharmProjects/rec/data/data.csv',index=False)
print(data.head())
print()
file = open('C:/Users/Administrator/PycharmProjects/rec/data/data.csv', 'r',
            encoding='UTF-8')  # 记得读取文件时加‘r’， encoding='UTF-8'
##读取data.csv中每行中除了名字的数据
data = {}  ##存放每位用户评论的电影和评分
for line in file.readlines()[1:1000]:
    # 注意这里不是readline()
    line = line.strip().split(',')  #userId,rating,movieId,title
    # 如果字典中没有某位用户，则使用用户ID来创建这位用户
    if not line[0] in data.keys():
        data[line[0]] = {line[3]: line[1]}
    # 否则直接添加以该用户ID为key字典中
    else:
        data[line[0]][line[3]] = line[1]

print(data)


def Euclidean(user1, user2):
    # 取出两位用户评论过的电影和评分
    user1_data = data[user1]
    user2_data = data[user2]
    distance = 0
    # 找到两位用户都评论过的电影，并计算欧式距离
    for key in user1_data.keys():
        if key in user2_data.keys():
            # 注意，distance越大表示两者越相似
            distance += pow(float(user1_data[key]) - float(user2_data[key]), 2)

    return 1 / (1 + sqrt(distance))  # 这里返回值越小，相似度越大


# 计算某个用户与其他用户的相似度
def top10_simliar(userID):
    res = []
    for userid in data.keys():
        # 排除与自己计算相似度,用户之间相似度结果：0表示两位的影评几乎一样，1表示没有共同的影评
        if not userid == userID:
            simliar = Euclidean(userID, userid)
            res.append((userid, simliar))
    res.sort(key=lambda val: val[1])
    return res[:10]


RES = top10_simliar('1')
print(RES)


def recommend(user):
    # 相似度最高的用户
    top_sim_user = top10_simliar(user)[0][0]
    print("top_sim_user",top_sim_user)
    # 相似度最高的用户的观影记录
    items = data[top_sim_user]
    print("itens",items)
    recommendations = []
    # 筛选出该用户未观看的电影并添加到列表中
    for item in items.keys():
        if item not in data[user].keys():
            recommendations.append((item, items[item]))
    recommendations.sort(key=lambda val: val[1], reverse=True)  # 按照评分排序
    # 返回评分最高的10部电影
    return recommendations[:10]


Recommendations = recommend('1')
print(Recommendations)


