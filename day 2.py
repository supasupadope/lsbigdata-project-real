# 2장 데이터 타입 이해

x = 15
print(x, "는 ", type(x), "형식입니다.", sep='')
print(x, "는 ", type(x), "형식입니다.", sep=' ')
# sep는 사이에 뭘 넣을지

# 문자형 데이터 예제
a = "Hello, world!"
b = 'python programming'
# 여러 줄 문자열
ml_str = """This is
a multi-line
string"""
print(a, type(a))
print(b, type(b))
print(ml_str, type(ml_str))

# 문자열 결합
greeting = "안녕" + " " + "파이썬!"
print("결합 된 문자열:", greeting)
# 문자열 반복
laugh = "하" * 3
print("반복 문자열:", laugh)

#리스트 데이터타입 

# 리스트 생성 예제
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", [1, 2, 3]]

#숫자, 문자, 리스트 다 들어갈 수 있

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed List:", mixed_list)

normal_list = [fruits[0], numbers[1]]
print(normal_list)

print(type(fruits))
print(type(normal_list))

#튜플 ,수정할 수 없다

# 튜플 생성 예제, 소괄호
a = (10, 20, 30) # a = 10, 20, 30 과 동일
b1 = (10,) #튜플
b2 = (10)  #int
b1
b2
print(type(b1))
print(type(b2))

print("좌표:", a)
print("단원소 튜플:", b1)

# 인덱싱
print("첫번째 좌표:", a[0])
# 슬라이싱
print("마지막 네개 좌표:", a_tp[1:]) # 2, 3, 4, 5
print("처음 세개 좌표:", a_tp[:3])  # 0, 1, 2

print(a_tp[1:3]) # [1], [2]

a_list = [10, 20, 30, 40, 50]
a_tp = (10, 20, 30, 40, 50)
print(a_list[1:4])
print(a_list[0:3])

a_list[1] = 25
a_tp[1] = 25 # 안됨
print(a_list[1])
print(a_list)

print(a_tp[1])

## 사용자 정의 함수

def min_max(numbers):
  return min(numbers), max(numbers)

a=[1,2,3,4,5]
result = min_max(a)
result = min_max((1, 2, 3, 4, 5))
print("Minimum and maximum:", result) 
#리스트 result 넣어도 tuple로 나옴

print(type(result))


# 딕셔너리 생성 예제 #key와 value
# 'key' : value # 중괄호
person = {
'name': 'John',
'age': 30,
'city': 'New York'
}
print("Person:", person)

person = {
  'name' : '고윤하',
  'major': ['piano', 'vocal'], 
  'age' : 37
}

person = {
  'name' : '고윤하',
  'major': ('piano', 'vocal'),
  'age' : 37
}

#value에 숫자, 튜플, 리스트 다 가능

person.get('name') 
person.get('major')[1] # 원하는 거 골라오기

Y_major = person.get('major')
Y_major[0]       # 원하는 거 골라오기 ver.2 (따로 변수)

#집합 #순서 유지 ㄴ

fruits = {'apple', 'banana', 'cherry', 'apple'}
print("Fruits set:", fruits) # 중복 'apple'은 제거됨

# 빈 집합 생성
empty_set = set()
print("Empty set:", empty_set)

empty_set = {'1'}
empty_set = {2}
empty_set = {(3)}       #???
empty_set.add("apple")  #함수 뒤에 . 붙히면 추가 함수 

empty_set.add('apple')
empty_set.add('banana')
empty_set.add('cherry')

empty_set.remove('apple')
empty_set.discard('cherry') #discard는 없는 거 넣어도 오류 ㄴ
empty_set.remove('cherry')

#집합 간 연산
other_fruits = {'berry', 'cherry'}
union_fruits = fruits.union(other_fruits) #합집합
intersection_fruits = fruits.intersection(other_fruits) #교집합 
print("Union of fruits:", union_fruits)
print("Intersection of fruits:", intersection_fruits)

#논리형 데이터 타입 #true, false

# 논리형 데이터 예제
p = True
q = False
print(p, type(p))
print(q, type(q))
print(p + p) # True는 1로, False는 0으로 계산됩니다.

is_active = True
is_greater = 10 > 5 # True 반환
is_equal = (10 == 5) # False 반환
print("Is active:", is_active)
print("Is 10 greater than 5?:", is_greater)
print("Is 10 equal to 5?:", is_equal)

#조건문
a=3
if (a == 2):
  print("a는 2와 같습니다.")
else:
  print("a는 2와 같지 않습니다.")

num = 123
str_num = str(num)
print("문자열:", str_num, type(str_num))
# 문자열형을 숫자형(실수)으로 변환
num_again = float(str_num)
print("숫자형:", num_again, type(num_again))

# 리스트와 튜플 변환
lst = [1, 2, 3]
print("리스트:", lst)
tup = tuple(lst)
print("튜플:", tup)

set_example = {'a', 'b', 'c'}
# 딕셔너리로 변환 시, 일반적으로 집합 요소를 키 또는 값으로 사용
dict_from_set = {key: True for key in set_example}
print("Dictionary from set:", dict_from_set)

#교재 65p 패키지 사용

import seaborn as sns #약어
!pip install seaborn

var = ['a', 'a', 'b', 'c']
var
sns.countplot(x = var)
import matplotlib.pyplot as plt #약어로 쓴거
plt.show()

df = sns.load_dataset('titanic')
sns.countplot(data = df, x = "sex")
sns.countplot(data = df, x = "sex", hue='sex')
plt.clf()  # 초기화
plt.show()

sns.countplot(data = df, x='class')
plt.show()

?sns.countplot #함수 설명
sns.countplot(data = df, x='class', hue ='alive')
sns.countplot(data = df, y='class', hue ='alive')
sns.countplot(data = df, y='embark_town', hue ='alone')
plt.show()

#hue가 뭔데, x y넣을땐 안 그려지는 이유가 먼데 
# countplot 자체가 x y 를 지정하는게 아니라
# 하나만 지정하고, 나머지 하나는 hue로써야.. 

#!pip install scikit-learn
import sklearn.metrics

sklearn.metrics.accuracy_score()

from sklearn import metrics
#metrics.accuracy_score()


import sklearn.metrics as met
# met.accuarcy_score()

a = 1,2,3 (그냥 넣으면 자동 tuple)
