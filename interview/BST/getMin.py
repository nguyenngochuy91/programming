# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:08:01 2019

@author: huyn
"""

def getMin(nums):
    # Write your code here
    start,stop = 0,len(nums)-1 
    while start+1<stop: 
        mid = (start+stop)//2
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return nums[mid+1]
        elif nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
            return nums[mid]
        elif nums[mid]<nums[mid+1] and nums[mid]>nums[mid-1]: # mid-1,mid,mid+1 increase 
            if nums[mid]<nums[len(nums)-1]: # means that our min is to the left 
                stop = mid
            else: # min is to the right 
                start = mid
    if start ==stop: 
        return nums[start]
    return min(nums[start],nums[stop])