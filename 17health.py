import pandas as pd
import numpy as np
import time

fname = './data/health.csv'
health = pd.read_csv(fname, encoding='cp949')
# print(health.head())
# 위의 rownum에서 5개를 출력해준다
print()
# print(health.tail())
# 아래의 rownum에서 5개를 출력해준다 .
print(health)
print()
print('-'*70)

time.sleep(1)
print('결측값null 갯수', health.isnull().sum())
print('결측값null 갯수', health.isnull())
# null값을 확인해준다 .
print('결측값duplicated', health.duplicated().sum())
# 결측값이 존재하지않으므로 오류발생
print(health.shape)
print(health)
print(health.tail())  # 하위 행번호 1162
data = health[health['WEIGHT'] == 60].index
print('결과값 = ', data)
print(data)

remove = health.drop(data)
health.reset_index(drop=True, inplace=True)
print(health)
health.dropna(inplace=True)
print(health)
# remove = health.drop(data)


fname = './data/health.csv'
# 경로입력후에 지원진걸  to_csv로 반영한다 .
remove.to_csv(fname)
print(fname, '파일 저장했습니다 .')

print(health.tail())
data = health[health['WEIGHT'] == 50].index
remove = health.drop(data)
print(health)
print(remove)

remove.to_csv(fname, index=False)
print()
print('-'*70)
