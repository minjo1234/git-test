# 07mean.py

import numpy as np

jumsu = [175,  177, 179, 181, 183, 185, 187]
avg = np.mean(jumsu)
jumsu_cha = []
print('총점', np.sum(jumsu))
print('평균', np.mean(jumsu))
print()

# 총점,평균.최대,최소,갯수,길이, 중앙값,빈도수
# 편차

print()
print('-' * 50)
jumsu_cha = []

for k in jumsu:
    print('편차', k-avg)
    ret = k-avg
    jumsu_cha.append(ret)

print(jumsu_cha)

for k in jumsu:
    ret = k-avg
    print(f'편차 {k}-{avg}={ret}')

# f 를 사용하면 {} 변수를 사용할 수 있다 .
