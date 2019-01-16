import numpy as np
import matplotlib.pyplot as plt
size = 4
mae=np.array([0.714,0.702,0.690,0.725])
rmse=np.array([0.922,0.914,0.908,0.927])


x = np.arange(size)

total_width, n = 0.8, 2     # 有多少个类型，只需更改n即可
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, mae,  width=width, label='MAE',color="lightgray")
plt.bar(x + width, rmse, width=width, label='RMSE',tick_label=['0.001','0.002','0.005','0.01'],color="dimgray")

plt.ylim((0, 1.5))
# 设置坐标轴的lable
#标签里面必须添加字体变量：fontproperties='SimHei',fontsize=14。不然可能会乱码
plt.xlabel(u'alpha',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'MAE/RMSE',fontproperties='SimHei',fontsize=14)

for a, b in zip(x,mae):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)

for a, b in zip(x,rmse):
    plt.text(a+width, b, b, ha='center', va='bottom', fontsize=10)
plt.legend()
plt.show()