import numpy as np
import matplotlib.pyplot as plt

maxrange = 80
x = np.linspace(-6,6,maxrange)
size = 1000000
err = []
arr = np.loadtxt('uni.dat',dtype = 'double')
for i in range(0,maxrange):
	arr_leq= np.nonzero(arr < x[i])
	arr_n = np.size(arr_leq)
	err.append(arr_n/size)

	
plt.plot(x.T,err)
plt.xlabel('$x$')
plt.ylabel('$CDF$')
plt.savefig('../figs/2_cdf.png')
plt.show()
