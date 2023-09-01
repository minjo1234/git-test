import numpy as np

x = [5 , 7 , 3]
y = [2, 9 ,4]

# 예측알고리즘 기본 
# LR=Linear Regression 선형회귀

x = [2,4,6,8,10]        # 시간 총합계 30 /5 평균 6시간 
y = [81,93,91,97,98]    # 점수 총합계 평균 92점

print(np.sum(x))
print(np.average(x))

print(np.sum(y))
print(np.average(x))

print('시간총점' , np.sum(x) , '시간의 평균' , np.mean(x))  
print('점수총점', np.sum(y), '점수평균', np.mean(y))
print()

result = 0 
# 공부한 시간 6시간 - 본인이 공부한시간 차이후 공부한시간차이 합계 
for k in x:
    print(k, end='')
    result =  k - np.mean(x)
    print('평균과의 시간차' , result)

print()