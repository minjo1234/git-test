import numpy as np


x = [5 ,7 ,3 ]
y = [2 , 9 ,4]

# 실행중에러발생 print(x,y) 리스트 

print(y*5)
print('09-01-금요일')
print()

a = np.array(x)
b = np.array(y)
print(a*b)
print()
print(b*5)
print()

print()
print('')
print(np.ones([3,5]))
a
print(np.zeros((3,5)))
print()

# zeros and ones 는 매개인자를 하나만 받기 때문에 두 개의 인자또는 리스트를 넣을경우 한 번더 감싸줘야한다 . 
data = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(data)

print(data)
