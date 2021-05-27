# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:05:38 2021

@author: YDD
"""

my_information = {'姓名':'岳冬冬','学号':'8211180305','专业':'遥感1801','宿舍号':'3011'}
print(my_information)
for key,value in my_information.items():
    print(f"Key:{key}")
    print(f"Value:{value}\n")
    
del my_information['宿舍号']
print(my_information)

information_1 =  {'姓名':'室友1','学号':'82111803013','专业':'遥感1801','宿舍号':'3011'}
information_2 =  {'姓名':'室友2','学号':'82111803022','专业':'遥感1801','宿舍号':'3011'}
my_list = [my_information,information_1,information_2]
print(my_list)
del my_list[1]['宿舍号']
del my_list[2]['宿舍号']
print(f'删除室友宿舍号信息之后：\n{my_list}')