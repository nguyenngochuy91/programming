# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:46:44 2019

@author: huyn
"""
import heapq
from collections import deque

# generate matrix given edges
def generate(arr,n):
    d= {}
    for x,y in arr:
        if x not in d:
            d[x]=[]
        if y not in d:
            d[y]=[]
        d[x].append(y)
        d[y].append(x)
    matrix = []
    for i in range(n):
        tmp= []
        if i not in d:
            matrix.append([0]*n)
            continue
        for j in range(n):
            if j in d[i]:
                tmp.append(1)
            else:
                tmp.append(0)
        matrix.append(tmp)
    return matrix
    



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
#print(findShortest(graph_nodes, graph_from, graph_to, ids, val))

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

#edges = [[1,2], [2,3], [3,4], [1,4], [1,5],[6,7],[8,9]]
#print (findRedundantConnection(edges))

#834. Sum of Distances in Tree
#An undirected, connected tree with N nodes labelled 0...N-1 and N-1 edges are given.
#
#The ith edge connects nodes edges[i][0] and edges[i][1] together.
#
#Return a list ans, where ans[i] is the sum of the distances between node i and all other nodes.
def sumOfDistancesInTree(N,edges):
    res = []
    return 
    
#given a graph, find the number of connected component
def numberOfConnectedComponent(matrix):
    size  =0
    n = len(matrix)
    visited = [False]*n
    def dfs(visited,current,n):
        for node in range(n):
            if matrix[current][node] and not visited[node]:
                visited[node]= True
                dfs(visited,node,n)
    for node in range(n):
        if not visited[node]:
            size+=1
            dfs(visited,node,n)
    return size
#matrix = [[False,True,False,True], 
# [True,False,True,False], 
# [False,True,False,True], 
# [True,False,True,False]]
#print (numberOfConnectedComponent(matrix))

#given a graph, and a vertex, find the size of connected component of that vertex
def dfsComponentSize(matrix, vertex):
    n = len(matrix)
    visited = [False]*n
    visited[vertex]= True
    def dfs(visited,current,n):
        size = 1
        for node in range(n):
            if matrix[current][node] and not visited[node]:
                visited[node]= True
                size+=dfs(visited,node,n)
        return size
    return dfs(visited,vertex,n)

#given a graph, get all the connected component, recursive style
def findAllConnectedComponentDFS(matrix):
    n = len(matrix)
    visited = [False]*n
    cc= []
    def dfs(visited,current,n):
        path =[current]
        for node in range(n):
            if matrix[current][node] and not visited[node]:
                visited[node]= True
                path.extend(dfs(visited,node,n))
        return path
    for node in range(n):
        if not visited[node]:
            visited[node]= True
            path = dfs(visited,node,n)
            cc.append(path)
    return cc
#arr = [[1,2],[2,3],[4,5],[7,8],[9,10],[10,11]]
#matrix = generate(arr,11)
#print (matrix)
#print (findAllConnectedComponentDFS(matrix))

#given a graph, get all the connected component, while style
def findAllConnectedComponentBFS(matrix):
    n = len(matrix)
    visited = [False]*n
    cc= []
    for node in range(n):
        if not visited[node]:
            queue = [node]
            visited[node] = True
            path  = []
            while queue:
                currentNode = queue.pop()
                path.append(currentNode)
                for neighbor in range(n):
                    if not visited[neighbor] and matrix[currentNode][neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            cc.append(path)
    return cc
#arr = [[1,2],[2,3],[4,5],[7,8],[9,10],[10,11]]
#matrix = generate(arr,11)
#print (matrix)
#print (findAllConnectedComponentBFS(matrix))

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
    
#arr = [[0,1],[1,2],[2,3],[3,4],[2,5],[4,6],[1,7],[5,0]]
#matrix = generate(arr,7)
#print (matrix)
#print (isTree(matrix))
    

# given a graph, check it has a cycle, using normal dfs
def hasCycle(matrix):
    n = len(matrix)
    visited = [False]*n
    def dfs(visited,currentNode,parentNode,n):
        for node in range(n):
            if matrix[currentNode][node]:
            # if the node is visited and not same as parent 
                if parentNode!=node and visited[node]:
                    return True
                elif not visited(node):
                    visited[node] = True
                    if dfs(visited,node,currentNode,n):
                        return True
        return False
    for node in range(n):
        if not visited[node]:
            visited[node] = True
            if dfs(visited,node,None,n):
                return True
    return False

# given a graph, check it has a cycle using coloring
def hasCycleColor(matrix):
    return

# given a graph, find all of its cycle
def getAllCycle(matrix):
    n  = len(matrix)
    
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
#graph = [[1,3], [0,2], [1,3], [0,2]]
#print (isBipartite(graph))
#graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
#print (isBipartite(graph))
def smallestStringWithSwaps(s, pairs) -> str:
    edges = {}
    for index in range(len(s)):
        edges[index]= []
    for x,y in pairs:
        edges[x].append(y)
        edges[y].append(x)
    visited= [False]*len(s)
    cc = []
    def dfs(currentIndex,component):
        for neighbor in edges[currentIndex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                component.append(neighbor)
                dfs(neighbor,component)
    for index in range(len(s)):
        if not visited[index]:
            visited[index]= True
            component     = [index]
            dfs(index,component)
            cc.append(sorted(component))

    s= list(s)
    for component in cc:

        stringComponent = [s[index] for index in component]
        stringComponent.sort()
#        print (stringComponent)
        for i in range(len(component)):
            indexToFillInS = component[i]
            letterToFill   = stringComponent[i]
            s[indexToFillInS] = letterToFill
    return "".join(s)

#s = "cba"
#pairs = [[0,1],[1,2]]
#print (smallestStringWithSwaps(s,pairs))
def nthUglyNumberNaive(n: int, a: int, b: int, c: int) -> int:
    a,b,c = sorted([a,b,c])
    array = [a,b,c]
    smallest= min(array)
    n-=1
    while n:
        if smallest == array[0]:
            array[0]+=a
            if array[1]==array[0]:
                array[1]+=b
            if array[2]==array[0]:
                array[2]+=c
        elif smallest ==array[1]:
            array[1]+=b
            if array[1]==array[0]:
                array[0]+=a
            if array[2]==array[1]:
                array[2]+=c
        else:
            array[2]+=c
            if array[1]==array[2]:
                array[1]+=b
            if array[2]==array[0]:
                array[0]+=a
        n-=1
        smallest= min(array)
        print(array)
    return smallest 
#5200. Sort Items by Groups Respecting Dependencies
#There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.
#
#Return a sorted list of the items such that:
#
#The items that belong to the same group are next to each other in the sorted list.
#There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
#Return any solution if there is more than one solution and return an empty list if there is no solution.
#
# 
def sortItems(n, m, group, beforeItems):
    d= {}
    for index in range(n):
        gr = group[index]
        
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
