import matplotlib
import matplotlib.pyplot as plt

from matplotlib import font_manager
from matplotlib import rc
import numpy as np

import matplotlib as mpl

mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # 추가해줍니다.


labels = ['푸바오', '일바우', '길동', '영희']
sizes = [40, 60, 90, 35]
# plt.plot(labels, sizes)
# plt.title('우와 차트당 ')
# plt.show()  # 반드시 기술
# 그래프로 보여줌

# x = range(10)
# y = np.random.randint(10, 100, 10)
# plt.bar(x, y, width=0.9, color='red')
# plt.title('bar test')
# plt.show()
# 표로 보여줌
# 난수를 발생해서 매번 다르다 .

z = np.random.randn(10000)
print(z)
plt.hist(z, bins=20, color='hotpink')
plt.show()
print()
