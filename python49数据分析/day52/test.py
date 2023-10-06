import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print('第一个数组：')
print(a)
print('\n')
# a = a.tolist()
# print(a)
a = a.reshape(3,2)
print(a)