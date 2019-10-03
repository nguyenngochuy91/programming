# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:29:15 2019

@author: huyn
"""

from typing import List
class Trie:
    def __init__(self):
        self.root = {}
    # this function only add the word into the Trie, with index in the list, is reverse
    def add(self,word,index,isReverse):
        root = self.root
        stack = []
        for letter in word:
            if letter not in root:
                root[letter] = {}
            root = root[letter]
        
def isPalindrom(string):
#    print (startIndex,stopIndex)
    return string==string[::-1]    
#336. Palindrome Pairs
#Given a list of unique words, find all pairs of distinct indices (i, j) in the 
#given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome. 
def palindromePairsNaive(words: List[str]) -> List[List[int]]:
    d = {}
    for index,word in enumerate(words):
        if word not in d:
            d[word]=[]
        reverse= word[::-1]
        if reverse not in d:
            d[reverse]=[]
        d[reverse].append(index)
        d[word].append(index)
    res = set()
    for index,word in enumerate(words):
        for j in range(len(word)+1):
            leftWord = word[:j]
            rightWord = word[j:]
            if isPalindrom(leftWord) and rightWord in d and d[rightWord]!=index:
                res.add((d[rightWord],index))
            if isPalindrom(rightWord) and leftWord in d and d[leftWord]!=index:
                res.add((index,d[leftWord]))
                
    return res
    
#Input: ["abcd","dcba","lls","s","sssll"]
#Output: [[0,1],[1,0],[3,2],[2,4]] 
    
#Input: ["abcd","dcba","lls","s","sssll"]
#Output: [[0,1],[1,0],[3,2],[2,4]] 
# given 2 string of different length, check if concatenate give palindrome
def isPalindrome(s1,s2):
    l1,l2 = len(s1),len(s2)
    for i in range((l1+l2)//2):
        j = l1+l2-i-1
        if l1>=l2:
            if j<l1:
                if s1[i]!=s1[j]:
                    return False
            else:
                j-=l1
                if s1[i]!=s2[j]:
                    return False
        else:
            if i<l1:
                if s1[i]!=s2[j-l1]:
                    return False
            else:
                if s2[i-l1]!=s2[j-l1]:
                    return False
            
    return True
    

print (isPalindrome("abcddc","ba"))
print (isPalindrome("abcd","cba"))
print (isPalindrome("abc","cba"))
# given a word, check the farthest point that it forms a palindrome from the end
