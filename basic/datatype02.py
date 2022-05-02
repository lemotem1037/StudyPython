# 문자열
bruce_eckel = "인생은 짧고. \n\t당신은 파이썬이 필요하다" #\n (기존의 문구를 탈출한다는 뜻) 엔터같은 특수문자,  #\t 탭키
print(bruce_eckel)

# multi_line 홑따운표 3개 자동 생성과 여러줄 문자(의 배)열
multi_line = '''인생은 짧고.
당신은 파이썬이 필요하다.
그리고 C#도 필요하다.
'''
print(multi_line)

# 불형 Boolean/bool

# 리스트(배열)_인덱스의 값은 전체 크기의 n-1
b = [1, 2, 3, 4] #오라클은 위치가 1부터 시작, 자바 파이썬 등은 인덱스가 0부터 시작
print(b)

b.append(5)#어팬드는 리스트 맨 마지막에 추가
print(b)

b.insert(3, 10) #3번째 위치에 10을 추가 # 원하는 위치, 인덱스에 추가
print(b)

b.sort() # sort 오름차순 정렬기능
print(b)

b.reverse() # reverse 내림차순 정렬기능
print(b)

b.remove(10) # 원소(원하는 값) 삭제
print(b)

print(type(b)) #결과<class 'list'> 클래스==타입이 리스트다


## 튜플
c = (1, 2, 3, 4)
print(c)
# c.append(5) #에러 튜플에서는 값 추가 불가능
print(c[2])


## 딕셔너리(사전타입) key : value 쌍의 집합
# () == 튜플, [] == 리스트, {} == 딕셔너리

spiderman = {
    'name' : '피터파커',
    'age' : 18,
    'weapon' : '웹슈터',
    'memberOFAvengers' : True

}

print(spiderman)
print(piderman['name'])
print(piderman['memberOFAvengers'])





