# 문자열 포맷팅
a = "I'm so happy {0} you.".format('to')

print(a)

name = 'lemotem'
login_str = '{0}님 로그인 중'.format(name)


# 문자열 포맷팅 방법
print(login_str)

print('{0}, {1}, {2}'.format('하나', 2, True))
print (f"{'하나'}, {2}, {True}")
print (f"{'하나'}, {2}, {login_str}")

# 소수점 표현
PI = 3.14159268
print('{0:0.2f}'.format(PI))
print(f'{PI:0.3f}')

full_name = 'lemotem'
print(full_name.split()) # 문자열을 ''잘라서 리스트로 만듦
print(sp_names)
print(sp_names[0])

greeting = 'Hello, Wolrd'
words = greeting.split(',') #문자열을 , 로 잘라서 리스트로
print(words)

hi = '     Hello~      '
print(hi,lstrip())       # 오라클 LTRIM()
print(hi.rstrip())       # RTRIM
print(hi.strip())        # TRIM
print(words[1].strip())

# 문자열 특정 단어, 문자열 값 변경
print(full_name.replace('lemotem', 'Ashley'))

# 리스트 연산 (숫자일 경우)
arr = [1, 2, 3, 4, 5]

print(arr[3] + arr[0]) #arr에 리스트에 3번째 자리 값과 0번째 자리에 있는 값의 합 3+1== 4

# 리스트 연산 (문자일 경우)
arr = ['1', 2, 3, '4', 5]

print(arr[3] + arr[0])  #arr에 리스트에 3번째 자리의 '문자' 값과 0번째 자리에 있는 '문자' 값의 합  41

#
print(arr[4] + arr[2]) # 그냥 더하기 ==8 
print(arr[3] + arr[0]) # '4' 글자와 '1' 글자를 합쳐라
print(arr[3] * arr[1]) # '4' 글자를 3번 반복 출력

# 이중 리스트
arr2 = [1, 2, 3.14, ['Hi', 'My', 'Friends']]
print(arr2[2])
print(arr2[3][1]) #My
print(arr2[3][1][0]) #y

arr3 = arr + arr2
print(arr3)

#우선순위 연산자에 () 입력

