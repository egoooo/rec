import numpy as np
import matplotlib.pyplot as plt


w= np.linspace(0.1, 1000, 1000)
p = np.abs(1 / (1 + 0.1j * w))

plt.subplot(221)
plt.plot(w, p, lw=2)
plt.xlabel('X')
plt.ylabel('y');

plt.subplot(222)
plt.semilogx(w, p, lw=2)
plt.ylim(0, 1.5)
plt.xlabel('log(X)')
plt.ylabel('y')

plt.subplot(223)
plt.semilogy(w, p, lw=2)
plt.ylim(0, 1.5)
plt.xlabel('x')
plt.xlabel('log(y)')

plt.subplot(224)
plt.loglog(w, p, lw=2)
plt.ylim(0, 1.5)
plt.xlabel('log(x)')
plt.xlabel('log(y)')
plt.show()