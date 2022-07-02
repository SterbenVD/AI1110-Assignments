import numpy as np
import matplotlib.pyplot as plt

maxrange = 50
x = np.linspace(-2, 10, maxrange)
size = 1000000
err = []
arr = np.loadtxt('uni.dat', dtype='double')
log = np.log(arr)
var = np.array([-2 * i for i in log])
for i in range(0, maxrange):
    arr_leq = np.nonzero(var < x[i])
    arr_n = np.size(arr_leq)
    err.append(arr_n/size)

tg = []
def tcdf(y):
	return 1 - np.exp(-y/2)

for i in range(0,maxrange):
    if(x[i] > 0):
        temp = tcdf(x[i])
        tg.append(temp)
    else:
        tg.append(0)

plt.scatter(x, err, color="blue", label="Experimental CDF")
plt.plot(x, tg, color='orange', label="Theoretical CDF")
plt.xlabel('$V$')
plt.ylabel('$CDF$')
plt.legend(loc='best')
plt.savefig('../figs/3_cdf.png')
plt.show()
