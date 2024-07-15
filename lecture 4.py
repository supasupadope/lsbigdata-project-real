#수학함수

import math as m

x=4
m.sqrt(x)

m.exp(5)

m.factorial(5)

m.log(10, 10)

m.sin(m.radians(90))
m.cos(m.radians(180))
m.tan(m.radians(45))

import math as m

def normal_pdf(x, mu, sigma)
    sqrt_two_pi = m.sqrt( 2 * m.pi)
    factor = 1 / (sigma * sqrt_two_pi)
    return factor * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def my_normal_pdf(x, mu, sigma):
    part_1 = (sigma * m.sqrt(2 * m.pi))**-1
    part_2 = m.exp(-(x-mu**2) / (2*sigma**2))
    return part_1 * part_2
  
my_normal_pdf(3, 3, 1)

def my_f(x, y, z)
    return (x**2 + m.sqrt(y) + m.sin(z)) * (m.exp(x))
    
my_f(2, 9, m.pi/2)

def my_g(x):
  return m.cos(x) + m.sin(x) * m.exp(x)

!pip install numpy #numpy 설치

# 벡터 생성하기 예제
a = np.array([1, 2, 3, 4, 5]) # 숫자형 벡터 생성
b = np.array(["apple", "banana", "orange"]) # 문자형 벡터 생성
c = np.array([True, False, True, True]) # 논리형 벡터 생성
print("Numeric Vector:", a)
print("String Vector:", b)
print("Boolean Vector:", c) #논리형 벡터 

a
type(a)
a[3]
a[2:]
#numpy를 인덱싱해도 numpy array로 반환
a[1:4]

# 빈 배열 생성
x = np.empty(3)
x
print("빈 벡터 생성하기:", x)
# 배열 채우기
x[0] = 1
x[1] = 2
x[2] = 3
print("채워진 벡터:", x)

#배열 생성

vec1=np.array([1, 2, 3, 4, 5])
vec2=np.arange(10)
vec3=np.arange(1, 101)
vec4=np.arange(1, 101, 0.5) #시작, 끝, 간격
vec5=np.arange(1, 100.5, 0.5) #시작, 끝, 간격

vec1
vec2
vec3
vec4
vec5

l_space1 = np.linspace(0, 1, 5) #0부터 1까지 5개가 나오게 동일한 간격
l_space2 = np.linspace(0, 100, 100)
l_space3 = np.linspace(0, 1, 5, endpoint=False)
#끝값 제외

l_space1
l_space2
l_space3

import numpy as np
    
#repeat 
np.repeat(3, 5)

vec1 = np.arange(5)
vec1
np.repeat(vec1, 5)

vec2 = np.arange(0, -100, -1)
vec2

vec3 = np.linspace(-100, 0, 101)
vec3

vec4=np.arange(0, -100, -1)
vec5=-np.arange(0,100)
vec5

#repeat vs tile
vec1=np.arange(5)
np.repeat(vec1,3)
np.tile(vec1,3)

vec1 *2 #벡터 사칙연산
vec1 +1
vec1 +=1
vec1
vec1 *=2
vec1

vec1 = np.array([1,2,3,4])
vec1 + vec1

max(vec1)
sum(vec1)
sum(vec1 *2)

#35672 이하 홀수들의 합은?

vec1 = np.arange(1, 35672, 2)
vec1
sum(vec1)
np.arange(1, 35672, 2).sum() #뒤에 붙혀서도 가능

#넘파이 벡터 길이 재는 방법

import numpy as np

a = np.array([1,2,3,4,5])
len(a)
a.shape #튜플 하나 입력할 때도 쉼표 

[[1, 2, 3], [4, 5, 6]] #list in list
# 리스트 안의 요소는 두개, 
# 그 안의 리스트 안의 요소는 세개
b = np.array([[1, 2, 3], [4, 5, 6]])
b

length = len(b) # 첫 번째 차원의 길이 2
shape = b.shape # 각 차원의 크기 (2,3)
size = b.size # 전체 요소의 개수 6

a=np.array([1,2])
a=np.array([5,6,7,8])
b=np.array([1,2,3,4])
a+b

shape = a.shape
shape = b.shape
#행렬처럼 차원이 같아야 계산 가능.

#타일로 가능 
np.tile(a, 2) + b
np.repeat(a, 2) + b

#브로드캐스팅 
a = np.array([1.0, 2.0, 3.0])
b = 2.0
a * b
a.shape
b.shape

#하나는 shape이 존재하고 다른 하나는 존재하지 
#않을 때 브로드캐스팅이 된다??

# 길이가 다른 두 벡터
a = np.array([1, 2, 3, 4])
b = np.array([1, 2])
print("a의 shape:", a.shape)
print("b의 shape:", b.shape)

# b 배열을 반복 확장하여 a의 길이에 맞춤
b_repeated = np.tile(b, 2)
print("반복된 b 배열:", b_repeated)
# 브로드캐스팅을 사용한 배열 덧셈
result = a + b_repeated
print("브로드캐스팅 결과:", result)




a * b

b == 3 #3이 포함된 부분만 True
       #각각 부분에 다 비교연산 
       
#35672 보다 작은 수 중에서 7로 나눠서
#나머지가 3인 숫자들의 개수는?

a=np.arange(1, 35673) 
a
a%7 == 3
sum(a%7 == 3) #True는 1이니까 

sum((np.arange(1, 35672)) %7 == 3) #똑같음

import numpy as np
# 2차원 배열 생성
matrix = np.array([[ 0.0, 0.0, 0.0],
[10.0, 10.0, 10.0],
[20.0, 20.0, 20.0],
[30.0, 30.0, 30.0]])

matrix.shape
# 1차원 배열 생성
vector = np.array([1.0, 2.0, 3.0])
vector = np.array([1.0, 2.0, 3.0, 4.0])
vector.shape

# 브로드캐스팅을 이용한 배열 덧셈
result = matrix + vector
print("브로드캐스팅 결과:\n", result)
# 4 x 3 행렬에 1 x 4 벡터는 계산이 안 됨
# 1 x 4를 4 x 1 로 바꿔서 계산

vector = np.array([1.0, 2.0, 3.0, 4.0]).reshape(4, 1)
# 브로드캐스팅을 이용한 배열 덧셈
result = matrix + vector
print("브로드캐스팅 결과:\n", result)

## 각각의 행이나 열이 맞아야 계산이 되는듯?
#ex) 4 x 3 이랑 4 x 1,  4 x 3 이랑 1 x 3 
#(3,) = 1 x 3이랑 같음

