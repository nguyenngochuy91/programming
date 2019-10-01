# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:07:48 2019

@author: huyn
"""

def getPeak(nums):
    # Write your code here
    start ,stop =0,len(nums)-1 
    while start+1<stop:
        mid = (start+stop)//2
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid
        elif nums[mid]<nums[mid-1]:
            stop = mid
        elif nums[mid]<nums[mid+1]: 
            start = mid
    if nums[start]>=nums[stop]:
        return start
    return stop