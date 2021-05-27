# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:25:19 2021

@author: YDD
"""

age = input('请输入年龄：')
age = int(age)
if age<2:
    print('这个人是婴儿')
elif 2<=age and age<4:
    print('这个人是幼儿') 
elif 4<=age and age<13:
    print('这个人是儿童')  
elif 13<=age and age<20:
    print('这个人是青年人')  
elif 20<=age and age<65:
    print('这个人是成年人')  
elif 65<=age:
    print('这个人是老年人')  