# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:00:53 2021

@author: YDD
"""

file_name = 'readfile.txt'#文件名字
try:
    with open(file_name,encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} does not exist.")
else:
    words = contents.split()                        #以空格为分隔符split(str, count)
    for each_word in words:
        print(each_word)   #打印每一行

#求交集并集函数
def Intersection_and_union(words):
    temp_Intersection = set(words[0])
    temp_union = set(words[0])
    for each_word in words:
        temp_Intersection = set(each_word)&temp_Intersection
        temp_union = set(each_word)|temp_union
    return temp_Intersection,temp_union

[temp_Intersection,temp_union] = Intersection_and_union(words) #调用函数
print("集合的交集是:{temp_Intersection}")
print("集合的并集是:{temp_union}")
# temp_Intersection = str(temp_Intersection)
# temp_union = str(temp_union)
temp_Intersection = ''.join(temp_Intersection)
temp_union = ''.join(temp_union)
try:
    with open(file_name,'a') as f:
        f.write(f'\n{temp_Intersection}')
        f.write(f'\n{temp_union}')
except FileNotFoundError:
    print(f"Sorry, the file {file_name} does not exist.")
else:
    print("文件写入成功")


    