# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:00:07 2019

@author: huyn
"""

#You are given two strings s and t of the same length, consisting of uppercase English letters. 
#Your task is to find the minimum number of "replacement operations" needed to get some anagram of the 
#string t from the string s. A replacement operation is performed by picking exactly one character from the string s and replacing it by some other character.
def createAnagram(s, t):
    ds = {}
    dt = {}
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in l:
        ds[letter]=0
        dt[letter]=0
    for item in s:
        ds[item]+=1
    for item in t:
        dt[item]+=1        
    swap = 0 # swapping
    leftOver = 0
    for letter in l:
        vs = ds[letter]
        vt = dt[letter]
        if vs==vt:
            continue
        elif vs<vt:
            extra = vs-vt
            if leftOver>=0:
                swap+=min(leftOver,-extra)
            leftOver+=extra
        else:
            extra= vs-vt 
            if leftOver<=0: 
                swap +=min(-leftOver,extra)
            leftOver+=extra 
    return swap