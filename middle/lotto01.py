# 첫번째 간단한 로또
import random as rnd   # as rnd - 별명 변경

numbers = [i for i in range(1, 46)]  # 1부터 45까지 'i for i in range'

lotto = []  #빈 리스트에 로또 번호 저장

for i in range(6):   # 6번 반복
    lotto.append(rnd.choice(numbers))
    
lotto.sort()     # sort 정렬   
print(lotto) 

