# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:01:25 2019

@author: huyn
"""

#221. Maximal Square
#Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    arr = []
    output = 0
    for i in range(row-1,-1,-1):
        for j in range(col-1,-1,-1):
            if matrix[i][j]=="1":
                val= min(arr[i][j+1],arr[i+1][j],arr[i+1][j+1])+1
                arr[i][j]=val
                output   = max(val,output)
    return output**2