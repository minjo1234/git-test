# 예측알고리즘 LR = Linear Regression 선형회귀
import numpy as np
import matplotlib.pyplot as plt
x = [4,6,8,10]       #시간 총합계 30 /5   평균 6시간
y = [93,91,97,98]   #점수 총합계 460 /5  평균 92점


A = np.vstack( [x,np.ones(len(x))]).T
C = np.vstack([3,4]).T
B = np.hstack([x,np.ones(len(x))]).T
# 여기서 "T"는 배열의 전치(transpose)를 나타내는 속성입니다. "전치"는 배열의 행과 열을 뒤바꾸는 작업을 의미합니다.
# 이어지는 구조를 만들기위해서 작성한것이다 . 원래는 하나씩작성되는데 이어진다 원래는 [2][1]등으로 생성되는데 그 오류를 극복했다 .
# 원래는 1차원이 두개 생겨야 하는데 
# vstack 행과 열을 그대로 추력
# hstack 행과 열을 교차해서 출력한다 .
print(A)
print(C)
print()
print(B)
m,c = np.linalg.lstsq(A,y, rcond=None)[0]
# 최소자승법으로 기울기와 Y절편을 구할 수 있다 
# np.linalg.lstsq(A,y, rcond=None)[0] 로 인해서 m,c의 초기값으로부터의 증가량을 확인하는 것이 가능하다 .

print(m,c)
print()

su = np.polyfit(x,y,1)
print(su)
su = np.polyfit(x,y,2)
print(su)
# 최소자승법을 이용해서 polyfit을 이용하면 차수를 알수있다 
# 1을 넣어주면 함수의 차수를 2를 넣어주면 2차식의 차수를 찾아준다 . 
# 


plt.plot(x,y , 'o' , label ='Orginal Data' , markersize = '10')
plt.plot(x, int(m)*x + c, 'r', label = 'Fitted Data')
plt.legend()
plt.show()

