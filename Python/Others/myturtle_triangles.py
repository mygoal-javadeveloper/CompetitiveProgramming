from turtle import *

def draw_triangle(triangle_length, triangle_angles):
    shape('turtle')
    speed(0)
    for x in range(3):
        forward(triangle_length)
        left(triangle_angles)
        


draw_triangle(100, 120)
