import pandas as pd
import time

fname = './data/score.csv'
score = pd.read_csv(fname, encoding='cp949')

print()
print(score)

time.sleep(1)
print(score.loc[3])
print()
print(score[score['dept'] == 103])
print()

print(score['kor'].max())
print(score['kor'].min())

print('국어최대값 = ', (score.kor).max())
print('국어최소값 = ', (score.kor).min())

print(score[(score.dept) == 102])

print()
print('-' * 70)

time.sleep(1)
print(score)
print()

# print(score)
kor = score['eng']
kor = score['kor']
print()


kor = score.kor
eng = score['eng']
mat = score.mat
hap = kor + eng + mat
avg = round(hap/3, 2)
score.insert(5, ['hap'], hap, True)
score.insert(6, ['avg'], avg, True)
# 임시적으로 넣을 수 있다 .
print(score)


print()
