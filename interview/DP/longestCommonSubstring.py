# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:08:25 2019

@author: huyn
"""

#longest common substring
# given 2 string, find the longest common susbstring
def longestCommonSubstring(s1,s2):
    n  = len(s1)
    m  = len(s2)
    arr =[[0]*n for i in range(m)]
    currentMax = 0
    for i in range(1,n):
        if s1[i]==s2[0]:
            arr[0][i]=1
            currentMax = 1
            stopS1    = i
            stopS2    = 0
    for j in range(1,m):
        if s2[j]==s1[0]:
            arr[j][0]=1 
            currentMax = 1
            stopS1    = 0
            stopS2    = j
    for j in range(1,m):
        for i in range(1,n):
            if s2[j]==s1[i]:
                arr[j][i]= arr[j-1][i-1]+1
                if currentMax<arr[j][i]:
                    currentMax = arr[j][i]
                    stopS1    = i
                    stopS2    = j                    
            else:
                arr[j][i] = 0
    if currentMax:
        return stopS1,stopS2
    return -1,-1
    
s1= "abc"
s2= "acabsdqabc"
print (longestCommonSubstring(s1,s2))
# return the matrix, we will traverse thsi ourselves
def longestCommonSubstringArr(s1,s2):
    n  = len(s1)
    m  = len(s2)
    arr =[[0]*n for i in range(m)]
    currentMax = 0
    for i in range(1,n):
        if s1[i]==s2[0]:
            arr[0][i]=1
            currentMax = 1
            stopS1    = i
            stopS2    = 0
    for j in range(1,m):
        if s2[j]==s1[0]:
            arr[j][0]=1 
            currentMax = 1
            stopS1    = 0
            stopS2    = j
    for j in range(1,m):
        for i in range(1,n):
            if s2[j]==s1[i]:
                arr[j][i]= arr[j-1][i-1]+1
                if currentMax<arr[j][i]:
                    currentMax = arr[j][i]
                    stopS1    = i
                    stopS2    = j                    
            else:
                arr[j][i] = 0
    return arr