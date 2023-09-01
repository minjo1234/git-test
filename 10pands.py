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
