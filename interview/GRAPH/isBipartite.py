# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:52:31 2019

@author: huyn
"""

#785. Is Graph Bipartite?
def isBipartite(graph):
    d = {}
    for node,neighbors in enumerate(graph):
        if node not in d: # have not assign this node, that means any of the edge was not assigned neither
            stack = [node]
            d[node] = 0 
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in d:
                        stack.append(neighbor)
                        d[neighbor]= 1-d[node]
                    elif d[neighbor]==d[node]:
                        return False
    return True