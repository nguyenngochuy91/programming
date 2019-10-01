# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:07:06 2019

@author: huyn
"""

def binarySearch(arr,num):
    start,stop = 0,len(arr)-1
    while start +1< stop:
        mid = (start+stop)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            stop = mid
        else:
            start = mid
    if arr[start]== num: 
        return start
    if arr[stop] == num: 
        return stop
    return -1