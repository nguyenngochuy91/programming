# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:04:32 2019

@author: huyn
"""

#756. Pyramid Transition Matrix
#We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.
#
#We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.
#
#We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.
#
#Return true if we can build the pyramid all the way to the top, otherwise false.
def pyramidTransition(bottom,allowed):
    d= {}
    for x,y,z in allowed:
        if (x,y) not in d:
            d[(x,y)] = set()
        d[(x,y)].add(z)
    level = len(bottom)-1
#    print (d)
    def dfs(currentString,currentLevel,path):
#        print (currentString,currentLevel,path)
        if currentLevel ==0:
#            print (path)
            return True
        else:
            # this to store potential combination for upper level
            potentialNextLevel =[]
            for i in range(len(currentString)-1):
                first,second = (currentString[i],currentString[i+1])
                myTuple = (first,second)
                if myTuple not in d:
                    return False 
                else:
                    potential = d[myTuple]
                    potentialNextLevel.append(potential)
            arr  = set([""])
            for potential in potentialNextLevel:
                temp = set()
                for item in potential:
                    for string in arr:
                        temp.add(string+item)
                arr = temp
#            print (2385,arr)
            for string in arr:               
                path.append(string)
                check = dfs(string,currentLevel-1,path)
                if check:
                    return True
                path.pop()
            return False
    return dfs(bottom,level,[bottom])