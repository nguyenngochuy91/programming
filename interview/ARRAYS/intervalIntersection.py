# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:57:58 2019

@author: huyn
"""

#986. Interval List Intersections
#
#Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
#Return the intersection of these two interval lists.
#
#(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x 
#with a <= x <= b.  The intersection of two closed intervals is a set of real numbers 
#that is either empty, or can be represented as a closed interval.  For example, the intersection of 
#[1, 3] and [2, 4] is [2, 3].)
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
def intervalIntersection(A,B):
    i = 0
    j = 0
    result = []
    while i<len(A) and j<len(B):
        intervalA = A[i]
        intervalB = B[j]
        # check if those 2 interval intersect
        if (intervalA[0]>=intervalB[0] and intervalA[0]<=intervalB[1]): # means that B[0], A[0],min(B[1],A[1]),max(B[1],A[1])
            # intersection is equal to A[0],min(B[1],A[1])
            intersection = [intervalA[0],min(intervalB[1],intervalA[1])]
            # if A[1] greater than B[1], we keep i, increase j
            if intervalA[1]>intervalB[1]:
                j+=1
            elif intervalA[1]<intervalB[1]:
                i+=1
            # if equal, increase both
            else:
                i+=1
                j+=1
            result.append(intersection)
        elif (intervalB[0]>=intervalA[0] and intervalB[0]<=intervalA[1]): # means that A[0], B[0],min(B[1],A[1]),max(B[1],A[1])
            intersection = [intervalB[0],min(intervalB[1],intervalA[1])]
            if intervalA[1]>intervalB[1]:
                j+=1
            elif intervalA[1]<intervalB[1]:
                i+=1
            # if equal, increase both
            else:
                i+=1
                j+=1
            result.append(intersection)
        else: # no intersection, we keep the one with higher interval
            if intervalA[0]>intervalB[1]:
                j+=1
            elif intervalB[0]>intervalA[1]:
                i+=1
    return result