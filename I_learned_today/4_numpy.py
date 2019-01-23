import numpy as np

values = [[1, 1],[1,1]]
a = np.array(values)

a.shape
print(np.dot(a,np.dot(a,a)))
print(np.dot(a,a,a))


m = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(m.shape)
n =m.T
print(n.shape)
