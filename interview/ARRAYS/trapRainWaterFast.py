# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:56:25 2019

@author: huyn
"""

def trapRainWaterFast(array):
    total = 0
    left = 0
    right = len(array)-1
    leftWall,rightWall = 0
    while left<right:
        if array[left]<array[right]:
            if array[left]>leftWall:
                leftWall = array[left]
            else:
                total+=leftWall-array[left]
            left+=1
        else:
            if array[right]>rightWall:
                rightWall = array[right]
            else:
                total+=rightWall-array[right]
            right-=1
    return total