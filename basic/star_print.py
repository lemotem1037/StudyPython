# * 별 찍기 (역삼각형 반)
for x in range(1, 6):      # 5(n+1)까지 출력
    for y in range(x, 6):
        print('*', end='')  #print 뒤에 end 쓰면 
    print('')

#print 뒤에 end 쓰면 다음 줄이 아닌 붙여쓰기가 됨
print('Hello', end= ' ')  # 띄어쓰기 공백 가능
print('World')

