# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:47:26 2021

@author: YDD
"""
import ast
 
#阶乘函数
def fac_rec(n):
    if n == 0:
        f = 1
    else:
        f = n*fac_rec(n-1)
    return f

#阶乘的和
def fact_sum(n,m,*b):
    if n == 0:
        s = 1
    else:
        s = fac_rec(n) + fact_sum(n-1,m,*b)[0]
    result2 = s
    for i in b:
        result2 = result2*i
    try:
        result1 = s//m     
        return s,result1,result2
    except ZeroDivisionError:
        print("You can't divide by zero")
        return s,0,result2
    #return s,result

n = input("请输入n：")
n = int(n)
m = input("请输入m：")
m = int(m)
b = ast.literal_eval(input("请输入列表b，使用逗号隔开: ")) 
a = fact_sum(n,m,*b)
print(f'阶乘和为：{a[0]}')
print(f's//m={a[1]}')
print(f'可变参数*b与s累乘的结果：{a[2]}')
