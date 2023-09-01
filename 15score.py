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
kor = score.keywords()
kor = score['eng']
kor = score['kor']
print()
