# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:46:44 2019

@author: huyn
"""
import heapq
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