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

#DFS: Connected Cell in a Grid
def maxRegion(grid):
    row = len(grid)
    col = len(grid[0])
    def dfs(grid,x,y,row,col):
        size = 0
        if grid[x][y]:
            grid[x][y]=0
            size+=1
            temp = [(1,1),(-1,-1),(1,-1),(-1,1),
                    (0,1),(1,0),(0,-1),(-1,0)]
            for a,b in temp:
                newX,newY=x+a,b+y
                if newX>=0 and newX<row and newY>=0 and newY<col:
                    size+=   dfs(grid,newX,newY,row,col)
        return size
    myMax = 0
    for i in range(row):
        for j in range(col):
            myMax= max(myMax,dfs(grid,i,j,row,col))
    return myMax
#grid = [[1,1,0,0],
#        [0,1,1,0],
#        [0,0,1,0],
#        [1,0,0,0]
#        ]
#print (maxRegion(grid))

def minTime(roads, machines,n):
    
    d= {}
    minimal =0
    # if any of the machine share an edge, delete the edge,add the weight
#    for start,end,time in roads:
#        
    return 


#roads,machines=[[2, 1, 8], [1, 0, 5], [2, 4, 5], [1, 3, 4]] ,[2, 4, 0]
#print (minTime(roads, machines))
#roads,machines=[[0, 1, 4], [1, 2, 3], [1, 3, 7], [0, 4, 2]] ,[2, 3, 4]
#print (minTime(roads, machines))

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

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print (findRedundantConnection(edges))