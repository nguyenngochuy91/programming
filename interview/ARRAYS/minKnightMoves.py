# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:05:36 2019

@author: huyn
"""


def minKnightMoves(x: int, y: int) -> int:
    queue = deque([(0,0)])
    step = 0
    visited = set((0,0))
    while True:
        size= len(queue)
        for i in range(size):
            X,Y = queue.popleft()
            if X==x and Y==y:
                return step
            else:
                temp = [[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
                for a,b in temp:
                    newX,newY= X+a,Y+b
                    if (newX,newY) not in visited:
                        visited.add((newX,newY))
                        queue.append((newX,newY))
        step+=1
    return