import numpy as np
totalrainfall=np.array([2146,724.8,784.3,2161.4,529,802.3,962.8,1425.4,718.3,739.4,1613.6,931,1039.8,814.6,1120.5,1123.1,1554.3,373.7,310.1,1063.2,1311.9,646.9,3480.8,2208.9,3063.6,2658.3,657.6,3539.3,1130.3,2932,1171.9,1238.9,759.5,1721.1,842,490.7,828.5,1582.3,960.9,1358.7,1521.5,629.4,212,1193,1272,1460.9,444.8,850.9,734.9,675.9,3687.9,1617.2,1831.3,1651.4,722.4,3135.5,1009.4,698.7,842.6,1396.1,3796.9,1645.2,1313.4,2431.3,804.2,1166.3,705.3,795.4,716.2,933.7,4431.3,1127.5,3034.8,1728,699.9,1318.9,689.2,1440.8,2207.5,1539.3,3218,722.7,676.2,1419.6,1117.2,1796.6,1870.3,611.5,1033.8,0,736.2,1102.7])
totalrainfall=totalrainfall/200
#
mean=totalrainfall.mean()
var=totalrainfall.var()
binning=list(range(0,20))
#hist,bins = np.histogram(totalrainfall,bins =binning)
print(len(totalrainfall))
print(mean)
print(var)
p=1-mean/var
r=(1-p)*mean/p
#---------
from scipy.stats import nbinom
X = np.arange(0, 20)
XX=np.arange(3,20+3)
neg=75*nbinom.pmf(X, r, p)
#--------------
from scipy.special import factorial
t = np.arange(0, 20, 0.1)
d = 120*np.exp(-mean)*np.power(mean, t)/factorial(t)
#--------------------
from matplotlib import pyplot as plt
plt.hist(totalrainfall,bins = binning, label="data")
plt.title("totalrainfall")
#--------------
plt.vlines(XX, 0, neg, colors='y', lw=5, alpha=0.5, label="neg binomial fit")
plt.plot(t, d,label="poisson fit")
plt.xlabel('annual rainfall (scaled by 200) in mm')
plt.ylabel('number of cities')
plt.legend()
#------------------------------------
plt.savefig("fits.png")
plt.show()
