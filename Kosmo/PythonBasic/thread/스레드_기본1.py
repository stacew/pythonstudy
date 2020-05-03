import threading


# 지역변수(Local) 지역 이외에서 존재하는지 모름.
# <-> 전역변수(Global)

def minus():
    for x in range(100, -1, -1):
        print('minus :', x)


def plus():
    for x in range(0, 101):
        print('plus :', x)


# target = minus() <-뒤에 () 붙이면 쓰레드 안함...
m = threading.Thread(target=minus)
p = threading.Thread(target=plus)

m.start()
p.start()
