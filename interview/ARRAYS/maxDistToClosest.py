# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:56:44 2019

@author: huyn
"""
#849. Maximize Distance to Closest Person
#In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
#
#There is at least one empty seat, and at least one person sitting.
#
#Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
#
#Return that maximum distance to closest person.
def maxDistToClosest(seats):
    check = False
    currentLength = 0
    start = 0
    stop = 0
    localLength = 0
    position = None
    for index,item in enumerate(seats):
        if item:
            if check: # this means end of our vacancy
                stop = index-1
                if start ==0: # means that we are from the left
                    localLength= stop-start
                    if (localLength>currentLength):
                        position= 0
                        currentLength = localLength
                else:
                    localLength = (stop-start)//2
                    if (localLength>currentLength):
                        position= (stop+start)//2
                        currentLength = localLength
                check = False
        else:
            if not check:
                check = True
                start = index
    if check:
        stop = index
        localLength = (stop-start)
        if localLength>currentLength:
            position = index
            currentLength = localLength
    return currentLength+1