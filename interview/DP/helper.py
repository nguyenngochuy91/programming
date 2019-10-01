# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:05:17 2019

@author: huyn
"""
import random
def generateString(n,letters):
    string = ""
    for i in range(n):
        string+=random.choice(letters)[0]
    return string
def isPalindrom(string,startIndex,stopIndex):
#    print (startIndex,stopIndex)
    while startIndex<stopIndex:
#        print (startIndex,string[startIndex],stopIndex,string[stopIndex])
        if string[startIndex]!=string[stopIndex]:
            return False
        else:
            startIndex+=1
            stopIndex-=1
    return True