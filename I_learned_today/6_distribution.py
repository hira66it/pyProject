import numpy as np
import random
import math
import time
from scipy.special import gamma, factorial

class OneParameterDist:
    def __init__(self, mu):
        self.mu = mu
    
    def sample(self, n):
        print("Hello")

    def pdf(self, x):
        print("World!")
    
    def mean(self):
        print("!!")

    def var(self):
        print("miroh")

    def std(self):
        print("31894")


class Bernoulli(OneParameterDist):
    def sample(self, n):
        self.procsdSample = [0.] * n
        for i in range(n):
            tmp = random.random()
            if tmp <= self.mu:
                self.procsdSample[i]=1.
            else: self.procsdSample[i] =0.
        return self.procsdSample

    def pdf(self, x):
        if x==0: return 1-self.mu
        elif x==1: return self.mu
    def mean(self):
        return self.mu
    def var(self):
        return( self.mu*(1-self.mu))
    def std(self):
        return math.sqrt(self.var())
#-------------------------------------------------------------#
def mean(arr):
    return sum(arr)/len(arr)
def var(arr):
    return mean(list(map(lambda x: x**2, arr)))-mean(arr)**2
def std(arr):
    return math.sqrt(var(arr))
#-------------------------------------------------------------#
sample_size=10000
mu = 0.1
b = Bernoulli(mu)
b_sample = b.sample(sample_size)

print( 'Theoritical_mean : ', b.mean() )
print( 'Theoritical_var : ',b.var())
print( 'Theoritical_std : ',b.std())
print( 'pdf(1) : ', b.pdf(1) )
print( 'pdf(0) : ', b.pdf(0) )
print( 'sample_mean : ',mean(b_sample) )
print( 'sample_var : ' ,var(b_sample))
print( 'sample_std : ' ,std(b_sample))


class TwoParameterDist:
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
    def sample(self, n):
        print("Hello")

    def pdf(self, x):
        print("World!")
    
    def mean(self):
        print("!!")

    def var(self):
        print("miroh")

    def std(self):
        print("31894")

class Beta(TwoParameterDist):
    def sample(self, n):
        a= self.alpha
        b= self.beta
        self.mode = (a-1)/(a+b-2)

        self.procsdSample = [0.] * n
        c = self._beta(self.mode)
        i=0
        np.random.seed(seed=None)
        random.seed(time.time_ns() * 2)
        while i<n:
            u1 = np.random.rand()
            u2 = random.random()
            if u1 <= self._beta(u2)/c:
                self.procsdSample[i]=u2
                i +=1
        return self.procsdSample
    def _beta(self,x):
        a= self.alpha
        b= self.beta
        return gamma(a+b)/gamma(a)/gamma(b) * (x**(a-1)) * ((1-x)**(b-1))
    def pdf(self, x):
        return self._beta(x)
    def mean(self):
        return self.alpha/(self.alpha+self.beta)
    def var(self):
        a=self.alpha
        b=self.beta

        return( (a*b)/ ((a+b)**2) / (a+b+1) )
    def std(self):
        return math.sqrt(self.var())

sample_size=10000
mu = 0.1
b = Beta(3,2)
b_sample = b.sample(sample_size)

print( 'Theoritical_mean : ', b.mean() )
print( 'Theoritical_var : ',b.var())
print( 'Theoritical_std : ',b.std())
print( 'pdf(0.6) : ', b.pdf(0.6) )
print( 'pdf(2/3) : ', b.pdf(2./3.) )
print( 'sample_mean : ',mean(b_sample) )
print( 'sample_var : ' ,var(b_sample))
print( 'sample_std : ' ,std(b_sample))