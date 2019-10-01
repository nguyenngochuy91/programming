# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:08:11 2019

@author: huyn
"""

def climbingLeaderboard(scores, alice):
    d= {}
    value = set()
    i = 1
    for s in scores:
        if s not in value:
            d[i]=s
            value.add(s)
            i+=1
    res = []
    for score in alice:
        start,stop = 1,len(d)
        check = False
        while start+1<stop:
            mid = (start+stop)//2
          
            if d[mid]==score:
                res.append(mid)
                check = True
                break
            if d[mid]<score:
                stop = mid
            else:
                start = mid
        if not check:
            if d[stop]>score:
                res.append(stop+1)
            else:
                if d[start]>score:
                    res.append(stop)
                else:
                    res.append(start)
    return res