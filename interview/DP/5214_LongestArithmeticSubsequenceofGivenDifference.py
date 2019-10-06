# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:02:44 2019

@author: huyn
"""

#5214. Longest Arithmetic Subsequence of Given Difference
#Given an integer array arr and an integer difference, return the length of the 
#longest subsequence in arr which is an arithmetic sequence such that the difference 
#between adjacent elements in the subsequence equals difference.
from typing import List
def longestSubsequence(arr: List[int], difference: int) -> int:
    maxLength = 1
    d = {arr[0]:1}
    for item in arr[1:]:
        val = item-difference
        if val in d:
            length = d[val]
            d[item] = length+1
            maxLength = max(maxLength,d[item])
        else:
            d[item]=1
    return maxLength 