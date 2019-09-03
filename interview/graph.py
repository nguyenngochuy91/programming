# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:46:44 2019

@author: huyn
"""

#The Ruler of HackerLand believes that every citizen of the country should have access to a library. 
#Unfortunately, HackerLand was hit by a tornado that destroyed all of its libraries and obstructed its roads! 
#As you are the greatest programmer of HackerLand, the ruler wants your help to repair the roads and build 
#some new libraries efficiently.
#
#HackerLand has  cities numbered from  to . The cities are connected by  bidirectional roads. 
#A citizen has access to a library if:
#
#Their city contains a library.
#They can travel by road from their city to a city containing a library.
#The following figure is a sample map of HackerLand where the dotted lines denote obstructed roads:
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<=c_road:
        return c_lib*n
    d= {}
    for edge in cities:
        start,stop = edge
        if start not in d:
            d[start]=[]
        if stop not in d:
            d[stop]=[]
        d[start].append(stop)
        d[stop].append(start)
    
    return