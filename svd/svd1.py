# -*- coding: utf-8 -*-
'''
Created on 2017年10月16日
@author: Administrator
'''
import numpy as np
import pandas as pd
from math import exp
import time
import math


class LFM:

    def __init__(self, lclass, iters, alpha, lamda, topk, ratio, traindata):
        self.lclass = lclass  # 隐类数量，对性能有影响
        self.iters = iters  # 迭代次数，收敛的最佳迭代次数未知
        self.alpha = alpha  # 梯度下降步长
        self.lamda = lamda  # 正则化参数
        self.topk = topk  # 推荐top k项
        self.ratio = ratio  # 正负样例比率，对性能最大影响
        self.traindata = traindata

    # 初始化开始.....
    def getUserPositiveItem(self, userid):  # 生成正样例
        traindata = self.traindata
        series = traindata[traindata['userid'] == userid]['itemid']
        positiveItemList = list(series.values)
        return positiveItemList

    def getUserNegativeItem(self, userid):  # 生成负样例
        traindata = self.traindata
        itemLen = self.itemLen
        ratio = self.ratio
        userItemlist = list(set(traindata[traindata['userid'] == userid]['itemid']))  # 用户评分过的物品
        negativeItemList = []
        count = ratio * len(userItemlist)  # 生成负样例的数量
        for key, value in itemLen.iteritems():  # itemLen.index
            if count == 0:
                break
            if key in userItemlist:
                continue
            negativeItemList.append(key)
            count = count - 1
        return negativeItemList

    def initUserItem(self, userid):
        # traindata=self.traindata
        positiveItem = self.getUserPositiveItem(userid)
        negativeItem = self.getUserNegativeItem(userid)
        itemDict = {}
        for item in positiveItem: itemDict[item] = 1
        for item in negativeItem: itemDict[item] = 0
        return itemDict

    def initModel(self):
        traindata = self.traindata
        lcalss = self.lclass  # 隐类数量
        userID = list(set(traindata['userid'].values))
        self.userID = userID
        itemID = list(set(traindata['itemid'].values))
        self.itemID = itemID
        itemCount = [len(traindata[traindata['itemid'] == item]['userid']) for item in itemID]
        self.itemLen = pd.Series(itemCount, index=itemID).sort_values(ascending=False)  # 统计每个物品对应的热门度（次数并降序
        # 初始化p、q矩阵
        arrayp = np.random.rand(len(userID), lcalss)  # 构造p矩阵，[0,1]内随机值
        arrayq = np.random.rand(lcalss, len(itemID))  # 构造q矩阵，[0,1]内随机值
        p = pd.DataFrame(arrayp, columns=range(0, lcalss), index=userID)
        q = pd.DataFrame(arrayq, columns=itemID, index=range(0, lcalss))
        # 生成负样例
        userItem = []
        for userid in userID:
            itemDict = self.initUserItem(userid)
            userItem.append({userid: itemDict})
        return p, q, userItem

    # 初始化结束.....
    def sigmod(self, x):
        # 单位阶跃函数,将兴趣度限定在[0,1]范围内
        y = 1.0 / (1 + exp(-x))
        return y

    def lfmPredict(self, p, q, userID, itemID):
        # 利用参数p,q预测目标用户对目标物品的兴趣度
        p = np.mat(p.ix[userID].values)
        q = np.mat(q[itemID].values).T
        r = (p * q).sum()
        r = self.sigmod(r)
        return r

    def latenFactorModel(self):
        # traindata=self.traindata
        lclass = self.lclass
        iters = self.iters  # 迭代次数
        alpha = self.alpha  # 梯度下降步长
        lamda = self.lamda  # 正则化参数
        p, q, userItem = self.initModel()
        for step in range(0, iters):
            for user in userItem:
                for userID, samples in user.items():
                    for itemID, rui in samples.items():
                        eui = rui - self.lfmPredict(p, q, userID, itemID)
                        for f in range(0, lclass):
                            # print('step %d user %d class %d' % (step, userID, f))
                            p[f][userID] += alpha * (eui * q[itemID][f] - lamda * p[f][userID])
                            q[itemID][f] += alpha * (eui * p[f][userID] - lamda * q[itemID][f])
            alpha *= 0.9  # 学习速率
        return p, q

    def recommend(self, userid, p, q):
        itemID = self.itemID
        Topk = self.topk
        # traindata=self.traindata
        # userItemlist = list(set(traindata[traindata['userid'] == userid]['itemid']))
        # otherItemList = [item for item in set(traindata['itemid'].values) if item not in userItemlist]
        predictList = [self.lfmPredict(p, q, userid, itemid) for itemid in itemID]
        series = pd.Series(predictList, index=itemID)
        series = series.sort_values(ascending=False)[:Topk]
        return series

    def recallAndPrecision(self, p, q):  # 召回率和准确率
        traindata = self.traindata
        # itemID=self.itemID
        userID = self.userID
        hit = 0
        recall = 0
        precision = 0
        for userid in userID:
            trueItem = traindata[traindata['userid'] == userid]['itemid']
            preitem = self.recommend(userid, p, q)
            preItem = list(preitem.index)
            for item in preItem:
                if item in trueItem:
                    hit += 1
            recall += len(trueItem)
            precision += len(preItem)
        return (hit / (recall * 1.0), hit / (precision * 1.0))

    def coverage(self, p, q):  # 覆盖率
        traindata = self.traindata
        recommend_items = set()
        all_items = set()
        userID = self.userID
        for userid in userID:
            trueItem = traindata[traindata['userid'] == userid]['itemid']
            for item in trueItem:
                all_items.add(item)
            preitem = self.recommend(userid, p, q)
            preItem = list(preitem.index)
            for item in preItem:
                recommend_items.add(item)
        return len(recommend_items) / (len(all_items) * 1.0)

    def popularity(self, p, q):  # 流行度
        # traindata = self.traindata
        itemLen = self.itemLen
        # itemID=self.itemID
        userID = self.userID
        ret = 0
        n = 0
        for userid in userID:
            preitem = self.recommend(userid, p, q)
            preItem = list(preitem.index)
            for item in preItem:
                ret += math.log(1 + itemLen[item])
                n += 1
        return ret / (n * 1.0)


