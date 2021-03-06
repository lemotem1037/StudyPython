# for문 - for 변수 in list: 에서 list는 열거된 값

arr = [1,2,3,4,5,6,7,8,9,10] # 1 - 10까지 더한 값 구하기
result = 0

for x in arr:
    result = result + x

print('배열의 합 = ', result)


# range tkdyd (1부터 100까지는 101)
arr = [1,2,3,4,5,6,7,8,9,10]
result = 0

for x in range(1, 101):
    result = result + x

print('배열의 합 = ', result)


arr2 = ('me', 'mt', 'frinend', 'han')

for x in arr2:                 #for 변수 in arr2:
    print(f'{x:>10}')          #print(f'{변수}') 변수:>10은 10번째 자리에 맞춰줌


for x in arr2:                 #for 변수 in arr2:
    print(f'{x * 2}')          #print(f'{변수}') 변수*2 두번씩 출력


#드래기 하고 편집 - 주석 블럭 주석처리가능
# 파이썬 한줄 주석
# ''' 다중문자열 == 여러줄 주석과 같다


## 1-10까지 짝수 구분하기
for num in range(1, 11):      # n+1
    if (num % 2) == 0:
        print(f'{num}는 짝수입니다.')
    else:
        print(f'{num}는 홀수입니다.')



for num in range(1, 11, 2):      # 시작 숫자, 끝숫자 n+1, 2씩 증가하라 규칙생성. 짝수를 원하면 1부터 시작
    if (num % 2) == 0:
        print(f'{num}는 짝수입니다.')
    else:
        print(f'{num}는 홀수입니다.')


# for 문 내에서 사용하는 continue, break(탈출)
values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

num = 0
for item in values:
    num +=1                 # 줄여쓸 수 있음 num = num + 1
    if (num % 2) == 0 :     # ???? 질문하기 0에 1을 추가된 상채에서 1을 2로 나눌 때 0, 2로 나눔 짝수 닶이 나오면 탈출
            break           # 반복문 탈출
    
    else:
        print(f'{num}번 수는 {item}입니다.')


# for 문 내에서 사용하는 continue
values = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

num = 0
for item in values:
    num +=1                 # 줄여쓸 수 있음 num = num + 1
    if (num % 2) == 0 :     # ???? 질문하기 0에 1을 추가된 상채에서 1을 2로 나눌 때 0, 2로 나눔 짝수 닶이 나오면 탈출
            continue        # if문 조건만 패스 다음 값 진행
    
    else:
        print(f'{num}번 수는 {item}입니다.')





