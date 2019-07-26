# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:37:52 2019

@author: huyn
"""

# second version of binarySearch that has l<r, and r = mid, l = mid , 
# this helps our l and r never goes out of bound, and they dont flip
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