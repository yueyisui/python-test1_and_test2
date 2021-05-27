# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:32:04 2021

@author: YDD
"""

prompt = "请输入你喜欢的歌曲(输入 'quit' 停止)："
out = ''
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        out += city
        out += '\n'
        print(f'喜欢的歌曲有：\n{out}')