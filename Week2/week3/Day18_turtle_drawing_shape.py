
#turtle for drawimg shape
import turtle as t
import random
tim = t.Turtle()
colors = ["red","purple","green","yellow","gray","brown"]

def draw_shape(num_sides):
    angle =360 / num_sides
    for _ in range(num_sides):
        tim.forward(80)
        tim.right(angle)

for shape_Side_n in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(shape_Side_n)
