import numpy as np

list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a.shape)  # (4, )

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)  # (2, 3)
print(b[0, 0])  # 1


# what shape ????????
# shapes는 배열을 2차원 배열의 형태로 보고 index의 크기를 출력한다
# ex = np.array(1,2,3,4) -> (4,0)  ex= np.array([1,2,3,4] , [1,2,3,4]) -> (2,4)
# 2차원배열의 형식을 다 가지고 있다 .
