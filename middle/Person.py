# 사람 객체를 위한 클래스 Person
from ast import Pass  # Pass는 ptyhon에만 있는 실행 기능

class Person:   #동사 없고, 행위는 함수로 작성 가능
    name = ''    # 이름속성
    age = 0      # 나이속성
    height = 100 # 키
    weight = 40  # 몸무게

    def walk(self, speed):
        print(f'{self.name}이/가 {speed}km/h로 걷는다.')
        return 
        
    def run(self, speed):
        print(f'{self.name}이/가 {speed}km/h로 뛴다.')
        return 


p = Person() # 객체 생성
name = 'lemotem' 
p.age = 24
p.height = 158
p.weight = 52

p.walk(2)   # p == self
p.run(10)

print(type(p)) # type class 안에 __main__. 변수 Person

print(p.name) 
print(p.age)


## 보안용 연습 __ 
from ast import Pass  # Pass는 ptyhon에만 있는 실행 기능

class Person:   #동사 없고, 행위는 함수로 작성 가능
    __name = ''  # 이름속성
    age = 0      # 나이속성
    height = 100 # 키
    weight = 40  # 몸무게

    #생성자 재정의 (new가 먼저 init == 초기화)
    def __init__(self, name) -> None:    # '-> None' 생략가능
        if name == None:
            self.__name = 'lemotem'
        else:
            self._name = name
 
        print(f'{self.__name} 탄생!')
# 매직메서드__str__ 사용 재정의
def __str__(self) -> str:
    value = f'''객체 {self.__name}\n
    나이 : {self.age}\n
    키 : {self.height} '''
    return value

    def walk(self, speed):
        print(f'{self.name}이/가 {speed}km/h로 걷는다.')
        return 
        
    def run(self, speed):
        print(f'{self.name}이/가 {speed}km/h로 뛴다.')
        return 

p = Person('lemotem') # 객체 생성
#p.__name = 'lemotem' 
p.age = 24
p.height = 158
p.weight = 52

p.walk(2)   # p == self
p.run(10)

#print(type(p)) # type class 안에 __main__. 변수 Person

#print(p.name) 
#print(p.age)
print(p)

