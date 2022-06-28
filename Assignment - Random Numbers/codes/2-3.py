import numpy as np
import matplotlib.pyplot as plt

maxrange=80
x = np.linspace(-6,6,maxrange)
size = 1000000
err = []
derr = []
arr = np.loadtxt('uni.dat',dtype = 'double')

for i in range(0,maxrange):
	arr_leq= np.nonzero(arr < x[i])
	arr_n = np.size(arr_leq)
	err.append(arr_n/size)

for i in range(0,maxrange-1):
	derr.append(err[i+1]-err[i])/(x[i+1]-x[i])

plt.plot(x[0:(maxrange-1)].T,derr)
plt.xlabel('$x$')
plt.ylabel('$PDF$')
plt.savefig('../figs/2_pdf.png')
plt.show()
