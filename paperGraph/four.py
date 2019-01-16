import numpy as np
import matplotlib.pyplot as plt
size = 4
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
d = np.random.random(size)
x = np.arange(size)

total_width, n = 0.8, 4    # 有多少个类型，只需更改n即可
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, a,  width=width, label='f=10',tick_label=['10','20','25','30'])
plt.bar(x + width, b, width=width, label='f=20')
plt.bar(x + 2 * width, c, width=width, label='f=30')
plt.bar(x + 3 * width, d, width=width, label='f=40')

# 设置坐标轴的lable
#标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'ClusterNumber',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'MAE',fontproperties='SimHei',fontsize=14)
plt.legend()
plt.show()