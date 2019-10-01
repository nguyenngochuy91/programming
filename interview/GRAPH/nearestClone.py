# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:51:11 2019

@author: huyn
"""

# find the nearest clone
# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    edges = {}
    for i in range(len(graph_from)):
        start = graph_from[i]
        stop  = graph_to[i]
        if start not in edges:
            edges[start]=[]
        if stop not in edges:
            edges[stop]=[]
        edges[start].append(stop)
        edges[stop].append(start)
    colors = set()
    for i in range(len(ids)):
        if ids[i]==val:
            colors.add(i+1)
    if len(colors)<=1:
    
        return -1
    minimum = float("inf")
    visited = set()
    for id in colors:
        if id in visited:
            continue
        visited.add(id)
        queue = deque([])
        count = 1
        for neighbor in edges[id]:
            if neighbor not in visited:
                queue.append(neighbor)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                visited.add(node)
                if ids[node-1]==val:
                    minimum= min(minimum,count)
                    break
                for neighbor in edges[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            count+=1
    return minimum