from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

width_half = 500 / 2
height_half = 500 / 2
step = 5

for i in range(10, 250, step):
    x1 = width_half - i
    y1 = height_half - i
    x2 = width_half + i
    y2 = height_half + i
    canvas.create_arc(x1, y1, x2, y2, extent=255, style=ARC)
    tk.update()
    time.sleep(0.01)

tk.mainloop()