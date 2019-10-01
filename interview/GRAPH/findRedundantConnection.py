# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:51:51 2019

@author: huyn
"""

#684. Redundant Connection
#In this problem, a tree is an undirected graph that is connected and has no cycles.
#
#The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N),
# with one additional edge added. 
#The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
#
#The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, 
#that represents an undirected edge connecting nodes u and v.
#
#Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple 
#answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the
# same format, with u < v.
def findRedundantConnection(edges):
    d = {}
    n= 0 
    v= {}
    for i in range(len(edges)):
        start,stop = edges[i]
        if start not in d:
            d[start] = []
        if stop not in d:
            d[stop] = []
        d[start].append(stop)
        d[stop].append(start)
        n= max(n,stop)
        v[tuple(edges[i])] = i
    visited = {i+1:False for i in range(n)}
    myPath = []
    def dfs(currentNode,parent,path):
        check = False
        for neighbor in d[currentNode]:
            if parent!=neighbor:
                if visited[neighbor]: # we hit a circle 
                    
                    path.append([currentNode,neighbor])
#                    print (path,currentNode,neighbor,"visited")
                    # get the cycle
#                    print (path)
                    for i in range(len(path)):
                        edge = path[i]
#                        print (edge)
                        if edge[0]!=neighbor:
                            continue
                        else:
                            break
                    for i in range(i,len(path)):
                        edge = path[i]
                        myPath.append(tuple(sorted(edge)))
#                    print (myPath)
                    return True
                elif neighbor in d:
                    visited[neighbor]= True
#                    print (currentNode,neighbor)
                    path.append([currentNode,neighbor])
                    check = dfs(neighbor,currentNode,path)
                    if check:
                        break
                    path.pop()
        return check
    for i in range(1,n+1):
        if not visited[i] and i in d:
            visited[i]= True
            check = dfs(i,None,[])
            if check:
                break

    edge= None
    index = 0
#    print (myPath)
    
    for path in myPath:
        if v[path]>index:
            index= v[path]
            edge =list(path)   
    return edge