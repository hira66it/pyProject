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

x = np.linspace(-3.5, 5.5, 2251)

print(np.random.rand(2,2)) #random value [1,1,1,1,1]
print(np.random.randn(2,2)) #normal distribution [5x5]
print(np.random.random())

print( np.random.randint(3,5,(2,2),dtype=np.int32) )
np.random.normal(mu,std,n)
np.random.seed(seed=None)
x.tolist() # to python list
np.empty([2, 2], dtype=np.absint64)
npa = np.asarray([1,2,3], dtype=np.float64)

a = np.arange(15).reshape(3,5)
print(a.shape,a.dtype.name)
b= np.array([1.+4j,2.,3.],dtype=complex)
b=np.zeros((3,3,3))
b=np.ones((3,3,3))
b=np.identity(3)
b=np.pi
b=np.linspace(0,2*np.pi,10).reshape(5,2)
f=np.sin(b)
print(f<0)
print(np.array([[1,0],[1,1]])*np.ones((2,2)).reshape(2,2))
print(b.T@b)
print(b.sum(axis=1))

a = np.arange(3)
print(a[:3:3])
#arr1 = np.ndarray([1,2,3])
#print(ndarray.ndim(arr1))
print(np.cos(np.pi))
