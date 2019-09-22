# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:47:01 2019

@author: Huy Nguyen
"""
while True:
    n = input().strip()
    if n =="0":
        break	
    while len(n)>1:
        n = str(sum([int(i) for i in n]))
    print (n)