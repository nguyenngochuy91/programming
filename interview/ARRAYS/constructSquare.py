# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:00:30 2019

@author: huyn
"""

#Given a string consisting of lowercase English letters, find the largest square number which 
#can be obtained by reordering the string's characters and replacing them with any digits you need 
#(leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.
#
#If there is no solution, return -1.
def constructSquare(s):
    v = len(s)
    ds = {}
    dv = {}
    for l in s:
        if l not in ds:
            ds[l]=0
        ds[l]+=1
    for key in ds:
        val = ds[key]
        if val not in dv:
            dv[val]=[]
        dv[val].append(key)
    if len(ds)>10:
        return -1
    if v ==1:
        return 9
    start = int((10**(v-1))**.5)
    stop  = int((10**v)**.5)

    for i in range(stop,start,-1):
        i = i**2

        # check if there is a valid mapping
        num = str(i)
        ds = {}
        dn= {}
        check = True
        for l in num:
            if l not in ds:
                ds[l]=0
            ds[l]+=1
        for key in ds:
            v = ds[key]
            if v not in dn:
                dn[v]=[]
            dn[v].append(key)  
        if len(dn)!=len(dv):
            continue
        for key in dn:
            if key not in dv:
                check = False
                break
            else:
                if len(dv[key])!=len(dn[key]):
                    check = False 
                    break 
        if check:
            return i
            
    return -1