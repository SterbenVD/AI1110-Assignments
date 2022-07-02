import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import mpmath as mp

maxrange = 100
x = np.linspace(-6, 6, maxrange)
size = 1000000
err = []
arr = np.loadtxt('gau.dat', dtype='double')
for i in range(0, maxrange):
    arr_leq = np.nonzero(arr < x[i])
    arr_n = np.size(arr_leq)
    err.append(arr_n/size)

tg = []
def gauss_pdf(y):
	return 1/mp.sqrt(2*np.pi)*np.exp(-y**2/2.0)

sum = 0
for i in range(0,maxrange):
    sum += gauss_pdf(x[i]) * (12/maxrange)
    tg.append(sum)

plt.scatter(x, err, color="blue", label="Experimental CDF")
plt.plot(x, tg, color='orange', label="Theoretical CDF")
plt.xlabel('$x$')
plt.ylabel('$CDF$')
plt.legend(loc='best')
plt.savefig('../figs/2_cdf.png')
plt.show()
