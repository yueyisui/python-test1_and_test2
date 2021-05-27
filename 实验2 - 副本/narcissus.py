# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:26:21 2021

@author: YDD
"""
#水仙花函数
def narcissus(n):
    temp_n = str(n)
    list_n = list(temp_n)
    num = len(list_n)  #位数
    sum_temp = 0
    for each_n in list_n:
        each_n = int(each_n)
        sum_temp += each_n**num #求和
    if sum_temp == n: #判断是都为水仙花数
        return sum_temp
    else:
        return 0