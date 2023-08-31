import numpy as np
import math
a = np.empty(5)
print(a)

# empty -> 양의실수형태로 매개인자 만큼 출력한다.

b = np.arange(4)
print(b)
print(type(b))
# 0부터 3까지 바로 출력이 가능하다 -> 리스트형태로 numpy array

c = np.arange(2, 9, 2)
print(c)

d = np.linspace(0, 10, num=5)
print(d)

# 매개인자만큼 발생하는데 num=5  가중치를 숫자사이만큼 가중된다
# ex ->  [ 0.   2.5  5.   7.5 10. ]
e = np.linspace(0, 20, num=5, endpoint=True)
print(e)

# ex -> [ 0.  5. 10. 15. 20.]

x = np.ones(5, dtype=np.int64)
# 1이 출력되는 데 정수타입으로 출력되도록
# ex - > [1 1 1 1 1]
print(x)
print()

x = np.ones(5)
print(x)

# 1이 출력되는데 실수타입으로도 출력이 가능하다.
# ex -> [1. 1. 1. 1. 1.]

arr = np.array([9, 8, 7, 1, 2, 3, 4, 5])
print(arr)
print(np.sort(arr))

print()
data = [9, 1, 5, 3, 7, 2, 4, 6]
# 파이썬 기본의 리스트
print(data)
# 그냥 리스트를 sort하는 것은 불가능한데 np.sort를 하면 한 번에 해결이 가능하다 .
print(sorted(data))
print(np.sort(data))

data = np.array([9, 1, 5, 3, 7, 2, 4, 6])
print(data)
print(np.sort(data))

num = 0

for i in range(len(data)):
    num += data[i]

print(num)


kim = [5, 7, 3]
lee = [2, 9, 4]

# print(kim*lee) 오류발생

print(np.dot(kim, lee))
# 리스트끼리의 연산을 도와준다 .


a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print(a*b)
# 리스트에서 각 자리마다의 곱을 나타내주는것이다 .

c = np.concatenate((a, b))
# 리스트 두 개를 연결해준다 .
print(c)
