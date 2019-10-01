# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:00:52 2019

@author: huyn
"""
import heapq
## #1129 Shortest Path with Alternating Colors
#Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, 
#each edge is either red or blue, and there could be self-edges or parallel edges.
#
#Each [i, j] in red_edges denotes a red directed edge from node i to node j.  
#Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.
#
#Return an array answer of length n, where each answer[X] is the length of the 
#shortest path from node 0 to node X such that the edge colors alternate along 
#the path (or -1 if such a path doesn't exist).
def shortestAlternatingPaths(n, red_edges, blue_edges):
    graph = {}
    answer = {}
    for i in range(n):
        answer[i]={}
        answer[i][0]=float("inf")
        answer[i][1] = float("inf")
    for edge in red_edges:
        start,stop = edge
        if start in graph:
            if 1 not in graph[start]:
                graph[start][1] = []

        else:
            graph[start]={}
            if 1 not in graph[start]:
                graph[start][1] = []    
        graph[start][1].append(stop)     
    for edge in blue_edges:
        start,stop = edge
        if start in graph:
            if 0 not in graph[start]:
                graph[start][0] = []

        else:
            graph[start]={}
            if 0 not in graph[start]:
                graph[start][0] = []    
        graph[start][0].append(stop)  
    answer[0]={0: 0, 1: 0}
    pq = []
    if 0 in graph:
        if 1 in graph[0]:
            for neighbor in graph[0][1]:
                heapq.heappush(pq,(1,neighbor,1))
        if 0 in graph[0]:
            for neighbor in graph[0][0]:
                heapq.heappush(pq,(1,neighbor,0))
#    print (graph,pq)
    while pq:
#        print (33,pq)
#        print (34,answer)
        distance,currentNode,currentColor  = heapq.heappop(pq)
        if distance <answer[currentNode][currentColor]:
            answer[currentNode][currentColor] = distance
        if currentNode not in graph:
            continue
        else:
            if (1-currentColor) not in graph[currentNode]:
                continue
            else:
                for neighbor in graph[currentNode][1-currentColor]:
                    neighborDistance = 1 + answer[currentNode][currentColor]
                    #print (neighbor,answer)
                    # check if the distance to this neighbor through currentNode is less than current Distance
                    if answer[neighbor][1-currentColor]>neighborDistance: # update and insert to our hp
                        answer[neighbor][1-currentColor] = neighborDistance
                        heapq.heappush(pq,(neighborDistance,neighbor,1-currentColor))
#        print (50,pq)
#        print (51,answer)
    output = [0]
#    print (pq,answer)
    for i in range(1,n):
        val= min(answer[i][0],answer[i][1])
        if val==float("inf"):
            output.append(-1)
        else:
            output.append(val)
    return output