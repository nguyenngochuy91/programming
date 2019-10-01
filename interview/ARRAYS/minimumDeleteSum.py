# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:58:48 2019

@author: huyn
"""

#712. Minimum ASCII Delete Sum for Two Strings
#
#Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
def minimumDeleteSum(s1,s2):
    dp =[]
    for i in range(len(s1)+1):
        temp =[]
        for j in range(len(s2)+1):
            temp.append(None)
        dp.append(temp)
    dp[0][0]=0
    for i in range(1,len(s1)+1):
        dp[i][0]= dp[i-1][0]+ord(s1[i-1])
    for j in range(1,len(s2)+1):
        dp[0][j] = dp[0][j-1]+ord(s2[j-1])
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))
    return dp[-1][-1]