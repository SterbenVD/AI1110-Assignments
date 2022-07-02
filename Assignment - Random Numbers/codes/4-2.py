import numpy as np
import matplotlib.pyplot as plt

# Experimental Graph
maxrange = 60
x = np.linspace(-0.5, 2.5, maxrange)
size = 1000000
err = []
arr = np.loadtxt('tri.dat', dtype='double')
for i in range(0, maxrange):
    arr_len = np.count_nonzero(arr < x[i])
    err.append(arr_len/size)

# Theory Graph
tg = []
def tpdf(y):
    ans = 0
    if(y < 0 or y > 2):
        ans = 0
    elif(y < 1):
        ans = y
    else:
        ans = 2 - y
    return ans

sum = 0
for i in range(0, maxrange):
    sum += tpdf(x[i]) * (3/maxrange)
    tg.append(sum)

plt.scatter(x.T, err, label="Experimental CDF")
plt.plot(x, tg, color='orange', label="Theoretical CDF")
plt.xlabel('$T$')
plt.ylabel('$CDF$')
plt.legend(loc='best')
plt.savefig('../figs/4_cdf.png')
plt.show()
