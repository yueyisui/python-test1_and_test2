# -*- coding: utf-8 -*-
"""
Created on Mon May 24 08:50:53 2021

@author: YDD
"""
import math
import numpy as np
import numpy.matlib

class SwimmingPoolPrice:
    '''游泳池的造价'''
    def __init__(self,R):
       self.R = R
       self.width = 3
       self.length = 0
       self.area = 0
       self.price = 0     
        
    def calculate_price(self):
        '''计算泳池的造价'''
        data_size = len(self.R)
        L= self.R
        B = np.matlib.ones((data_size,1)) #转为矩阵
        new_R =  (B.T*B).I*B.T*L
        length = 2*math.pi*new_R #周长
        area = math.pi*((new_R+self.width)**2-new_R**2) #面积
        self.price = length*35 + area*20 #价格造价
        print(f"游泳池的造价是：{self.price}")
        
data_size = 10 #数据个数
error = np.random.normal(size=(data_size,1))
noise_R = error + 30 #加入误差之后的数据
#我的泳池
my_swimmingpoolprice = SwimmingPoolPrice(noise_R)
my_swimmingpoolprice.calculate_price()

