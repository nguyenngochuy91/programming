# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:08:25 2019

@author: huyn
"""
#875. Koko Eating Bananas
#Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  
#The guards have gone and will come back in H hours.
#
#Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, 
#and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, 
#and won't eat any more bananas during this hour.
#
#Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
#
#Return the minimum integer K such that she can eat all the bananas within H hours.
def minEatingSpeed(piles, H):
    def check(piles,K,H):
        hour = 0
        for p in piles:
            hour+=p//K
            if p%K:
                hour+=1
        return hour<=H
    start,stop = 0, max(piles)
    while start+1<stop:
        mid = (start+stop)//2
        if check(piles,mid,H):
            stop = mid
        else:
            start = mid
    if check(piles,stop,H):
        return stop
    return start