if __name__ == "__main__":
    start = time.clock()
    print(start)

    # 导入数据
    # df_sample = pd.read_csv("D:\\dev\\workspace\\PyRecSys\\demo\\ratings.csv",names=['userid','itemid','ratings'],header=0)userId,rating,movieId,title
    df_sample = pd.read_table("C:\\Users\\Administrator\\PycharmProjects\\rec\\data\\u1.base", names=['userid','itemid','ratings','stamp'], header=0)

    print(df_sample.head())
    traindata = df_sample[['userid', 'itemid']]
    print(traindata)
    for ratio in [1]:   #for ratio in [1, 2, 3, 5, 10, 20]
        for lclass in [10]: #for lclass in [5, 10, 20, 30, 50]:
            lfm = LFM(lclass, 2, 0.02, 0.01, 10, ratio, traindata)  # 隐类参数
            p, q = lfm.latenFactorModel()
            print(q)
            # 推荐
            # preitem = lfm.recommend(1, p, q)
            # print (preitem)
            # 模型评估
            print("%3s%20s%20s%20s%20s%20s" % ('ratio', 'lcalss', "recall", 'precision', 'coverage', 'popularity'))
            recall, precision = lfm.recallAndPrecision(p, q)
            coverage = lfm.coverage(p, q)
            popularity = lfm.popularity(p, q)
            print("%3d%20d%19.3f%%%19.3f%%%19.3f%%%20.3f" % (
            ratio, lclass, recall * 100, precision * 100, coverage * 100, popularity))

    end = time.clock()
    print('finish all in %s' % str(end - start))
