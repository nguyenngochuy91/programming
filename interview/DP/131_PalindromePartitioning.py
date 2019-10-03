# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:55:22 2019

@author: huyn
"""
from helper import isPalindrom,generateString
#from typing import List
#131. Palindrome Partitioning
#Given a string s, partition s such that every substring of the partition is a palindrome.
#
#Return all possible palindrome partitioning of s.
s="aab"
#[
#  ["aa","b"],
#  ["a","a","b"]
#]
def partition(s: str):
    res = []
    def dfs(s,index,path):
        if index == len(s):
            temp = []
            for item in path:
                temp.append(item)
            res.append(temp)
        for i in range(index,len(s)):
            if isPalindrom(s,index,i):
                path.append(s[index:i+1])
                dfs(s,i+1,path)
                path.pop()
    dfs(s,0,[])
    return res
s = generateString(20,"abcd")
print (s)
#print (partition(s))
