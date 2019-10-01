# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:09:14 2019

@author: huyn
"""

#1201. Ugly Number III
#Write a program to find the n-th ugly number.
#
#Ugly numbers are positive integers which are divisible by a or b or c.
def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
    start = min([a,b,c])
    stop  = max([a,b,c])*n
    lcmABC = lcm([a,b,c])
    lcmAB  = lcm([a,b])
    lcmBC  = lcm([c,b])
    lcmAC  = lcm([a,c])    
    while start+1<stop:
        mid   = (start+stop)//2
        index = getIndex(mid,lcmAB,lcmBC,lcmAC,lcmABC,a,b,c)
        if index<n:
            start = mid
        else:
            stop = mid
    return stop
def lcm(array):
    array = list(set(array))
    if len(array)==1:
        return array[0]
    a= array[0]
    multiple = a
    for num in array[1:]:
        a= math.gcd(a,num)
        multiple*=num
    return multiple/a
def getIndex(mid,lcmAB,lcmBC,lcmAC,lcmABC,a,b,c):
    numDivisibleC   = mid//c
    numDivisibleA   = mid//a
    numDivisibleB   = mid//b
    numDivisibleAB  = mid// lcmAB
    numDivisibleBC  = mid// lcmBC
    numDivisibleAC  = mid // lcmAC
    numDivisibleABC = mid //lcmABC
    if len(set([a,b,c]))==3:
        return numDivisibleA+numDivisibleB+numDivisibleC-numDivisibleAB-numDivisibleBC-numDivisibleAC+numDivisibleABC
    elif len(set([a,b,c]))==2:
        return sum(set([numDivisibleC,numDivisibleA,numDivisibleB]))-numDivisibleABC
    else:
        return numDivisibleA