# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:29:19 2021

@author: YDD
"""

all_class = ['测绘1801','测绘1802','测绘1803','遥感1801']
for each_class in all_class:
    print(f"{each_class}诚挚邀请参加学院篮球赛 !")
    
print('测绘 1801班不能参加')
all_class[0] = '测绘1901'
print(all_class)

all_class.insert(0,'测绘1902')
all_class.append('遥感1901')
print(all_class)

del all_class[5]
num = len(all_class)
print(f'遥感1901可以优先选择比赛对手，参赛班级数量为{num}个')

choose_class = input(f'请输入选择班级的编号（1-{num}）：')
choose_class = int(choose_class)
if choose_class>0 and choose_class<=5:
    temp_all_class = all_class.pop(choose_class-1)  
    print(f'遥感1901选择的对手为{temp_all_class}')

