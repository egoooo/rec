import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

x = np.array([20,30,40,50,60])
y = np.array([0.9676,
0.9608,
0.9554,
0.9509,
0.9501,
])
y1=np.array([0.9585,
0.9527,
0.9503,
0.9489,
0.9485
])
y2=np.array([0.9371,
0.9371,
0.9371,
0.9371,
0.9371
])
y3=np.array([0.9365,
0.9278,
0.9212,
0.9171,
0.9176,
])

plt.plot(x, y, marker='o', mec='r', mfc='w',label="U-CF")
plt.plot(x, y1, marker='^', mec='b', mfc='w',label="I-CF")
plt.plot(x, y2, marker='s', mec='b', mfc='w',label="SVD")
plt.plot(x, y3, marker='x', mec='b', mfc='w',label="ours")
# 设置坐标轴的取值范围
plt.xlim((10, 70))
plt.ylim((.9100, 0.9750))
plt.legend()
# 设置坐标轴的lable
#标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'NeighborNumber',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'RMSE',fontproperties='SimHei',fontsize=14)

#修改主刻度
ax=plt.subplot(111)
xmajorLocator = MultipleLocator(10) #将x主刻度标签设置为20的倍数
xmajorFormatter = FormatStrFormatter('%5.0f') #设置x轴标签文本的格式
ymajorLocator = MultipleLocator(0.005) #将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%1.3f') #设置y轴标签文本的格式
# #设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)

#修改次刻度
xminorLocator = MultipleLocator(5) #将x轴次刻度标签设置为5的倍数
yminorLocator = MultipleLocator(0.1) #将此y轴次刻度标签设置为0.1的倍数
#设置次刻度标签的位置,没有标签文本格式
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)

plt.annotate('min RMSE 0.9171', xy=(50, 0.9171), xytext=(55, 0.9250),arrowprops=dict(facecolor='black', shrink=0.05,width=1,headlength=5,headwidth=3))
plt.show()