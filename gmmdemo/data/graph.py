
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0.,10,0.2)
y1=np.cos(x)
y2=np.sin(x)
y3=np.sqrt(x)
plt.rcParams['figure.figsize']=(10,6)   #reParams设置图片尺寸
plt.plot(x,y1,color='blue',linewidth=1.5,linestyle='-',marker='.',label=r'$y=cos{x}$')
plt.plot(x,y2,color='green',linewidth=1.5,linestyle='-',marker='*',label=r'$y=sin{x}$')
plt.plot(x,y3,color='m',linewidth=1.5,linestyle='-',marker='x',label=r'$y=\sqrt{x}$')
plt.legend(loc='upper right')  #loc参数设置图例在图片中的位置

plt.text(8.0,1,r'$x \in [0.0, \ 10.0]$',color='k',fontsize=10)
plt.text(4.0,2.0,r'$y \in [-1.0, \ 4.0]$',color='k',fontsize=10)

plt.scatter([8,],[np.sqrt(8),],50,color='m')  #使用散点图放大当前点
plt.annotate(r'$2\sqrt{2}$',xy=(8,np.sqrt(8)),xytext=(8.5,2.2),fontsize=16,color='#090909',\
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.1',color='#090909'))
#xy参数设置'被注解点'的坐标,xytext参数设置'注解文字'的位置,arrowprops参数设置注解文字与被注解点的连接方式


# x, y = np.mgrid[-2:2:20j, -2:2:20j]
# z = x * np.exp(-x ** 2 - y ** 2)
# ax = plt.subplot(111, projection='3d')
# ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plt.cm.coolwarm, alpha=0.8)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
plt.show()