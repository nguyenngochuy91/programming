# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:52:15 2019

@author: huyn
"""

# given a graph, check if it is a tree (no cycle, and all connected)
def isTree(matrix):
    n = len(matrix)
    numberOfConnected = 0
    visited = [False]*n
    def dfs(visited,currentNode,parentNode,n):
        for node in range(n):
            if visited[node] and node !=parentNode and matrix[currentNode][node]:
                return True
            elif not visited[node] and matrix[currentNode][node]:
                visited[node]= True
                if dfs(visited,node,currentNode,n):
                    return True
        return False
    for node in range(n):
        if not visited[node]:
            numberOfConnected+=1
            visited[node]=True
            if dfs(visited,node,None,n):
                return False
#    print (numberOfConnected)
    return numberOfConnected==1