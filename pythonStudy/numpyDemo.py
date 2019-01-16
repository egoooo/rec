import numpy as np
from matplotlib import pyplot as plt
c=np.arange(25)
c.resize([5,5])
print(c)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]

a=c+3
print(a)

a>23
print(a)



x=np.random.rand(10)
C=x>0.5
print(x[x>0.5])
print(C)



B = np.arange(3)
print(B)                   # [0 1 2]
print(np.exp(B))           # [ 1.   2.71828183  7.3890561 ]
print(np.sqrt(B))          # [ 0.   1.          1.41421356]

x = np.arange(-100,100)
y =  2  * x* x*x +  5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"--ob")
plt.show()


