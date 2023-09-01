import pandas as pd
import time
fname = './data/emp.csv'
emp = pd.read_csv(fname, encoding='utf-8')

time.sleep(0.5)
print(emp.iloc[2:5, 1:3])  # 행과 열을 등록해서 2행부터 4행까지 1열부터 3열까지 출력하도록 했다 .

print(emp.loc[3])
print(emp.loc[3])
print(emp.loc[2:, ['Name']])
# 에러 pring(emo.loc(3)) loc[숫자문자접근 5번째까지]  iloc [숫자로만 접근]
# 에러 Print(emp.loc(3))
# loc 는 문자숫자둘다가능 iloc는 숫자만 가능하다 .
