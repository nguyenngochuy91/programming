# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:03:03 2019

@author: huyn
"""

# 1177 Can Make Palindrome from Substring
def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    letter = "qwertyuiopasdfghjklzxcvbnm"
    d = {}
    for l in letter:
        d[l]=0
    dictionary={}
    for i in range(len(s)):
        dic = {}
        for l in letter:
            dic[l]=d[l]
        dic[s[i]]+=1
        dictionary[i]=dic
        d= dic
    ans = []
    for query in queries:
        left,right,k = query
        odd = 0
        val =0
        if left == 0:
            dic = dictionary[right]
            for l in letter:
                if dic[l]%2:
                    if odd ==1:
                        val+=1
                    else:
                        odd +=1
        else:
            for l in letter:
                if (dictionary[right][l]-dictionary[left-1][l])%2:
                    if odd ==1:
                        val+=1
                    else:
                        odd+=1
#        print (left,right,k,val)
        if (val%2)+(val//2)<=k:
            ans.append(True)
        else:
            ans.append(False)
    return ans