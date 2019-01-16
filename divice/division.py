#!usr/bin/env python
# encoding:utf-8
from __future__ import division

'''
__Author__:沂水寒城
学习Python中的X[:,0]、X[:,1]、X[:,:,0]、X[:,:,1]、X[:,m:n]和X[:,:,m:n]
'''

# 对于X[:,0];
#
# 是取二维数组中第一维的所有数据 列
#
# 对于X[:,1]
#
# 是取二维数组中第二维的所有数据 列
#
# 对于X[:,m:n]
#
# 是取二维数组中第m维到第n-1维的所有数据
#
# 对于X[:,:,0]
#
# 是取三维矩阵中第一维的所有数据
#
# 对于X[:,:,1]
#
# 是取三维矩阵中第二维的所有数据
#
# 对于X[:,:,m:n]
#
# 是取三维矩阵中第m维到第n-1维的所有数据

import numpy as np


def simple_test():
    '''
    简单的小实验
    '''
    data_list = [[1, 2, 3], [1, 2, 1], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [6, 7, 9], [0, 4, 7], [4, 6, 0],
                 [2, 9, 1], [5, 8, 7], [9, 7, 8], [3, 7, 9]]
    # data_list.toarray()
    data_list = np.array(data_list)
    print(data_list)
    print('X[:,0]结果输出为：')
    print(data_list[:, 0])

    print('X[:,1]结果输出为：')

    print (data_list[:, 1])

    print ('X[:,m:n]结果输出为：')
    print(data_list[:, 0:1])

    data_list = [[[1, 2], [1, 0], [3, 4], [7, 9], [4, 0]], [[1, 4], [1, 5], [3, 6], [8, 9], [5, 0]],
                 [[8, 2], [1, 8], [3, 5], [7, 3], [4, 6]],
                 [[1, 1], [1, 2], [3, 5], [7, 6], [7, 8]], [[9, 2], [1, 3], [3, 5], [7, 67], [4, 4]],
                 [[8, 2], [1, 9], [3, 43], [7, 3], [43, 0]],
                 [[1, 22], [1, 2], [3, 42], [7, 29], [4, 20]], [[1, 5], [1, 20], [3, 24], [17, 9], [4, 10]],
                 [[11, 2], [1, 110], [3, 14], [7, 4], [4, 2]]]
    data_list = np.array(data_list)
    print(data_list)
    print('X[:,:,0]结果输出为：')

    print (data_list[:, :, 0])

    print('X[:,:,1]结果输出为：')

    print(data_list[:, :, 1])

    print ('X[:,:,m:n]结果输出为：')

    print(data_list[:, :, 0:1])

    X=[[1,2],[3,4]]
    data_list = np.array(X)
    print(data_list)
    X=data_list[:,::-1] #交换行和列
    print(X)



if __name__ == '__main__':
    simple_test()
