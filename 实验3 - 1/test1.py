# -*- coding: utf-8 -*-
"""
Created on Mon May 24 08:03:47 2021

@author: YDD
"""

import Restaurant    
#我的饭店
my_restaurant = Restaurant.Restaurant("中南饭馆","中餐")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.record_people_number(3)

class IceCreamStand(Restaurant.Restaurant):
    "冰淇淋店"
    def __init__(self,Restaurante_name,cuisine_type):
        super().__init__(Restaurante_name,cuisine_type)
        self.flavors = ['iceCream1','iceCream2','iceCream3']
        
    def describe_icecreamstand(self):
        print(f"冰淇淋有：{ self.flavors}")
        
my_icecreamstand = IceCreamStand("中南饭馆","中餐")
my_icecreamstand.describe_icecreamstand()


        