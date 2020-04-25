class Phone: #모델링(설계)( = 디자인 )
    #성질(멤버 변수)
    color = ''
    company = ''

    #동작(멤버 함수)
    def __init__(self, color='', company=''): #객체 생성 시 변수 초기화
        self.color = color
        self.company = company
        print('__init__ 호출')
            

    def game(self):
        print(self.color + '색 폰으로 게임하다.')

    def __str__(self): #내장된 함수를 재정의
        return self.company +', ' + self.color + '색 Phone'


class Computer:
    company = ''
    price = ''
    def __init__(self, company, price):
        self.company = company
        self.price = price
    def __str__(self):
        return self.company + ' 제품, ' + str(self.price) + '원'


print('import : ' + __name__ + '\n')

#부품.py가 혼자 실행될 동작하도록
#if __name__ != '__main__': #테스트 해보려는데 quit()하면 전체 종료 됨.

if __name__ == '__main__':
    p1 = Phone()
    p1.color = '빨강'
    p1.company = 'sk'
    print(p1)
    p2 = Phone(company='samsung', color='파랑')
    print(p2)
    p3 = Phone(company='apple')
    print(p3)
    print()

    com1 = Computer('삼성', 100)
    com2 = Computer('Lg', 50)
    print(com1)
    print(com2)
    print()

print('import : ' + __name__ + '\n')