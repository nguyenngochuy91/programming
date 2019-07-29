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
    
# 76. Minimum Window Substrin
#    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
def findSubString(str1,str2):
    if len(str2)==1:
        return str2 in str1
    d = {}
    for l in str2:
        if l not in d:
            d[l]=0
        d[l]+=1
    # number of different character, use this to mark if we already match str2
    hitting = 0
    start,stop = 0,0
    currentD = {}
    output = ""
    while stop<len(str1):
        letter = str1[stop]
        if letter not in currentD:
            currentD[letter]=0
        currentD[letter]+=1
        if letter in d and d[letter]==currentD[letter]:
            hitting+=1
#        print (currentD,hitting)
        # if we hit the form, we will retract just like our template, we retract as long as our hitting is still equal to len(d)
        while hitting ==len(d) and start+1<stop:
#            print ("inner loop")
            # we check if our current is the smallest string
            if not output:
                output = str1[start:stop+1]
#                print (84,output)
            else:
                if (stop-start+1)<len(output):
                    output = str1[start:stop+1]
#                    print (88,output)
        
            # get the character on start
            leftMostLetter =str1[start]
#            print ("leftMostLetter",leftMostLetter)
            # decrease our count
            currentD[leftMostLetter]-=1
#            print (currentD)
            if leftMostLetter in d and currentD[leftMostLetter]<d[leftMostLetter]:
                hitting-=1
            
            # increment our start
            start+=1
        # increment our stop
        stop+=1  
            
    return output
#239. Sliding Window Maximum
#Given an array nums, there is a sliding window of size k which is moving from the very 
#left of the array to the very right. You can only see the k numbers in the window. 
#Each time the sliding window moves right by one position. Return the max sliding window.