# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:48:14 2021

@author: YDD
"""

import narcissus
print(narcissus.narcissus(153))
c = input("请输入一个大于等于1000的整数：")
c = int(c)
result = list()
for i in range(100,c):
    temp = narcissus.narcissus(i)
    if temp!=0:
        result.append(temp)
    num = len(result)
print(f"100到{c}之间的水仙花数有{result},共{num}个")