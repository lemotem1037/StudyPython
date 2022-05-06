# 객체지향 클래스 상속
class Vehicle:
    name = '탈 것'
    color = '색상'

    def __init__(self,color = None) -> None:
        self.color = color
        print(f'{self.color} 색 {self.name} 생성!')


    def desc(self):
        print(f'{self.name} 객체')

    def move(self):
        print(f'{self.name} 이동!')

class Car(Vehicle): #Vehicle클래스를 상속받은 Car
    name = '자동차' #부모클래스의 name
    brand = '현대'

    def __init__(self, color=None) -> None:     # 부모에게 받은 그대로 상속
        super().__init__(color)                         
        print(f'{color}색 {self.brand} {self.name} 생성!!')
    
    def move(self):
        super().name()  
        print(f'{self.name} 달린다!')
         # super().move() # 부모에게서 상속된 이름으로 바껴서 {self.name}인자동차 달린다로 출력됨
    
    def stop(self):
        print('브레이크로 멈춘다.')


if __name__ == '__main__':     
    vcl = Vehicle()          # 부모클래스
    vcl.desc()
    vcl.move()

    mycar = Car('흰')            # 자식클래스
    mycar.desc()
    mycar.move()
    mycar.stop()





