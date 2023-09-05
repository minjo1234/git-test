import numpy as np 
import time

# 예측알고리즘  LR=Linear Regression선형회귀
x = [2,4,6,8,10]       #시간 총합계 30 /5   평균 6시간
y = [81,93,91,97,98]   #점수 총합계 460 /5  평균 92점

mean_x=np.mean(x) # 평균구하기 
mean_y=np.mean(y) # 평균구하기 
print('시간평균 =', mean_x , '\t 점수평균 =' , mean_y)  #6.0, 92.0
time.sleep(0.5)

parent = sum([(i - mean_x)**2 for i in x])
children = sum([(x[idx]-mean_x) * (y[idx] - mean_y) for idx, value in enumerate(x)])
w = children / parent
b = mean_y - ( mean_x * w)

print('분자: ', children)  #분자 76
print('분모: ', parent)    #분모 40
print('가중치(w): ', w)    #1.9기울기
print('bias(b): ', b)     #바이어스 80.6
print()

tm = [2,4,6,8,10] 
score = [81,93,91,97,98] 
for t in tm:
  my = t*w+b  #선형회귀공식
  print(score , ' 예상점수 ' , int(my))
  
print('\n08LR선형회귀 구현끝') 
