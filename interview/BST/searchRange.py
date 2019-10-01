# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:07:33 2019

@author: huyn
"""

def searchRange(nums, target):
    # Write your code here
    def searchLeft(nums,target):
        start,stop = 0 , len(nums)-1
        while start+1<stop:
            mid = (start+stop)//2
            if nums[mid]>=target: 
                stop = mid 
            else:
                start = mid
        if nums[start]==target:
            return start
        if nums[stop]== target:
            return stop 
        return -1 
    left = searchLeft(nums,target)
    if left ==-1:
        return [-1,-1]
    def searchRight(nums,target):
        start,stop = 0 , len(nums)-1
        while start+1<stop:
            mid = (start+stop)//2
            if nums[mid]<=target: 
                start = mid 
            else:
                stop = mid
        if nums[stop]==target:
            return stop
        if nums[start]== target:
            return start 
    right = searchRight(nums,target)
    return [left,right] 