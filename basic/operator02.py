# 문자열 연산 (문자에서는 +랑 * 만 가능)
from locale import currency


first = 'Hello'
second = ' World!'

print(first + second) # 문자연산 + (합치기)
print(first, second)  # 처음에 띄어쓰기를 하거나, print(first, second) 콤마를 찍기

print(first * 3) # 문자열 연산,+,*밖에 없음


# 문자열 길이 내장함수
print(len('한글'))
print(len(first))

# 리스트 연산 -마이너슨ㄴ 뒤에서부터 거꾸로임
print(first[0]) # 펄스트 여기서 인덱스는 4까지임 5하면 범위를 벗어나기 때문에 오류 print(first[4])

print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
print(first[-6]) # IndexError!! 큰문제

## 현재 일시
current_date = '2022-05-02 14:23:45'
print(len(current_date))
year = current_date[0:4]
month = current_date[5:7]
day = current_date[8:10]
hour = current_date[11:13]
min = current_date[14:16]
ses current_date[17:]

print(year, '년:', month, '월:', day, '일')
print(hour, '시', min, '분', ses, '초')

print(current_date[-5:-3])

p = 'python'
print(p)
p[0] = 'P' #python TypeError
print('P'+ p[1:])

print(p.upper()) #대문자

print(p2.lower()) #소문자






