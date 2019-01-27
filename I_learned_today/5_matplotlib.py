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
