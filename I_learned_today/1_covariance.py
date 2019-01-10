from __future__ import division
import math

def mean(x):
    tmp_value=0
    for tmp in (x):
        tmp_value+=tmp
    return tmp_value/len(x)
def variance(x_V):
    tmp_value=0
    n=len(x_V)-1
    for tmp in (x_V):
        tmp_value+=(tmp-mean(x_V))**2
    return tmp_value/n

def standard(x_S):
    return math.sqrt(variance(x_S))

def pre_cov(x_CX,x_CY):
    tmp_out=0
    for i,val in enumerate(x_CX):
        tmp_out+=(x_CX[i]-mean(x_CX))*(x_CY[i]-mean(x_CY))/(len(x_CX)-1)
    return tmp_out

def covariance(x_C):
    n = len(x_C[0])
    tmp_co = []
    for n_x in range(n):
        tmp_co_= []
        for n_y in range(n):
            tmp_x = []
            tmp_y = []
            for tmp in x_C:
                tmp_x.append(tmp[n_x])
            for tmp in x_C:
                tmp_y.append(tmp[n_y])
            
            tmp_co_.append(pre_cov(tmp_x,tmp_y))
        tmp_co.append(tmp_co_)
    return tmp_co

def main():
    a = [[1,3],[2,2],[3,1]]
    print (covariance(a))

if __name__=="__main__":
    main()
