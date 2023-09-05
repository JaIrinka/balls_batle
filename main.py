# import time
from tkinter import *
from hex_field import hex_field
import random

root = Tk()
root.title("PRINTING")

max_x = 1000
mav_y = 600
size_hex = 20
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
    "tomato"
]

canvas = Canvas(
    root, width=max_x, height=mav_y, bg="white"
)  ##Размер листа и его цвет, на котором будут графические изображения
canvas.pack()

hexagons = hex_field(canvas, size_hex, max_x, mav_y)

# canvas.create_line(10, 10, 500, 500, fill="green", width=2)
# canvas.create_line(10, 10, 490, 245, 10, 490, 10, 10, fill="red", width=5)
# canvas.create_rectangle(100, 100, 300, 200, outline="blue", fill="red", width=10)
# canvas.create_rectangle(150, 210, 250, 400, outline="green", fill="yellow", width=10)
# canvas.create_rectangle(260, 350, 300, 400, fill="grey", width=10)

# canvas.create_oval(100, 100, 400, 300, fill="red", outline="black")
# canvas.create_oval(50, 50, 250, 250, outline="green", fill="yellow", width=10)
# canvas.create_oval(100, 100, 200, 200, outline="blue", fill="red", width=10)
ball = canvas.create_oval(900, 500, 1000, 600, fill="green", width=5)

# canvas.create_polygon(100, 110, 10, 210, 250, 400, outline="green", fill="yellow", width=10)
# canvas.create_polygon(100, 100, 100, 200, 200, 200, 200, 100, outline="blue", fill="blue")
# canvas.create_polygon(100, 100, 100, 200, 300, 300, 10, 50, outline="blue", fill="orange", width=10)
# canvas.create_polygon(200, 150, 200, 250, 250, 300, 350, 300, 400, 250, 400, 150, 350, 100, 250, 100, outline="lime", fill="aqua", width=10)

# p1 = [300, 200]
# p2 = [250, 300]
# p3 = [350, 300]
# p4 = [350, 100]
# p5 = [250, 100]
# canvas.create_polygon(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], p1[0], p1[1], p4[0], p4[1], p5[0], p5[1], outline="brown", fill="tan", width=10)

# f2 = [450, 300]
# f3 = [550, 300]
# f4 = [550, 100]
# f5 = [450, 100]
# canvas.create_polygon(f2[0], f2[1], f3[0], f3[1], f5[0], f5[1], f4[0], f4[1], outline="brown", fill="tan", width=10)

# canvas.create_text(250, 250, font="Arial 50", text="Hello World", fill="green")

# canvas.create_oval(100, 100, 400, 300, fill="red", outline="black")


def move():
    canvas.move(ball, -1, -1)
    canvas.after(10, move)


move()


def colors():
    rand_hexagon = random.randint(0, len(hexagons) - 1)
    rand_color = random.randint(0, len(field_colors) - 1)
    canvas.itemconfigure(hexagons[rand_hexagon], fill=field_colors[rand_color])
    canvas.after(10, colors)


colors()

# canvas.create_polygon(0, 0, 0, 75, 75, 75, 75, 0, fill="red")
# canvas.create_oval(100, 100, 300, 300, fill="green")
# canvas.create_polygon(100, 100, 150, 150, 200, 100, fill="blue")

# while True:
#     for i in range((mx-100)//10):
#         c.move(ball, 10, 1)
#         root.update()
#         time.sleep(0.0005)


root.mainloop()
