import pandas as pd
import time
fname = './data/emp.csv'
emp = pd.read_csv(fname, encoding='utf-8')

time.sleep(0.5)
print(emp.iloc[2:5, 1:3])  # 행과 열을 등록해서 2행부터 4행까지 1열부터 3열까지 출력하도록 했다 .

print(emp.loc[3])
