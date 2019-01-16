import numpy as np
import matplotlib.pyplot as plt
x = np.array([10,15,20,25,30])
y = np.array([0.930,0.926,0.921,0.917,0.922])
y1=np.array([0.923,0.919,0.915,0.908,0.914])

plt.plot(x, y, marker='o', mec='r', mfc='w',label="K-SVD")
plt.plot(x, y1, marker='^', mec='b', mfc='w',label="GSVD")
# 设置坐标轴的取值范围
plt.xlim((5, 35))
plt.ylim((.90, 0.950))
plt.legend(['K-SVD','GSVD'])

# 设置坐标轴的lable
#标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'ClusterNumber',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'RMSE',fontproperties='SimHei',fontsize=14)



plt.show()