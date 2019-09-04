# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:46:44 2019

@author: huyn
"""
import heapq
from collections import deque
#The Ruler of HackerLand believes that every citizen of the country should have access to a library. 
#Unfortunately, HackerLand was hit by a tornado that destroyed all of its libraries and obstructed its roads! 
#As you are the greatest programmer of HackerLand, the ruler wants your help to repair the roads and build 
#some new libraries efficiently.
#
#HackerLand has  cities numbered from  to . The cities are connected by  bidirectional roads. 
#A citizen has access to a library if:
#
#Their city contains a library.
#They can travel by road from their city to a city containing a library.
#The following figure is a sample map of HackerLand where the dotted lines denote obstructed roads:
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib<=c_road:
        return c_lib*n
    d= {}

    for edge in cities:
        start,stop = edge
        if start not in d:
            d[start]=set()
        if stop not in d:
            d[stop]=set()
        d[start].add(stop)
        d[stop].add(start)
    # find connected component
    cc = []
    visited = set()
    while cities:
        start,stop = cities.pop()
        newComponent = []
        if start in visited or stop in visited:
            continue
        else:
            queue = [start]
            while queue:
                node = queue.pop()
                visited.add(node)
                heapq.heappush(newComponent,(-len(d[node]),node))
                for neighbor in d[start]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            cc.append(newComponent)
    minimum = 0
    for component in cc:
        minimum+=c_lib+c_road*(len(component)-1)
    return minimum
#    for component in cc:
        
#n, c_lib, c_road, cities=3,2,1,[[1, 2], [3, 1], [2, 3]]
#roadsAndLibraries(n, c_lib, c_road, cities)
#n, c_lib, c_road, cities=6 ,2, 5, [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]
#roadsAndLibraries(n, c_lib, c_road, cities)
    
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
#graph_nodes, graph_from, graph_to, ids, val= 4 ,[1, 1, 4] ,[2, 3, 2] ,[1, 2, 1, 1], 1
#findShortest(graph_nodes, graph_from, graph_to, ids, val)
graph_nodes, graph_from, graph_to, ids, val=5 ,[1, 1, 2, 3] ,[2, 3, 4, 5] ,[1, 2, 3, 3, 2] ,2
print(findShortest(graph_nodes, graph_from, graph_to, ids, val))