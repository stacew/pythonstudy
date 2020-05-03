from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

canvas.create_line(100, 100, 400, 400)

colors = ['red', 'pink', 'blue', 'purple', 'yellow'];
canvas.create_rectangle(100, 100, 400, 400, fill=random.choice(colors))

tk.mainloop()