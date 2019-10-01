# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:09:00 2019

@author: huyn
"""

#https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
######### great one
def repeatedString(s, n):
    d= {}
    current = None
    for i in range(len(s)):
        if s[i]=="a":
            if not d:
                d[i]=1
                current = i
            else:
                d[i]=d[current]+1
                current = i
    bigCount = n//len(s)*(len(d))
#    print ("bigCount",bigCount)
    extraLength = n%len(s)
#    print ("extraLength",extraLength)
    if extraLength and d:
        array = list(d.keys())
        start = 0
        stop = len(array)-1
        while start+1<stop:
            mid = (start+stop)//2
            if array[mid] == extraLength-1:
                return bigCount+d[array[mid]]
            elif array[mid]<extraLength-1:
                start=mid
            else:
                stop = mid
#        print (array,start,stop)
        if array[stop]<=extraLength-1:
            return bigCount+d[array[stop]]
        elif array[start]<=extraLength-1:
            return bigCount+d[array[start]]
    return bigCount