# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:41:48 2021

@author: YDD
"""

import turtle
import datetime
pen_size = 5.
turtle.setup(1000,500,200,200)
turtle.pensize(pen_size)
my_time_list = [[0,1,1,1,1,1,1],[0,1,0,0,0,0,1],[1,0,1,1,0,1,1],[1,1,1,0,0,1,1],[1,1,0,0,1,0,1],
           [1,1,1,0,1,1,0],[1,1,1,1,1,1,0],[0,1,0,0,0,1,1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1]]
def draw_number(input_number,position_number,pen_color):
    angle_list = [0,-90,180,90,90,0,-90]
    temp_number_list = my_time_list[input_number]
    turtle.penup()
    my_position = position_number*60
    turtle.goto(my_position,0)
    for i in range(7):
        turtle.seth(angle_list[i])
        turtle.fd(pen_size)
        turtle.penup()
        if temp_number_list[i] == 1:
            turtle.pendown()
        turtle.pencolor(pen_color)
        turtle.seth(angle_list[i])
        turtle.fd(50-2*pen_size)
        turtle.penup()
        turtle.seth(angle_list[i])
        turtle.fd(pen_size)

now_year = list(str(datetime.datetime.now().year)) #当前的年
now_month = list(str(datetime.datetime.now().month)) #当前的月
now_day = list(str(datetime.datetime.now().day)) #当前的日
# 显示年
for i in range(len(now_year)):
    draw_number(int(now_year[i]),-5 + i,'red')
turtle.goto(-60,0)
turtle.color("black")
turtle.write("年", font=('Arial', 20, 'normal'))   
# 显示月
for i in range(len(now_month)):
    draw_number(int(now_month[i]),0 + 2 - len(now_month) + i,'green')
turtle.goto(120,0)
turtle.color("green")
turtle.write("月", font=('Arial', 20, 'normal'))   
# 显示日
for i in range(len(now_day)):
    draw_number(int(now_day[i]),3 + 2 - len(now_day) + i,'blue')    
turtle.goto(300,0)
turtle.color("blue")
turtle.write("日", font=('Arial', 20, 'normal'))   
turtle.done()







