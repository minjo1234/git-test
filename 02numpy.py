import numpy as np
import random

# 1~45숫자난수 발생


num = random.randint(1, 45)
print('난수발생', num)

num = np.random.randint(1, 45)
print('넘피발생', num)

print()
c = np.random.rand(15).reshape(3, 5)
print(c)
# reshape -> 3,5 3행 5열


c = np.random.rand(20).reshape(4, 5)
print(c)
# rand => shape의 사이즈를 나타낸다  rand = reshape(x,y)
# reshape(x,y) => shape의 행과 열을 나타낸다 .
d = np.random.rand(30).reshape(5, 6)
z = np.random.randn(3, 5)  # 음수실수 ~ 양수
print(z)


# rand 양수실수 randn 음수실수 ~ 양수
# shape 행과 열을 확인 reshape 행과 열을 만들어준다 .

print('-'*70)
print()
