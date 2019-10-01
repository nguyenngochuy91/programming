# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:55:43 2019

@author: huyn
"""

def maxSumIncreasingSubsequence(array):
    activeLists= [[array[0]]]
    for i in range(1,len(array)):
        item = array[i]
        index = findCeiling([activeList[-1] for activeList in activeLists],item)
        if array[index]==item: # equal then we just continue
            continue
        else:
            if index ==-1: # it is the smallest,case 1
                activeLists.insert(0,[item])
            elif index == len(array)-1: # it is the largest, case 2
                temp =[]
                for num in activeLists[-1]:
                    temp.append(num)
                temp.append(item)
                activeLists.append(temp)
            else: # case 3, we can actually merge with the above, but for the sake of clarity
                temp = []
                for num in activeLists[index]:
                    temp.append(num)
                temp.append(item)
                # we need to remove all the have same length as this temp
                length = len(temp)
                new = []
                for activeList in activeLists:
                    if len(activeList)==length:
                        continue
                    else:
                        new.append(activeList)
                # insert temp at the correct index
                new.insert(index+1,temp)
                activeLists = new    
    return max([sum(activeList) for activeList in activeLists])