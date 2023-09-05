import pandas as pd
import time
fname = './data/emp.csv'
emp = pd.read_csv(fname, encoding='utf-8')
print(emp)

print(emp.pay)
print()
print(emp['pay'])
print()
print(emp['Name'])

print(emp.loc[3])
print()


time.sleep(0.5)
print(emp.loc[2:5])
print(emp.iloc[2:5])
# 2행부터 5열까지 출력하겠다

print(emp.loc[2:, ['Name', 'No', 'pay']])

time.sleep(0.5)
print(emp.loc[2:5, ['Name', 'No', 'pay']])
print()
print(emp.iloc[2:5])  # 5행전까지만 출력된다

print(emp.iloc[2:5, [1, 0, 2]])  # ilo[시작:5행-1] , [행번호숫자로명기]
