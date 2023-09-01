import numpy as np
#13unique.py

a = np.array([5,4,3,1,2,3,4,3,3,3,1,2,1,2,5,1,2,3,1,2,2,1,3])
print(a)
print(np.unique(a)) #유니크=자동소트
print()

print(np.zeros(5))  #사진을보고 얼굴검출, 그림맞추기
print()
b = np.array([ 0,0,0,7,8,1,0,0,0,9,6,0,0,0,0,0])
print(np.trim_zeros(b))
print(np.trim_zeros(b, trim='f'))
print(np.trim_zeros(b, trim='b'))
print()

import time
time.sleep(1)
data = np.arange(10)
print(data)
np.random.shuffle(data)
print(data)
print()
print('permutation()')
time.sleep(1)
print(np.random.permutation(10)) #permutation=shuffle+arange()






# numpy를 파일로 다운받아서도 사용할 수 있다 . 