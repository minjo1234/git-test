# 전치행렬 transpose matrix 매트릭스
import numpy as np

z = np.array([[1, 2], [4, 5]])

print(z)
print()
print(z.T)
print()
# print z로 출력할경우에는 행과 열이 원래대로 출력이 되는데 반대의 경우 행과 열이 반대로 출력된다
# z.T 행과 열을 반대로 출력

print(np.transpose(z))

# np.transpose(z) = z.T

msg = '''
    동해물과 백두산이 마르고 닳도록
    하느님이 보우하사 우리나라 만세
    무궁화 삼천리 화려강산
    대한사람 대한으로 길이 보전하세 . 
'''

print(msg)
# ''' ''' 을 이용하여 text 형식으로 출력이 가능하다 .
