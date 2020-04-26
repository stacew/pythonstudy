# import 부품 as tool
#p1 = tool.Phone()
#p2 = tool.Phone()

from 부품 import *
p1 = Phone()
p2 = Phone()

p1.color = '빨강'
p1.company = 'sk'
p1.game()
p2.color = '파랑'
p2.company = 'apple'
p2.game()
print()

print(p1)
print(p2)
print()

p1 = p2 #얕은 복사
p1.color = "검정"
print("p2 : " + str(p2))
print()

import copy
p1 = copy.deepcopy(p2) #깊은 복사
p1.color = "하얀"
print("p2 : " + str(p2))
print()

p3 = copy.deepcopy(p2) #깊은 복사 생성자 __init__ 아님.
print("p3 : " + str(p3))
print()