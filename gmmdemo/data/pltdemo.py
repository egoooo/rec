import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1,2,3,4])
# # plt.ylabel('some numbers')
# # plt.show()

#


# plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.axis([0,6,0,20])
# plt.show()

#
# x=np.arange(0.,1,0.02)
# plt.xlim(x.min()*1.1,x.max()*1.1)
# plt.ylim(-1.5,4.0)
# plt.text(0.8,2.9,r'$x \in [0.0, \ 10.0]$',color='k',fontsize=10)
# plt.text(0.8,0.8,r'$y \in [-1.0, \ 4.0]$',color='k',fontsize=10)
#
# plt.show()



size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
d = np.random.random(size)
x = np.arange(size)

total_width, n = 0.8, 4     # 有多少个类型，只需更改n即可
width = total_width / n
x = x - (total_width - width) / 2

plt.bar(x, a,  width=width, label='svd')
plt.bar(x + width, b, width=width, label='svd++')
plt.bar(x + 2 * width, c, width=width, label='CF')
plt.bar(x + 3 * width, d, width=width, label='UF')
plt.legend()
plt.show()