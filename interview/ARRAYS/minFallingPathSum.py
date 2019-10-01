# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:58:10 2019

@author: huyn
"""

#931. Minimum Falling Path Sum
#
#Given a square array of integers A, we want the minimum sum of a falling path through A.
#
#A falling path starts at any element in the first row, and chooses one element from each row.  
#The next row's choice must be in a column that is different from the previous row's column by at most one.
    
def minFallingPathSum(A):
    r = len(A)
    c = len(A[0])
    for i in range(1,r):
        for j in range(c):
            if j==0:
                A[i][j] = A[i][j]+min(A[i-1][j],A[i-1][j+1])
            elif j==c-1:
                A[i][j] = A[i][j]+min(A[i-1][j-1],A[i-1][j])
            else:
                A[i][j] = A[i][j]+min(A[i-1][j],A[i-1][j+1],A[i-1][j-1])
    return min(A[r-1])