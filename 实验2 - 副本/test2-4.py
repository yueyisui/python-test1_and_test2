# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:02:26 2021

@author: YDD
"""

leap_year = {'1':31,'2':29,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
Ordinary_year = {'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
year = input("请输入年份：")
month = input("请输入月份：")
year = int(year)

if year%4 == 0:
   for key, value in leap_year. items():
        if month == key:
            print(f"{year}年{month}有{value}天")
            break
else:
    for key, value in Ordinary_year. items():
        if month == key:
            print(f"{year}年{month}有{value}天")
            break