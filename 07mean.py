# 07mean.py
import numpy as np

jumsu = [175, 177, 179, 181, 183]

time = [1, 2, 3, 4, 5]  # 공부한시간
jumsu = [175, 177, 179, 181, 183]  # 점수

print()
# AI적용다양 고객응대,집값예상,주식예샹,지구온난화 예상

average = 0
hap = 0

for i in range(len(jumsu)):
    average += int(jumsu[i]) / int(len(jumsu))
    hap += (jumsu[i])

print(average)
print(hap)

data = np.array(jumsu)
print('총점', data.sum())
print('평균', data.mean())
# mean으로 평균을 구할 수있다 .

print()
print()
print()
