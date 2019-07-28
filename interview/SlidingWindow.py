# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 13:08:07 2019

@author: huyn
"""

"""
When to use:
    Ordered and iterable data structure: array, string, linkedList
"""

#Given an array of unsorted intrgers and a integer target, return true if a contiguous subarrays sums up to the 
#integer target. Otherwise, return False
# all positive
# O(n) time, O(1) space
def findContiguousSubarraySumUpToTarget(arr,target):
    start = end = 0
    subtotal = 0
    while end<len(arr):
        subtotal+=arr[end]
        end+=1
        while subtotal>target and start+1<end:
            subtotal-=arr[start]
            start+=1
        if subtotal==target:
            return True
    return False
# largest sum contiguous subarray:
def findContiguousSubarrayMaxSum(arr):
    start = end = 0
    currentM = -float("inf")
    currentS = 0
    while end<len(arr):
        currentS+=arr[end]
        end +=1
        while arr[start]<0 and start+1<end:
            currentS-=arr[start]
            start+=1
        if currentS>currentM:
            print (start,end-1)
            currentM = currentS
    return currentM
def normalMaxSub(arr):
    currentM,currentS = -float("inf"),0
    for item in arr:
        currentS = max(0,currentS+item)
        currentM = max(currentS,currentM)
    return currentM
#arr =[-2,4,-1,-2,1,5,-3,-15,2,3]
#arr1 = [-2,-3,-1,-2,-7,-9,-3,-15,2,3]
#print (normalMaxSub(arr))
#print (findContiguousSubarrayMaxSum(arr))
    
# 