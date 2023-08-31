import numpy as np
import time

x = np.array([1, 2, 3, 4, 5, 6])

data = [5, 7, 3]

for k in data:
    print(k*10, end='')

print((data*4), end='')

print(data)
data = np.array(data)


for k in data:
    print(k*10, end='')

print(data*9)
# +


def f(x):
    return x ** 2

# 굳이 list가 아닌 numpy 를 사용하는 이유가 ? -->
# 1. list와 출력형태가다르다  list -> [5, 7, 3] numpy -> [5 7 3]
# 또한 numpy 는 곱해서 출력할경우 숫자의 곱한 값이 나오지만 배열은 요소의 반복이다 .
