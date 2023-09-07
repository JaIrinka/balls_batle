# import time
from tkinter import *
from tkinter import ttk
from hex_field import HexField, SquareField
from configure import WIDTH, HEIGHT
import random

root = Tk()
root.title("PRINTING")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

size_hex = 15
field_colors = [
    "gold",
    "yellow",
    "goldenrod",
    "peru",
    "red",
    "orangered",
    "brown",
    "chocolate",
    "coral",
    "crimson",
    "darkgoldenrod",
    "darkorange",
    "darkred",
    "darksalmon",
    "firebrick",
    "indianred",
    "lightcoral",
    "lightpink",
    "lightsalmon",
    "tomato",
]


def print_hex():
    canvas = Canvas(
        root, width=WIDTH, height=HEIGHT, bg="white"
    )
    canvas.pack()

    def remove_canvas(a):
        canvas.destroy()
        hexBtn.pack()

    canvas.bind("<ButtonPress>", remove_canvas)
    hexBtn.pack_forget()

    field = HexField(canvas=canvas)
    # field = SquareField(canvas=canvas)
    
    figures = field.field()

    # ball = canvas.create_oval(900, 500, 1000, 600, fill="green", width=5)


    # def move():
    #     canvas.move(ball, -1, -1)
    #     canvas.after(10, move)
    # move()


    def colors():
        rand_hexagon = random.randint(0, len(figures) - 1)
        rand_color = random.randint(0, len(field_colors) - 1)
        canvas.itemconfigure(figures[rand_hexagon], fill=field_colors[rand_color])
        canvas.after(10, colors)
    colors()

hexBtn = ttk.Button(text="Hexagon field", command=print_hex)
hexBtn.pack()

root.mainloop()
