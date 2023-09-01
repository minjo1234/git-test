import numpy as np 

x = np.arange(100).reshape(5,20)
np.random.shuffle(x)
print(x)
print('- ' * 50)
print()

path = './data/test0901'  #확장자는 npy
np.save(path, x)
print(path , ' 파일저장성공')
print('2초후에 test0901.npy 파일열기처리합니다')

import time
time.sleep(1)
print(np.load('./data/test0901.npy'))



