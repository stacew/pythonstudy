from tkinter import *
import random
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.configure(background='black')
canvas.pack()

x = 250
y = 250

for i in range(50000):
    dice = random.randint(1, 3)
    if dice == 1:
        px = 250
        py = 50
        myColor = 'red'
    elif dice == 2:
        px = 50
        py = 450
        myColor = 'green'
    else:
        px = 450
        py = 450
        myColor = 'blue'

    x = (x + px) / 2
    y = (y + py) / 2
    canvas.create_line(x, y, x+1, y+ 1, fill=myColor)
    tk.update()
    time.sleep(0.0010)

tk.mainloop()