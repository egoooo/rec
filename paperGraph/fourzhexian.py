import numpy as np
import matplotlib.pyplot as plt
x = np.array([10,15,20,25,30])
y = np.array([0.930,0.926,0.921,0.917,0.921])
y1=np.array([0.925,0.920,0.916,0.913,0.918])
y2=np.array([0.923,0.919,0.915,0.908,0.914])
y3=np.array([0.927,0.923,0.920,0.911,0.919])
y4=np.array([0.931,0.928,0.924,0.917,0.923])

plt.plot(x, y, marker='o', mec='r', mfc='w',label="f=10")
plt.plot(x, y1, marker='^', mec='b', mfc='w',label="f=20")
plt.plot(x, y2, marker='s', mec='b', mfc='w',label="f=30")
plt.plot(x, y3, marker='.', mec='b', mfc='w',label="f=40")
plt.plot(x, y4, marker='x', mec='b', mfc='w',label="f=60")
# 设置坐标轴的取值范围
plt.xlim((5, 35))
plt.ylim((.90, 0.94))
plt.legend()
# 设置坐标轴的lable
#标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'ClusterNumber',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'RMSE',fontproperties='SimHei',fontsize=14)
plt.title("GSVD不同k,f下的RMSE值",fontproperties='SimHei',fontsize=10)
plt.show()