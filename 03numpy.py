import numpy as np

# zeros(),ones(), diag()

x = np.zeros(3)

print(x)
y = np.ones([3, 5])

print(x)
print()
print(y)

data = [5, 3, 7]
z = np.array(data)
print(z)
print()

z = np.array([[5, 3, 7]])
print(z)
# zeros는 매개인자가 필요하다.
# zeros의 매개인자는 1개이며 -> 기본인자값 0
# zeros로 1차원 배열을 생성하는 것이 가능하다 .
# ones 로 2차원개열을 생성하는것이 가능하다  -> 기본인자값 1

z = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(z)  # 행이 3개이고 열이 3개이다
print(z.shape)  # -> 3,3

print()
diag = np.diag(z)

print(diag)

# 2차원 배열을 1차원 배열로 만들어주는 함수이다
# z의 대각의 값인 1,5,9 만 출력해줬다 .

diag = np.diag([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(diag)


print(np.diag([1, 2, 3, 4, 5, 6]))
'''
[[1 0 0 0 0 0]
 [0 2 0 0 0 0]
 [0 0 3 0 0 0]
 [0 0 0 4 0 0]
 [0 0 0 0 5 0]
 [0 0 0 0 0 6]]
'''

# 1차원배열일 경우에는 2차원배열로 만들어준다
print()
print(np.diag(([1, 2, 3], [4, 5, 6], [7, 8, 9,])))  # [1 5 9]
print()

# diag 1차원배열을 2차원배열로
# diag 2차원배열을 1차원배열로 변경해주는 기능을한다
