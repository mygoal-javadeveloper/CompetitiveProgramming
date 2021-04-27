from turtle import *
def draw_square(square_length = 100):
    shape('turtle')
    speed(0)
    for x in range(60):
        for y in range(4):
            forward(square_length)
            right(90)
        right(5)


draw_square(150)

