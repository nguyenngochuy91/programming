# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:04:53 2019

@author: huyn
"""

def totalFruit(tree):            
    arr = []
    current=tree[0]
    count = 1
    for t in tree[1:]:
        if t==current:
            count+=1
        else:
            arr.append((current,count))
            count = 1
            current =t
    arr.append((current,count))
    if len(arr)<=1:
        return arr[0][1]
    maxSum = 0
    i = 0
    d= {}
    while i <len(arr)-1:
        if len(d)==0:
            firstCount =arr[i][1]
            firstType   = arr[i][0]
            d[firstType]=firstCount
            currentSum= firstCount
            j = i+1
        foundNew = False
        while j<len(arr):
            newType,newCount = arr[j]
            if newType not in d and len(d)==2:

                foundNew= True
                break
            elif newType not in d and len(d)==1:
                d[newType] = newCount
                currentSum+=newCount
            else:
                d[newType]+=newCount
                currentSum+=newCount
            j+=1
        maxSum = max(maxSum,currentSum)
        # if the while loop break because j == len(arr)
        if not foundNew:
            return maxSum
        else:
            # we found a newtype, increase index i until 1 of the number pop
            while True:
                currentType,currentCount = arr[i]
                d[currentType]-=currentCount
                currentSum -= currentCount
                if d[currentType]==0:
                    d.pop(currentType)
                    i+=1
                    break # we are done
                i+=1

            
    return maxSum
    
    