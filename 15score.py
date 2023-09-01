import pandas as pd
import time

fname = './data/score.csv'
score = pd.read_csv(fname, encoding='cp949')
print(score)

print()
print(score)

time.sleep(1)
print(score.loc[3])
print()
print(score[score['dept'] == 103])
print()
