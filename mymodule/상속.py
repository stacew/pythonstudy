class Person:
    name = '';
    def eat(self):
        print('먹다')

class Man(Person):
    speed = 0
    def eat(self):
        print('남자가 먹는다')
    def run(selfs):
        print('빨리 뛴다')

class Woman(Person):
    speed = 0

class SuperMan(Man):
    power = 0

    def fly(self):
        print('우주를 날다')

class WonderWoman(Woman):
    power = 0
    def eat(self):
        print('원더우먼이 먹는다')

#상속 관계
# 위 클래스 : 부모 클래스, super 클래스
#아래 클래스 : 자식 클래스, sub  클래스

if __name__ == '__main__':
    sm1 = SuperMan()
    sm1.eat()
    wm1 = WonderWoman()
    wm1.eat()