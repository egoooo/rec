import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

x = np.array([20,30,40,50,60])
y = np.array([0.9493,
0.9421,
0.9365,
0.9340,
0.9345,
])
y1=np.array([0.9431,
0.9375,
0.9337,
0.9311,
0.9308,
])
y2=np.array([0.9391,
0.9337,
0.9294,
0.9262,
0.9258])
y3=np.array([0.9365,
0.9270,
0.9213,
0.9171,
0.9176,
])
y4=np.array([0.9370,
0.9281,
0.9223,
0.9179,
0.9175,
])

plt.plot(x, y, marker='o', mec='r', mfc='w',label="f=10")
plt.plot(x, y1, marker='^', mec='b', mfc='w',label="f=20")
plt.plot(x, y2, marker='s', mec='b', mfc='w',label="f=30")
plt.plot(x, y3, marker='.', mec='b', mfc='w',label="f=40")
plt.plot(x, y4, marker='x', mec='b', mfc='w',label="f=60")
# 设置坐标轴的取值范围
plt.xlim((10, 70))
plt.ylim((.91, 0.96))
plt.legend()
# 设置坐标轴的lable
#标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'NeighborNumber',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'RMSE',fontproperties='SimHei',fontsize=14)
plt.title("隐因子数量和邻居数量对算法的RMSE的影响",fontproperties='SimHei',fontsize=10)

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



plt.show()