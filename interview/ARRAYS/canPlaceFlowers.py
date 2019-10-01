# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:57:06 2019

@author: huyn
"""

#    605. Can Place Flowers
#Suppose you have a long flowerbed in which some of the plots are planted and some 
#are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
#
#Given a flowerbed (represented as an array containing 0 and 1, where 0 means 
#empty and 1 means not empty), and a number n, return if n new flowers can be planted 
#in it without violating the no-adjacent-flowers rule.    
def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if len(flowerbed)==1 and flowerbed[0]==0 and n<=1:
        return True
    check = False
    start = 0
    stop = 0
    localLength = 0
    position = None
    for index,item in enumerate(flowerbed):
        if item:
            if check: # this means end of our vacancy
                stop = index-1
                if start ==0: # means that we are from the left
                    localLength= stop-start+1                        
                else:
                    localLength = (stop-start)
                n-= (localLength)//2
                check = False
        else:
            if not check:
                check = True
                start = index
        if n<=0:
            return True
    if check:
        stop = index
        if start:
            localLength = (stop-start)+1
        else:
            localLength = (stop-start)+2
        n-= (localLength)//2
    return n<=0