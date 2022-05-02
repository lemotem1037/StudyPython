# if문
name = 'lemotem' # = 하나는 값을 할당, ==두개는 같다
grnder = '여'

if name == 'lemotem': 
    if gender == '여':
        print('진료실로 들어갑니다.') #if문 참
        print('의사 선생님께 인사합니다.')
    else:
        print('성별이 다르네요.')

else:
    print('부를 때까지 기다리세요.')  #if문 거짓
    print('궁시렁거립니다.')


# 탭남용X 중첩문
name = 'lemotem'
grnder = '여'


if name == 'lemotem' and grnder == '여':
    print('진료실로 들어갑니다.') #if문 참
    print('의사 선생님께 인사합니다.')

else:
    print('부를 때까지 기다리세요.')  #if문 거짓
    print('궁시렁거립니다.')

num = 10

if num != 9:
    print('9가 아닙니다')
    
else:
    print('9 입니다.')