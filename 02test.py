import numpy as np

print()

a = np.array([1, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])

print(np.zeros([3,5]))

print(np.ones([3,5]))


print('-'*50)
# 5행 20열로 0부터 99까지 발생시킴 
x = np.arange(100).reshape(5,20)
print(x)
np.random.shuffle(x)
# 섞음 
print(x)

