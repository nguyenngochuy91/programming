# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:02:40 2019

@author: huyn
"""

#1162. As Far from Land as Possible
#Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 
#represents land, find a water cell such that its distance to the nearest land cell is 
#maximized and return the distance.
#
#The distance used in this problem is the Manhattan distance: the distance between 
#two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
#If no land or water exists in the grid, return -1.
def maxDistance(grid: List[List[int]]) -> int:
    n = len(grid)
    queue = deque([(i,j) for i in range(n) for j in range(n) if grid[i][j]])
    if len(queue)==n**2 or not queue:
        return -1
    depth = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            x,y = queue.popleft()
            position = [(0,1),(1,0),(0,-1),(-1,0)]
            for a,b in position:
                vX,vY = x+a,y+b
                if vX>=0 and vX<n and vY>=0 and vY<n and grid[vX][vY]==0:
                    grid[vX][vY]=1
                    queue.append((vX,vY))
        depth+=1
    return depth-1