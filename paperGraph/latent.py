import numpy as np
import matplotlib.pyplot as plt
x = np.array([10,20,30,40,60])
y = np.array([0.750,0.747,0.743,0.738,0.743])
y1=np.array([0.734,0.731,0.726,0.730,0.735])
y2=np.array([0.705,0.698,0.690,0.695,0.701])
y3=np.array([0.772,0.772,0.772,0.772,0.772])

plt.plot(x, y, marker='o', mec='r', mfc='w',label="Funk-SVD")
plt.plot(x, y1, marker='^', mec='b', mfc='w',label="BiasSVD")
plt.plot(x, y2, marker='s', mec='b', mfc='w',label="GLFM")
plt.plot(x, y3, marker='x', mec='b', mfc='w',label="U-CF")
# 设置坐标轴的取值范围
plt.xlim((0, 70))
plt.ylim((.65, 0.80))
plt.legend(['Funk-SVD','BiasSVD','GSVD',"U-CF"])
# 设置坐标轴的lable
#标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'LatentFactorNumber',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'MAE',fontproperties='SimHei',fontsize=14)
plt.show()