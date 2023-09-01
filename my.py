# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# %matplotlib inline

# from sklearn.linear_model import LinearRegression

# ## 데이터셋 불러오기 % 기초 전처리
# r1 = pd.read_csv('train.csv')
# r1.columns = [ r1.columns[i].lower() for i in ipb(range(len(r1.columns)))]
# t1 = r1.query('yearbuilt >= 1980').reset_index(drop=True)
