from turtle import *

def draw_hexagon(polygon_length):
    shape('turtle')
    speed(0)
    for x in range(6):
        forward(polygon_length)
        right(60)

draw_hexagon(100)
