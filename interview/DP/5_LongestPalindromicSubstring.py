# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:27:16 2019

@author: huyn
"""
from helper import generateString,isPalindrom
#5. Longest Palindromic Substring
#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
# O(n^3)
def longestPalindromeNaive(s: str) -> str:
    for i in range(len(s)-1,0,-1):
#        print (i)
        for j in range(len(s)-i):
#            print (14,j,j+i)
            if isPalindrom(s,j,j+i):
                return s[j:j+i+1]

#s="babad"
##print (isPalindrom(s,0,2))
#print (longestPalindrome(s))
#s = "cbbd"
#print (longestPalindrome(s))
##s = generateString(10,"asdf")
def longestPalindromeReverse(s1):
    if len(s1)==1:
        return s1
    s2 = s1[::-1]
    n  = len(s1)
    m  = len(s2)
    arr =[[0]*n for i in range(m)]
    currentMax = 0
    for i in range(n):
        if s1[i]==s2[0]:
            arr[0][i]=1
            currentMax = 1
            stopS1    = i
    for j in range(m):
        if s2[j]==s1[0]:
            arr[j][0]=1 
            currentMax = 1
            stopS1    = 0
    for j in range(1,m):
        for i in range(1,n):
            if s2[j]==s1[i]:
                arr[j][i]= arr[j-1][i-1]+1
#                print (i,j)
                if currentMax<arr[j][i]:
#                    print (i,j)
                    if len(s1)-1-j==i-arr[j][i]+1:
                        currentMax = arr[j][i]
                        stopS1     = i
            else:
                arr[j][i] = 0
#    print (arr)

    if currentMax:
        return s1[stopS1-currentMax+1:stopS1+1]
    return ""


def longestPalindromeDP(s):
    arr =[]
    l,r=0,-1
    for i in range(len(s)):
        arr.append([i,i])
        l,r = i,i
        try:
            if s[i]==s[i+1]:
                arr.append([i,i+1])
        except:
            continue
    maxLength =1
    for start,stop in arr:
        while True:
            if maxLength<stop+1-start:
                maxLength = stop+1-start
                l,r = start,stop
            if start==0 or stop==len(s)-1:
                break
            else:
                start-=1
                stop+=1
                if s[start]==s[stop]:
                    continue
                else:
                    break

    return s[l:r+1]
#s = "adfdasssssafsaadafsa"
#print (longestPalindromeDP(s))

def longestPalindromeSpace(s):
    l,r=0,-1
    maxLength  = 0
    for i in range(len(s)):
        start,stop =i,i
        while True:
            if maxLength<stop+1-start:
                maxLength = stop+1-start
                l,r = start,stop
            if start==0 or stop==len(s)-1:
                break
            else:
                start-=1
                stop+=1
                if s[start]==s[stop]:
                    continue
                else:
                    break
        start,stop =i,i+1
        try:
            if s[i]==s[i+1]:
                while True:
                    if maxLength<stop+1-start:
                        maxLength = stop+1-start
                        l,r = start,stop
                    if start==0 or stop==len(s)-1:
                        break
                    else:
                        start-=1
                        stop+=1
                        if s[start]==s[stop]:
                            continue
                        else:
                            break  
        except:
            continue
    return s[l:r+1]
s= "cbbd"
print (longestPalindromeSpace(s))