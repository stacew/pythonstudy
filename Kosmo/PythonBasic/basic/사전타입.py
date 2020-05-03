# 딕셔너리(=사전) - 키:값의 쌍의 자료구조
# 데이터 전송 시 사용되는 자료구조
me = {'이름': '홍길동', '나이': 100, '키': 120}
print(me['이름'])
print(me['나이'])
print(me['키'])
print()

our = {'member': ['홍길동', 100, 120]}
print(our['member'])

me = our['member']
print(me[0], me[1], me[2])


for x in me:
    print(x, end=' ')
