import matplotlib.pyplot as plt
import numpy as np


plt.plot(x, y, 'b', alpha=0.6, label='gamma(x)')
k = np.arange(1, 7)
plt.plot(k, factorial(k-1), 'k*', alpha=0.6,\
        label='(x-1)!, x = 1, 2, ...')
plt.xlim(-3.5, 5.5)
plt.ylim(-10, 25)
plt.grid()
plt.xlabel('x')
plt.legend(loc='lower right')

#'ro','r.','r-'

x = np.linspace(-3.5, 5.5, 2251)
np.linspace(2.0, 3.0, num=5)
#>>> array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
np.linspace(2.0, 3.0, num=5, endpoint=False)
#>>> array([ 2. ,  2.2,  2.4,  2.6,  2.8])
np.linspace(2.0, 3.0, num=5, retstep=True)
#>>> (array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)


#-------------------histogram---------------------#
mu, sigma = 0, 0.1 # mean and standard deviation
# np.random.nomral 함수를 이용해서 평균 0, 표준편차 0.1인 sample들을 1000개 추출한다.
s = np.random.normal(mu, sigma, 1000)
# sample들의 historgram을 출력한다.
count, bins, ignored = plt.hist(s, 30, normed=True)
# sample들을 이용해서 Gaussian Distribution의 shape을 재구축해서 line으로 그린다.
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * \
		np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()