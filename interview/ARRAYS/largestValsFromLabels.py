# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:59:36 2019

@author: huyn
"""

#1090. Largest Values From Labels
#We have a set of items: the i-th item has value values[i] and label labels[i].
#
#Then, we choose a subset S of these items, such that:
#
#|S| <= num_wanted
#For every label L, the number of items in S with label L is <= use_limit.
#Return the largest possible sum of the subset S.
def largestValsFromLabels(values, labels, num_wanted, use_limit):
    """
    :type values: List[int]
    :type labels: List[int]
    :type num_wanted: int
    :type use_limit: int
    :rtype: int
    """
    d = {}
    res = 0
    labelUse = {}
    for i in range(len(values)):
        label = labels[i]
        value = values[i]
        if value not in d:
            d[value] = {label:1}
        else:
            if label not in d[value]:
                d[value][label]=0
            d[value][label]+=1
    myList = sorted(d)


    while num_wanted:
        if myList:
            value = myList.pop(-1)
            # get the labels that have this value
            labels = d[value]
            for label in labels:
                labelCount = labels[label] # will have to check whether this label count cant be used and used how many times
                # get the number of this label already used
                if label not in labelUse:
                    labelUse[label]=0
                used = labelUse[label] 
                if used==use_limit:
                    pass # passed if already used to limit
                # else, add to the minimum of (use_limit-used,num_wanted)
                for i in range(min(use_limit-used,num_wanted,labelCount)):
                    res+=value
                    num_wanted-=1
                    labelUse[label]+=1

        else:
            break

    return res 