# -*- coding: utf-8 -*-
"""
Created on Mon May 24 08:47:56 2021

@author: YDD
"""

class Restaurant:
    """关于一个饭馆的信息"""
    def __init__(self,Restaurante_name,cuisine_type):
        self.Restaurante_name = Restaurante_name
        self.cuisine_type = cuisine_type
        self.people_number = 0
    
    def describe_restaurant(self):
        """打印饭馆基本信息"""
        print(f"饭馆的名字是：{self.Restaurante_name}\n美食的类型是：{self.cuisine_type}")
        
    def open_restaurant(self):
        """打印饭馆营业情况"""
        print("饭馆正在营业！！！！")
        
    def record_people_number(self,num):
        """就餐人数"""
        #self.people_number = input("请输入就餐人数:")
        self.people_number = num
        print(f"当前就餐人数是：{self.people_number}人")