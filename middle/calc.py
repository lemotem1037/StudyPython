# 계산기 프로그램
'''
함수선언 구조
def 함수명(매개변수):
    처리로직1
    처리로직2
'''

# 함수선언 먼저하기
from multiprocessing.sharedctypes import Value


def plus(a,b):
    res = a + b
    return res

def minus(a,b):
    res = a - b
    return res

def multiple(a,b):
    res = a * b

def divide(a,b):
    # if b == 0:
    #     return 0

    res = a / b
    return res

def adds(*args): #pramaenter. arguments
    res = 0
    for i in args:
        res += i
    
    return res
    
def mul_and_div(a,b):
     res = a + b
     res2 = a / b
     return (a * b, a / b)  # 튜플 사용 가능

def add_and_minus_and_mul_and_div(a, b):
    return(a+b, a-b, a*b, a/b)


print(adds(1,2,3,4,5,6,7,8,9,10))
print(adds(1,2,3))
print(adds(5,7,9,11,455))

(mul_val, div_val) = mul_add_div(16,2)
print(mul_val)
print(div_val)
print(mul_add_div(16,2))

print(add_and_minus_and_mul_and_div(17, 5))



print('계산기')    #ctrl+/ 주석처리
num = 0
x = 0
y = 0
Val = 0

while True:
    print(''' 메뉴
1. 덧셈
2. 뺄셈
3. 곱셈
4. 나눗셈
5. 종료
숫자입력 : ''', end='')
    num = int(input())  #숫자

    if num == 1:
        print('덧셈')
        print('첫번째 값 : ', end=' ')
        x = int(input())    # input 2라는 숫자를 받아서, int 정수로 바꿔서, X값을 도출
        print('두번째 값 : ',end=' ' )
        y = int(input())
        val = plus(x, y)   # 함수 호출된 곳으로 점프했다가 현재위치로 돌아옴 
        print(f'{x}+{y}={val}')
    elif num == 2:
        print('뺼셈')
    elif num == 3:
        print('곱셈')
    elif num == 4:
        print('나눗셈')
    elif num == 5:
        break
    else:
        continue

elif num == 2:
    print('뺄셈')
    print('첫번째 값 : ', end=' ')
    x = int(input())    # input 2라는 숫자를 받아서, int 정수로 바꿔서, X값을 도출
    print('두번째 값 : ',end=' ' )
    y = int(input())
    val = plus(x, y)   # 함수 호출된 곳으로 점프했다가 현재위치로 돌아옴 
    print(f'{x}+{y}={val}')
elif num == 2:
    print('뺼셈')
    print('첫번째 값 : ', end=' ')
    x = int(input())    # input 2라는 숫자를 받아서, int 정수로 바꿔서, X값을 도출
    print('두번째 값 : ',end=' ' )
    y = int(input())
    val = plus(x, y)   # 함수 호출된 곳으로 점프했다가 현재위치로 돌아옴 
    print(f'{x}-{y}={val}')
elif num == 3:
    print('곱셈')
    print('첫번째 값 : ', end=' ')
    x = int(input())    # input 2라는 숫자를 받아서, int 정수로 바꿔서, X값을 도출
    print('두번째 값 : ',end=' ' )
    y = int(input())
    val = plus(x, y)   # 함수 호출된 곳으로 점프했다가 현재위치로 돌아옴 
    print(f'{x}*{y}={val}')
elif num == 4:
    print('나눗셈')
    print('첫번째 값 : ', end=' ')
    x = int(input())    # input 2라는 숫자를 받아서, int 정수로 바꿔서, X값을 도출
    print('두번째 값 : ',end=' ' )
    y = int(input())
    val = plus(x, y)   # 함수 호출된 곳으로 점프했다가 현재위치로 돌아옴 
    print(f'{x}÷{y}={val}')

