import turtle
import time

local_time = time.localtime()
num_list = [[0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1]]
ang_list = [270, 180, 90, 90, 0, 270, 0]

turtle.setup(650, 350, 200, 200)
turtle.pensize(5)
turtle.pencolor("red")


def draw_number(input_number):
    temp_number_list = num_list[input_number]
    for i in range(7):
        if temp_number_list[i] == 0:
            turtle.penup()
        turtle.fd(100)
        turtle.seth(ang_list[i])
        turtle.pendown()


draw_number(5)

turtle.done()
