# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:01:29 2019

@author: huyn
"""
#516. Longest Palindromic Subsequence
#Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
from helper import generateString

s="cbbd"
# version used palindrome Substring
def longestPalindromeSubseq(s: str) -> int:
    arr =[]
    n = len(s)
    maxLength = 0
    for i in range(n):
        t= []
        for j in range(n):
            if i==j:
                t.append(1)
                maxLength = 1
            else:
                t.append(0)
        arr.append(t)
    # we go by the length of the substring
    for length in range(2,n+1):
        for i in range(n-length+1):
            j = i-1+length # j =i (diagonal, plus the legnth from it)
            if s[i]==s[j]:
                arr[i][j]= 2+arr[i+1][j-1]
            else:
                arr[i][j] = max(arr[i+1][j],arr[i][j-1])
            maxLength= max(maxLength,arr[i][j])
    return maxLength

#s = generateString(20,"adswqe")
#print (s)
#longestPalindromeSubseq(s)

def longestPalindromeSubseqAll(s):
    arr =[]
    n = len(s)
    maxLength = 0
    for i in range(n):
        t= []
        for j in range(n):
            if i==j:
                t.append(1)
                maxLength = 1
            else:
                t.append(0)
        arr.append(t)
    # we go by the length of the substring
    for length in range(2,n+1):
        for i in range(n-length+1):
            j = i-1+length # j =i (diagonal, plus the legnth from it)
            if s[i]==s[j]:
                arr[i][j]= 2+arr[i+1][j-1]
            else:
                arr[i][j] = max(arr[i+1][j],arr[i][j-1])
            maxLength= max(maxLength,arr[i][j])
    # backtrack on maxLength to gain all the subseq
    res = set()
#    last = (0,n-1)
    def dfs(currentX,currentY,currentPath,s):
        if currentX>=currentY: # we go the final
            if currentX==currentY:
                string = s[currentX]
            else:
                string = ""
            for letter in currentPath:
                string = letter+string+letter
            res.add(string)
        else:
            diagonal = arr[currentX+1][currentY-1]
            left     = arr[currentX][currentY-1]
            bot      = arr[currentX+1][currentY]
            val      = arr[currentX][currentY]
            print (val,left,bot,diagonal)
            if val==left and val == bot:
                dfs(currentX,currentY-1,currentPath,s)
                dfs(currentX+1,currentY,currentPath,s)
            else:
                if val == left:
                    dfs(currentX,currentY-1,currentPath,s)
                elif val==bot:
                    dfs(currentX+1,currentY,currentPath,s)
            if val==diagonal+2:
                currentPath.append(s[currentX+1])
                dfs(currentX+1,currentY-1,currentPath,s)
                currentPath.pop()
    dfs(0,n-1,[],s)
    return res
s = generateString(20,"adswqe")
#print (s)
#print (longestPalindromeSubseqAll(s))