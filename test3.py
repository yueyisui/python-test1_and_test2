# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:40:28 2021

@author: YDD
"""
import win32com.client

class Calculator:
     def __init__(self):
         self.result = 0
        
     def calculator(self,num):
         '''初始值'''
         self.result = num
       
     def jia(self,num):
         """加法"""
         self.result += num
        
     def jian(self,num):
         """减法"""
         self.result -= num
        
     def cheng(self,num):
         """乘法"""
         self.result *= num
         
     def chu(self,num):
         """乘法"""
         try:
             self.result = self.result/num
         except:
             print('不可以除以0')
                 
   
c1 =  Calculator()
c1.calculator(2)
c1.jia(6)
c1.jian(4)
c1.cheng(5)
print(c1.result)

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("王秉章是傻子")