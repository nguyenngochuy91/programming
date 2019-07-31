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
# given an array and target number, find the range of index that is equal to the target, 
# if target not in arrays, return [-1,-1]
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
# find peak in an array, could have multiple mid
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

# def find minimum element in rotated sorted array
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
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
def climbingLeaderboard(scores, alice):
    d= {}
    value = set()
    i = 1
    for s in scores:
        if s not in value:
            d[i]=s
            value.add(s)
            i+=1
    res = []
    for score in alice:
        start,stop = 1,len(d)
        check = False
        while start+1<stop:
            mid = (start+stop)//2
          
            if d[mid]==score:
                res.append(mid)
                check = True
                break
            if d[mid]<score:
                stop = mid
            else:
                start = mid
        if not check:
            if d[stop]>score:
                res.append(stop+1)
            else:
                if d[start]>score:
                    res.append(stop)
                else:
                    res.append(start)
    return res
