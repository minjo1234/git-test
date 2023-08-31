# 06mean.py
import numpy as np

array_example = np.array(
    [[[0, 1, 2, 3], [3, 4, 5, 6]],
     [[0, 1, 2, 3], [3, 4, 5, 6]],
     [[0, 1, 2, 3], [3, 4, 5, 6]]]
)

print(array_example)
print()

print(np.mean(array_example, axis=0))
print(array_example.ndim)
# 3 배열의 개수를 의미한다. 행을 의미

print()
print(array_example.size)
# index의 크기가 나온다 --> 24
print()
print(array_example.shape)
# (3,2,4)
# 3행 2열씩 4개의 인덱스
# 좀 사용하기 ㅈ같다

print()

