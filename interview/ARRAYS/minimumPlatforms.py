# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:56:03 2019

@author: huyn
"""

def minimumPlatforms(array):
    output = 1
    currentInterval = array[0]
    local =1
    for interval in array[1:]:
        currentInterval,isOverlapped = overlap(currentInterval,interval)
        if isOverlapped:
            local+=1
        else:
            output = max(output,local)
            local = 1
    return output