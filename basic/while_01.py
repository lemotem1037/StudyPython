# while 문
hit = 0   #ghit이 100보다 작을 때

while(hit < 100):
    hit +=1

    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 10:
        print('나무가 넘어갑니다!!')
        break
    else:
        print('나무가 아직 안 넘어갔네요.')

print('나무찍기 완료!!')



# 무한 루프
num = 1

while True:
    print(f'{num}')
    num += 1


# 무한 루프
num = 0

while True:
    print('''처리번호를 입력하세요.
1. 회원 입력
2. 회원 검색
3. 회원 수정
4. 회원 삭제
5. 종료
입력번호 : ''')
num = int(input())    #키보드로 입력 받은 수를 num 할당

if num ==1:
    print('회원정보입력')
elif num == 2: # 1은 아니고 2면 else if
    print('회원검색')
elif num == 3: #1,2가 아닌 3이면
    print('회원수정')
elif num == 4: #4라면
    print('회원삭제')
elif num == 5:
    print('프로그램 종료')
    break
else:
    print('잘못 입력했습니다.')
    continue

