#연습장

avg = 10
me = 15

print("저는 평균보다 높습니까?", me > avg)

a = True
b = True

print("a and not b는 ", a and not b,"입니다.")

not a
not not a

str1 = 'so'
str2 = 'sleepy'
print(str1 + ' ' + str2)

print((str2 + ' ') * 10)

~3
bin(~3)
bin(-4)
bin(~-4)

a =[1,2,3]
a

b = a
b

a[1] = 4
# 넣으니까 b도 바뀌네
# soft copy 

b
id(a)
id(b)

b = a # a에 있는 주소를 b에 할당. 
      # 그래서 a 바꾸니 b도 바뀜

# deep copy      
a = [1,2,3]
a

b=a[:]
b=a.copy()   #둘 중 하나

a[1] =4
a
b

