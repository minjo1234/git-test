import time
import matplotlib.pyplot as plt

from matplotlib import font_manager
from matplotlib import rc
import numpy as np

import matplotlib as mpl

mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False
# 점 그래프로 나타낸다

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # 추가해줍니다.
time.sleep(1)
labels = ['푸바오', '일바우', '길동', '영희']
sizes = [0.15, 0.1, 0.15, 0.05]
plt.scatter(labels, sizes, s=90, c='red', marker='d')
plt.title('scatter test 그래프')
plt.show()

# 09 graphi.py
time.sleep(1)
name = ['푸바오 ', '길동이 ', '둘리', '커즌스']
data = [40, 60, 86, 35]
plt.pie(data, labels=name, autopct='%0.1f%%')
plt.savefig('./data/길동.png')
plt.legend(name)  # legend = 범례
plt.show()

# 100퍼센트 원형 그래프
