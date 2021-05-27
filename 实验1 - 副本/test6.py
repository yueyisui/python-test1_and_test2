a# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:05:16 2021

@author: YDD
"""

#手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： ）手动创建列表包含汽车品牌信息： byd, toyota, audi, subaru, changan。
car_brand = ['byd', 'toyota', 'audi','subaru', 'changan']
for each in car_brand[0:3]:
    print(each)
sort_car_brand_1 = sorted(car_brand)
print(sort_car_brand_1)
car_brand.sort()
print(car_brand)
car_brand.reverse()
print(car_brand)
#加入宝马
print('添加宝马之后排序：')
car_brand.append('baoma')
sort_car_brand_2 = sorted(car_brand)
print(sort_car_brand_2)
car_brand.sort()
print(car_brand)
