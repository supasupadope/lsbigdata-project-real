import numpy as np
# 벡터 슬라이싱 예제, a를 랜덤하게 채움
np.random.seed(42)   
np.random.seed(2024)  #다른 사람도 똑같이 나옴

a = np.random.randint(1, 21, 10)
#함수에 f1 누르면 함수 설명, 
#1 ~ 21 사이에서 랜덤 10개 추출

print(a)
# 두 번째 값 추출
print(a[1])

a[2:5]
a[-1]
a[-2] # 맨 끝에서 두번째
a[::2] # 두칸씩 띄움
a[:] # 다 뽑음
a[1:6:2] # index 1부터 5까지 2칸 간격으로


#1에서부터 1000사이 3의 배수의 합은?
a = np.arange(1, 1001)
a
b = a[2:1000:3]
b
sum(b)

x =np.arange(0,1001)
sum(x[::3])


a = np.random.randint(1, 21, 10)
# 첫 번째, 세 번째, 다섯 번째 값 추출
print(a[[0, 2, 4]])

# 두 번째 값 제외하고 추출
print(np.delete(a, 1))  #인덱스 1을 제외

np.delete(a, [1,3]) ##??

a > 3
b = a[a > 3]  #True인 애들만 뽑아온다.

print(b)

np.random.seed(2024)
a = np.random.randint(1, 10000, 10)
#a[조건을 만족하는 논리형 벡터]

a[ (a > 2000) & (a <5000)]

a > 2000  # 얜 true/false로 나옴
a < 5000

#둘이 겹치는 애들만 숫자 형태로 반환
# &는 true true 일때 true


!pip install pydataset
import pydataset

df=pydataset.data('mtcars')
np_df = np.array(df['mpg']) #mpg만 선택

#15이상 25이하인 차가 몇대있나요?

a = np_df
a[(a >= 15) &(a <= 25)]
len(a[(a >= 15) &(a <= 25)])

# 평균 mpg 이상의 자동차 대수는?
sum(np_df >= np.mean(np_df))

# 15보다 작거나 22이 이상인 데이터 개수는?
len(a[(a >= 22) | (a < 15)])  # | = or 

np.random.seed(2024)
a = np.random.randint(1, 10000, 5)
a
b = np.array(["A", "B", "C", "F", "W"])
a[ (a > 2000) & (a <5000)]
b[ (a > 2000) & (a <5000)] 

# a랑 b랑 길이가 똑같으니까
# 'A'는 a의 첫 원소인 7817이랑 대응한다고 보는

row_names = np.array(df.index)
model_names = np.array(df.index)
model_names[(np_df >= 15) & (np_df <= 20)]

#연비 높은 애들
model_names[(np_df >= np.mean(np_df))]

#연비 낮은 애들
model_names[(np_df < np.mean(np_df))]

a[ a > 3000] = 3000 # 3000보다 큰놈은 3000
a

np.random.seed(2024)
a = np.random.randint(1, 100, 10)
a < 50
np.where(a < 50) #True인 인덱스 자리

np.random.seed(2024)
a = np.random.randint(1, 26346, 1000)
a

#처음으로 22000보다 큰 숫자가 나왔을 때,
#숫자 위치와 숫자는?

x = np.where(a > 22000)
x
type(x)
my_index = x[0][0]
a[my_index]


#처음으로 24000보다 큰 숫자가 나왔을 때,

x = np.where(a > 24000)
x
my_index = x[0][0]
a[my_index]

#10000보다 큰 숫자가 나왔을 때 50번째 위치와 숫자

x = np.where(a > 10000)
my_index = x[0][49]
a[my_index]

# 500보다 작은 숫자들 중 가장 마지막 숫자

x = np.where( a < 500)
x
my_index = x[0][-1]  #뒤에서 첫번째
a[my_index]

#960번째의 391

#nan = not a number

import numpy as np
a = np.array([20, np.nan, 13, 24, 309])
np.isnan(a)  # true/false로 반환 
a 
a + 3 #nan은 안 더해짐

np.mean(a)
np.nanmean(a) #nan 무시한 평균
np.nan_to_num(a) #nan을 0으로 변환
np.nan_to_num(a, nan = 0)

False
a = None
b = np.nan
b
a
b + 1
a + 1

a_filtered = a[~np.isnan(a)] #true false 전환
a_filtered 

import numpy as np
str_vec = np.array(["사과", "배", "수박", "참외"])
str_vec
str_vec[[0, 2]]

mix_vec = np.array(["사과", 12, "수박", "참외"], dtype=str)
#리스트는 데이터 타입 달라도 허용 O
#벡터는 한가지 데이터 타입만 허용 가능
#dype = str은 모든 타입을 문자열로

mix_vec 

combined_vec = np.concatenate((str_vec, mix_vec))
combined_vec = np.concatenate([str_vec, mix_vec])
combined_vec
type(combined_vec)
#()로 묶이고 , 생겨서 tuple
#concatenate를 하면 리스트나 튜플 뭘 넣어도 됨
#둘 다 다룰 수 있다.

np.arange(1, 5)
np.arange(12, 16)
col_stacked = np.column_stack((np.arange(1, 5), np.arange(12, 16)))

col_stacked
row_stacked = np.row_stack((np.arange(1,5), np.arange(12, 16)))
row_stacked


uneven_stacked = np.column_stack((np.arange(1, 5), np.arange(12, 18)))
uneven_stacked

#길이가 다른 벡터
vec1 = np.arange(1, 5)
vec2 = np.arange(12, 18)
vec1 = np.resize(vec1, len(vec2))
vec1
#length를 vec2와 같게 함 1234 ->123412

# 두 벡터를 세로로 쌓기
uneven_stacked = np.column_stack((vec1, vec2))
uneven_stacked
#길이가 다르면 에러가 난다

#vec2가 더 길면 길이가 줄어들음 
vec1 = np.arange(1, 5)
vec2 = np.arange(15, 18)
vec1 = np.resize(vec1, len(vec2))
vec1

#resize 후 가로로 쌓기기
vec1 = np.arange(1, 5)
vec2 = np.arange(12, 18)
vec1 = np.resize(vec1, len(vec2))
vec1
vec2
np.row_stack((vec1, vec2))

#주어진 벡터의 각 요소에 5를 더한 새로운 벡터를 생성하세요.
a = np.array([1, 2, 3, 4, 5])
a
a + 5

#주어진 벡터의 홀수 번째 요소만 추출하여 새로운 벡터를 생성하세요.
a = np.array([12, 21, 35, 48, 5])
a
a[0::2]

#주어진 벡터에서 최대값을 찾으세요.
a = np.array([1, 22, 93, 64, 54])
a
a.max()

#주어진 벡터에서 중복된 값을 제거한 새로운 벡터를 생성하세요.
a = np.array([1, 2, 3, 2, 4, 5, 4, 6])
a
np.unique(a)

#주어진 두 벡터의 요소를 번갈아 가면서 합쳐서 새로운 벡터를 생성하세요.
a = np.array([21, 31, 58])
b = np.array([24, 44, 67])
a
b

combined_vec = np.concatenate((a,b))
sorted_array = np.sort(combined_vec)
sorted_array

#or

x = np.empty(6)
x

# 짝수
x[[1, 3, 5]] = b
# x[1::2] = b랑 같음
x[1::2]

# 홀수
x[[0, 2, 4]] = a
#x[0::2] = a랑 같음
x
