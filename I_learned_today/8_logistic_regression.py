import matplotlib.pyplot as plt
import numpy as np
mu=0
std=1
sigma=1
n=500

def data_gen(data,y):
    tmp_y = [x + 0.5 * np.random.randn(1)+ y for x in data]
    tmp_x = [x - 0.5 * np.random.randn(1) for x in data] 
    return (tmp_x,tmp_y)


blue_point = data_gen(np.random.normal(mu,std,n),-5)
red_point = data_gen(np.random.normal(-1,std,n),2)


x_val = np.random.normal(mu,1,n)
y_val = np.random.normal(mu,0.3,n)
r = np.sqrt(2)/2
rotation_matrix = np.array([[r,-r],[r,r]])

init_point = np.matmul(rotation_matrix,[x_val,y_val])

blue_point = init_point + np.array([[1], [-1]])
red_point = init_point + np.array([[-1], [1]])


def plot_dot(x,y,color):
    plt.plot(x, y, color, alpha=0.6, label=color)
#     plt.xlim(-4, 4)
#     plt.ylim(-8, 6)
    plt.grid()
    plt.xlabel('x')
    plt.legend(loc='lower right')
plot_dot(blue_point[0],blue_point[1],'bo')
plot_dot(red_point[0],red_point[1],'rx')

T_matrix = np.empty((n*2,2))
for i,x in enumerate(range(n)):
    T_matrix[i] = [0,1]
for i,x in enumerate(range(n)):
    T_matrix[i+n] = [1,0]

X_matrix = np.empty((n*2,3))


for i in range(n):
    X_matrix[i]=np.array([1,red_point[0][i],red_point[1][i]])
for i in range(n):
    X_matrix[i+n]=np.array([1,blue_point[0][i],blue_point[1][i]])


mat =np.matmul(T_matrix.T,(np.linalg.pinv(X_matrix)).T)
(a,b,c) = (mat[0][0],mat[0][1],mat[0][2])
(d,e,f) = (mat[1][0],mat[1][1],mat[1][2])
a = a-d
b = b-e
c = c-f
# print(a,b,c)
# print('T:\n',T_matrix)
# print('X:\n',X_matrix)
# print('psudo:\n',np.linalg.pinv(X_matrix))
# print('weight:\n',mat)
xx = np.linspace(-3.5, 5.5, 100)
yy = [-b*x/c-a/c for x in xx]
plt.plot(xx, yy , 'b', alpha=0.6, label='line')
plt.show()