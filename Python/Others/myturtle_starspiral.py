from turtle import *

def draw_starspiral(star_length = 100):
    shape('turtle')
    speed(0)
    for x in range(60):
        for y in range(5):
            right(144)
            forward(star_length)
        star_length += 5
        right(5)

draw_starspiral()
