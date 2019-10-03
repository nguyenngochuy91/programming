# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:03:05 2019

@author: huyn
"""
from helper import generateString
from typing import List
#267. Palindrome Permutation II
#Given a string s, return all the palindromic permutations (without duplicates)
# of it. Return an empty list if no palindromic permutation could be form.
def generatePalindromes(s: str) -> List[str]:
    d = {}
    for letter in s:
        if letter not in d:
            d[letter]=0
        d[letter]+=1
    res = []
    c = 0
    oddLetter= ""
    for letter in d:
        if d[letter]%2:
            c+=1
            oddLetter = letter
            if c>1:
                return []
    if c == 1:
        d[oddLetter]-=1
    res = set()
    letterList = []
    for letter in d:
        for i in range(d[letter]//2):
            letterList.append(letter)
    def dfs(swapIndex,oddLetter):
        if swapIndex==len(letterList):
            res.add("".join(letterList)+oddLetter+"".join(letterList[::-1]))
        else:
            for i in range(swapIndex,len(letterList)):
                if letterList[i]!=letterList[swapIndex] or swapIndex==i:
                    letterList[i],letterList[swapIndex]= letterList[swapIndex],letterList[i]
                    dfs(swapIndex+1,oddLetter)
                    letterList[swapIndex],letterList[i] = letterList[i],letterList[swapIndex]
    dfs(0,oddLetter)
    return list(res)  

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#print (s)
#print(generatePalindromes(s))