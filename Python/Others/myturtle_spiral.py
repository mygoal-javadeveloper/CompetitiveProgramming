from turtle import *

def draw_spiral(square_length = 5):
    shape('turtle')
    speed(0)
    for x in range(60):
        for y in range(4):
            forward(square_length)
            right(90)
        square_length += 5
        right(5)

draw_spiral()
