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

print( '\n## Bernoulli Distribution ##\n')
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
        c = self._beta(self.mode)
        self.procsdSample = [0.] * n
        
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
b = Beta(3,2)
b_sample = b.sample(sample_size)
print( '\n\n\n## Beta Distribution ##\n')
print( 'Theoritical_mean : ', b.mean() )
print( 'Theoritical_var : ',b.var())
print( 'Theoritical_std : ',b.std())
print( 'pdf(0.6) : ', b.pdf(0.6) )
print( 'pdf(2/3) : ', b.pdf(2./3.) )
print( 'sample_mean : ',mean(b_sample) )
print( 'sample_var : ' ,var(b_sample))
print( 'sample_std : ' ,std(b_sample))

class NormalDist(TwoParameterDist):
    def __init__(self,alpha,beta):
        super().__init__(alpha, beta)
        self.SIGMA = math.sqrt(self.beta)
    def sample(self,n):
        MU=self.alpha
        
        self.procsdSample = [0.] * n
        i=0
        while i<n:
            x = random.uniform(-1.0, 1.0)
            y = random.uniform(-1.0, 1.0)
            w = x**2 + y**2
            if w>=0 and w<=1:
                g = MU + x * self.SIGMA * math.sqrt(-2 * math.log(w) / w)
                
                self.procsdSample[i]=g
                i+=1
        return self.procsdSample  
    def pdf(self, x):
        return 1./(math.sqrt(2.*math.pi)*self.SIGMA)*np.exp(-np.power((x - self.alpha)/self.SIGMA, 2.)/2)
    def mean(self):
        return self.alpha
    def var(self):
        a=self.alpha
        b=self.beta
        return b
    def std(self):
        return math.sqrt(self.beta)

sample_size=10000
b = NormalDist(0,1)
b_sample = b.sample(sample_size)
print( '\n\n\n## Normal Distribution ##\n')
print( 'Theoritical_mean : ', b.mean() )
print( 'Theoritical_var : ',b.var())
print( 'Theoritical_std : ',b.std())
print( 'pdf(0.6) : ', b.pdf(0.6) )
print( 'pdf(2/3) : ', b.pdf(2./3.) )
print( 'sample_mean : ',mean(b_sample) )
print( 'sample_var : ' ,var(b_sample))
print( 'sample_std : ' ,std(b_sample))

class Gamma(TwoParameterDist):
    def __init__(self,alpha,beta):
        super().__init__(alpha,beta)
    def sample(self,n):
        a = self.alpha
        b = self.beta
        self.procsdSample = [0.] * n
        i=0
        d = a - 1. / 3.
        c = 1. / math.sqrt(9.0 * d)
        while i<n:
            x = np.random.normal()
            v = 1. + c * x
            while (v <= 0.):
                x = np.random.normal()
                v = 1. + c * x
            v = v * v * v
            u = random.uniform(0, 1.0)
            if (u < 1. - 0.0331 * (x * x * x * x)):
                self.procsdSample[i]= (b * d * v)
                i+=1
                continue
            if (math.log(u) < 0.5 * x * x + d * (1. - v + math.log(v))):
                self.procsdSample[i]= (b * d * v)
                i+=1
        return self.procsdSample
        # ------------ You should edit below this line --------------------

    def pdf(self, x):
        a=self.alpha
        b=self.beta
        return (b**a) * (x **(a-1)) * np.exp(-b*x) / gamma(a)
    def mean(self):
        return self.alpha/self.beta
    def var(self):
        a=self.alpha
        b=self.beta
        self.var_val = a / (b**2)
        return self.var_val
    def std(self):
        return math.sqrt(self.var_val)

sample_size=10000
b = Gamma(2,1)
b_sample = b.sample(sample_size)
print( '\n\n\n## Gamma Distribution ##\n')
print( 'Theoritical_mean : ', b.mean() )
print( 'Theoritical_var : ',b.var())
print( 'Theoritical_std : ',b.std())
print( 'pdf(0.6) : ', b.pdf(0.6) )
print( 'pdf(2/3) : ', b.pdf(2./3.) )
print( 'sample_mean : ',mean(b_sample) )
print( 'sample_var : ' ,var(b_sample))
print( 'sample_std : ' ,std(b_sample))
