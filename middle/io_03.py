# 세개의 값을 입력받아 두개의 변수에 나눠담기
x, y, z = input('세 단어를 입력하세요(구분자 /) > ').split('/')

print(x)
print(y)
print(z)


# 두개의 값을 입력받아 두개의 변수에 나눠담기
x, y = input('두 수를 입력하세요(구분자 /) > ').split('/')

print(int(x) * int(y))  # int - 정수로 변환(*따로 기재)


#int는 따로 기재해야하지만 map을 이용하여 한꺼번에 작성
x, y = map(int, input('두 수를 입력하세요(구분자 /) > ').split('/'))

print(x * y) 

greeting = "Hello, I\'m a teacher. \"Bye~\" \\ \a"
print(greeting)

