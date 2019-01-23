import scipy as sp
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
import random

def makesample(n,mu,std):
    tmp=[]
    lst_x = np.random.normal(mu,std,n)
    return lst_x

n=100
x1 = makesample(n,2,1)
x2 = makesample(n,-2,1)
y1 = makesample(n,0,3)
y2 = makesample(n,0,3)

sigma_ml = np.dot(x1-np.mean(x1),np.transpose(x2-np.mean(x2)))

plt.plot(x1, y1,'b.')
plt.plot(x2, y2,'r.')


plt.ylabel("p(x)")
plt.title("probability density function(pdf)")
plt.show()