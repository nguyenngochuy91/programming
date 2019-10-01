# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:54:19 2019

@author: huyn
"""

def sort012Left(array):
    zero = 0
    one  = 0
    two  = len(array)-1
    while one <=two:
        if array[one]==0:
            array[zero],array[one] = array[one],array[zero]
            zero+=1
            one+=1
        elif array[one]==1:
            one+=1
        else:
            array[one],array[two]= array[two],array[one]
            two-=1
    
    return array