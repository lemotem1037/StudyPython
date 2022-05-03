# 구구단 프로그램
#2X1 =2 ... 2X9 =18 xxy = xy
#3X1 =2 ... 3X9 =27
#           9X9 =81

# 2단만 출력시 (2, 3)

# 단 들여쓰기X 한줄로 출력
print('---구구단 프로그램---')
for x in range (2, 10):     # range 2부터 9까지 
    for y in range (1,10):  # 1부터 9까지
        print(f'{x}x{y} = {x*y:2d}', end= ' ') # d== 정수,  end= ' ' 공백

#한단으로
print('---구구단 프로그램---')
for x in range (2, 10):     # range 2부터 9까지 
    for y in range (1,10):  # range 1부터 9까지
        print(f' {x}x{y} = {x*y:2d}', end= ' ')
    print()                 # 단마다 줄맞추기   
  

  print('---구구단 프로그램---')
for x in range (2, 10):     # range 2부터 9까지 
    print(f'{x}단 시작')    # 단마다 출력추가
    for y in range (1,10):  # range 1부터 9까지
        print(f' {x}x{y} = {x*y:2d}', end= ' ')
    print()                 # 단마다 줄맞추기   