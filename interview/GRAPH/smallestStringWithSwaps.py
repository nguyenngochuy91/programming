# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:53:17 2019

@author: huyn
"""

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