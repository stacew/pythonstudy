import time
import threading
from tkinter import *
import random

class RacingCar:
    label = None #주소가 들어가는 변수에는 None세팅.

    def __init__(self, w, img):
        self.label = Label(w, image=img)
        self.label.pack(side=TOP, ipady=10)

    def runCar(self, x, y):
        self.label.place(x=x, y=y)

        for _ in range(0, 300):
            r = random.randrange(0, 10)
            x = x + r
            self.label.place(x=x, y=y)
            if x >= 300:
                break;

            time.sleep(0.1)


def allCar():
    c1 = RacingCar(w, car1)
    c2 = RacingCar(w, car2)
    c3 = RacingCar(w, car3)
    t1 = threading.Thread(target=c1.runCar, args=(10, 80))
    t2 = threading.Thread(target=c2.runCar, args=(10, 160))
    t3 = threading.Thread(target=c3.runCar, args=(10, 240))
    t1.start()
    t2.start()
    t3.start()

if __name__ == '__main__':

    w = Tk()
    w.title('자동차 경주 게임') #창(tk)의 타이틀
    w.geometry('400x300') #크기 조절

    car1 = PhotoImage(file = 'thread/file/car1.gif')
    car2 = PhotoImage(file = 'thread/file/car2.gif')
    car3 = PhotoImage(file = 'thread/file/car3.gif')

    b = Button(w, text = '자동차 경주 시작!!!', command=allCar)
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)

    w.mainloop()