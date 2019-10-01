# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:59:27 2019

@author: huyn
"""

#1091. Shortest Path in Binary Matrix
#In an N by N square grid, each cell is either empty (0) or blocked (1).
#
#A clear path from top-left to bottom-right has length k if and only if it is composed of cells 
#C_1, C_2, ..., C_k such that:
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
#Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1
def shortestPathBinaryMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    k=0
    n = len(grid)-1
    if grid[0][0]==1 or grid[n][n]==1:
        return -1
    visited = set([(0,0)])
    current = set([(0,0)])
    while current:
        nextL = set()
        k+=1
        for node in current:
            x,y = node
            visited.add(node)
            if (x,y)==(n,n):
                return k
            temp = [(x-1,y-1),(x-1,y),(x-1,y+1),
                   (x,y-1),(x,y+1),
                   (x+1,y-1),(x+1,y),(x+1,y+1)]
            for t in temp:
                if t[0]>=0 and t[1]>=0 and t[0]<=n and t[1]<=n and t not in visited and grid[t[0]][t[1]]==0:
                    nextL.add(t)
        current = nextL
    return -1