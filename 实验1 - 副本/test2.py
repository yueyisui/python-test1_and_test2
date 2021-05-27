# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:07:04 2021

@author: YDD
"""

first_name = "eric"
last_name = "pottier"
massage1 = f"Hello, {first_name.title()} {last_name.title()}! Would you like to learn some python today?"
massage2 = f"Hello, {first_name.upper()} {last_name.upper()}! Would you like to learn some python today?"
massage3 = f"Hello, {first_name} {last_name.title()}! Would you like to learn some python today?"
print(massage1)
print(massage2)
print(massage3)
print(f"倒数第三个字母是：{massage1[-3]}")
