import time
import numpy as np

data = np.arange(10)
print(data)
np.random.shuffle(data)
# shuffle 섞는것이다 .
print(data)
print()
print('permutation()')
time.sleep(1)
print(np.random.permutation(10))
# permutation 랜덤을 하나씩 나오도록 출력해준다 .
