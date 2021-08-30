from turtle import *

shape("circle")
speed(0)
shapesize(0.01)
bgcolor("lightblue")

def snowflake_side(length, levels):
    if levels == 0:
        #color("blue")
        #dot(length)
        #color("black")
        forward(length)
        return

    length /= 3.0
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

def create_snowflake(sides, length):
    for i in range(sides):
        snowflake_side(length, sides)
        right(360 / sides)

left(-180)
create_snowflake(4, 250)

mainloop()