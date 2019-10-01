# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:00:25 2019

@author: huyn
"""
import heapq,typing
from collections import deque
class TreeNode(object):
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
# given a graph where vertices are cities, edge between vertices are bridges, with weight
# given a graph, indicate by list of list, where each element of list [startNode,endNode,weight],
# a source node, an end node, and k. Find the minimum weight path from source to end within k steps.
def findCheapestPrice(n, flights, src, dst, k):
    k+=1
    # Write your code here
    # initiate our priority queue
    priorityQueue = []
    # initiate our distance as a dictionary
    distances = {i:float("inf") for i in range(n)}
    # generate a graph using our flights info
    graphs = {}
    # update this using our flights info 
    for flight in flights:
        start,end,cost = flight 
        if start not in graphs:
            graphs[start]={}
        graphs[start][end] = cost 
    # push our src into the queue, each of item in queue store 
    heapq.heappush(priorityQueue,(0,src,0))
    # set distance to source as 0
    distances[src]=0
    while len(priorityQueue)!=0:
        print (priorityQueue)
        current_distance,current_vertex, current_step = heapq.heappop(priorityQueue)
        if current_vertex not in graphs:
            continue 
        if current_vertex == dst:
            return current_distance
        for neighbor in graphs[current_vertex]:
            neighbor_distance = graphs[current_vertex][neighbor]
            # find the distance from src to this neighbor through our current_vertex 
            distance = distances[current_vertex]+neighbor_distance 
            # if this distance is currently less than the neighbor and the step +1 does not get over k, we insert it back 
            if current_step+1<=k and distance<=distances[neighbor]:
                distances[neighbor] = distance 
                heapq.heappush(priorityQueue,(distance,neighbor,current_step+1))
    if distances[dst]==float("inf"):
        return -1 
    else:
        return distances[dst]
    
#1161. Maximum Level Sum of a Binary Tree
#Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

#Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
def maxLevelSum(self, root: TreeNode) -> int:
    currentL = 1
    bestL,maxSum = 0,-float("inf")
    queue = deque([root])
    while queue:
        currentSum,size = 0,len(queue)
        for _ in range(size):
            node = queue.popleft()
            currentSum+=node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if currentSum>maxSum:
            bestL = currentL
            maxSum = currentSum
        currentL+=1
    return bestL