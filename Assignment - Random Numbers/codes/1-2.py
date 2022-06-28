import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-0.1,1.1,80)
size = 1000000
err = []
arr = np.loadtxt('uni.dat',dtype = 'double')
for i in range(0,80):
	arr_leq= np.nonzero(arr < x[i])
	arr_n = np.size(arr_leq)
	err.append(arr_n/size)

	
plt.plot(x.T,err)
plt.xlabel('$x$')
plt.ylabel('$CDF$')
plt.savefig('../figs/1_cdf.png')
plt.show()
