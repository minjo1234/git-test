import matplotlib as mpl
import pandas as pd
import time

import matplotlib.pyplot as plt
import numpy as np

table = pd.DataFrame(
    {
        'weight': [80.0, 76.0, 72.0, 68.0, 64.0,  60.0],
        'height': [170, 210, 160, 180, 190, 175],
        'gender': ['f', 'm', 'm', 'f', 'm', 'f']
    }
)

print(table)
print()
print(table.sort_values(by='weight', ignore_index=True))
# groupby 로 인해서 그룹으로 묶을 수 있다 .
t_group = table.groupby('gender')
for k, value in t_group:
    print(k, ':', value)


mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False
