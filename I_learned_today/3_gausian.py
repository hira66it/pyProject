import scipy as sp
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import random

mu = 0
std = 1
sigma = 1
xx = np.linspace(-10, 10, 1000)
# rnd = rv.pdf(rv.rvs(size=(1, 100), random_state=0))


def meanStd(tmp):
    mean = np.mean(tmp[0])
    var = np.var(tmp[0], dtype=np.float64)
    return (mean,var)


def makesample(n):
    tmp=[]
    lst_x = np.random.normal(mu,std,n)
    # lst_x = [-1,0,1]
    lst_y =[]
    for bins in lst_x:
        lst_y.append(1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2)))
    tmp.append(lst_x.tolist())
    # tmp.append(lst_x)
    tmp.append(lst_y)
    return tmp
def gausian(mu,std):
    rv = sp.stats.norm(mu, std)
    return rv.pdf(xx)
#가우시안 분포 그리기
plt.plot(xx, gausian(0,1))

gaus_n=makesample(10)
plt.plot(xx, gausian(meanStd(gaus_n)[0],meanStd(gaus_n)[1]),'b')

gaus_n=makesample(100)
plt.plot(xx, gausian(meanStd(gaus_n)[0],meanStd(gaus_n)[1]),'g')

gaus_n=makesample(1000)
plt.plot(xx, gausian(meanStd(gaus_n)[0],meanStd(gaus_n)[1]),'r')

plt.ylabel("p(x)")
plt.title("probability density function(pdf)")
plt.show()