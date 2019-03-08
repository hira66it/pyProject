import numpy as np

def main():
    nn = Neural_NET()
    X = np.matrix("0 0; 0 1; 1 0; 1 1")
    y = np.matrix("0;1;1;0")
    print(nn.train(X, y, 5000)) ## Eddit
    # for e in X:
    #     print(e,nn.predict(e))

class calculus(object):
    def __init__(self):
        pass
    def sigmoid(self,x):
        return 1./(1.+np.exp(-x))
    def sigmoid_prim(self,x):
        return self.sigmoid(x) *(1. - self.sigmoid(x))
    def tanh(self, x):
        return np.tanh(x)
    def tanh_prime(self, x):
        return 1.0 - x**2

class Neural_NET(calculus):
    def __init__(self):
        super(Neural_NET,self).__init__()
        self.learning_rate = 0.25
        self.hidden_layer = 2 ## Eddit
    def forward(self,weights, inputb):
        s = np.matmul(inputb, weights)
        g = self.sigmoid(s)
        return g
    def train(self,inputvalue,answer,times):
        x = inputvalue    # X = n x L
        v = self.weight_init(x.shape[1],self.hidden_layer ) # v = (L+1) x M
        w = self.weight_init(self.hidden_layer, 1) # w = (M+1) x N
        t = answer   # t = n x N
        xb = self.addBias(x,-1) # xb = n x (L+1)
        for i in range(times):
            a = self.forward(v, xb) # a = n x M
            ab = self.addBias(a,-1) # ab = n x (M+1)
            y = self.forward(w,ab) # y = n x N
            err = np.matmul((y - t).T , (y - t)) # err = n x n
            if (i+1)%1000 ==0: print(err)
            wb = self.hideBias(w)
            do = np.multiply(np.multiply( (y - t) , y ) , (1 - y))
            dh = np.multiply(np.multiply( np.matmul(do ,wb.T) , a ) , (1-a))
            w = w - self.learning_rate * np.matmul(ab.T, do)
            v = v - self.learning_rate * np.matmul(xb.T, dh)
        a = self.forward(v, xb)
        ab = self.addBias(a, -1)
        y = self.forward(w, ab)
        return y
    def addBias(self,inputb,bias):
        return np.column_stack((np.full((inputb.shape[0], 1), bias), inputb))
    def hideBias(self,weights):
        return weights[1:,]
    def weight_init(self, m, n ):
        return np.random.uniform(-1,1,(m+1,n))


if __name__ == '__main__':
    main()
    