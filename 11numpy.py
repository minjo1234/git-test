import numpy as np

b = np.array([[1, 2], [3, 4]])
a = np.array([[5, 6], [7, 8]])
print()

print(np.vstack((a, b)))
# 하나로 합쳐줄수있다
print(np.hstack((a, b)))
print()
print(np.concatenate([b, a], axis=0))
# 동일하게 하나로 합치는 것이 가능하다 .
print()
print(np.concatenate([a, b], axis=1))
# 리녹스 cat = concatenate


# vsstack 행과열을 그대로
# hstack 행과열을 반대로
# axis = 0 means 원래대로
# axis = 1 행과 열을 반대로
a = np.array([1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(a)
print(np.unique(a))
