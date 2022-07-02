import numpy as np
import matplotlib.pyplot as plt

# Theory Graph
tg = np.concatenate([np.zeros(10),np.linspace(0,1,20), np.ones(10)])

# Experimental Graph	
maxrange = 40
x = np.linspace(-0.5,1.5,maxrange)
size = 1000000
err = []
arr = np.loadtxt('uni.dat',dtype = 'double')
for i in range(0,maxrange):
	arr_len= np.count_nonzero(arr < x[i])
	err.append(arr_len/size)

plt.scatter(x.T,err,label="Experimental CDF")
plt.plot(x,tg,color="orange",label="Theoretical CDF")
plt.xlabel('$x$')
plt.ylabel('$CDF$')
plt.legend(loc='best')
plt.savefig('../figs/1_cdf.png')
plt.show()