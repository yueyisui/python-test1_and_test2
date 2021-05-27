# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:22:07 2021

@author: YDD
"""

#计算 10到 15的平方，存储到列表中,并对计算结果进行打印。
t = list()
for each in range(10,16):
    temp = each**2
    t.append(temp)
print(t)