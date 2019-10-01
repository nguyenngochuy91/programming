# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:58:38 2019

@author: huyn
"""

#1023. Camelcase Matching
#A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. 
#(We may insert each character at any position, and may insert 0 characters.)
#
#Given a list of queries, and a pattern, return an answer list of booleans, where 
#answer[i] is true if and only if queries[i] matches the pattern.
    
def camelMatch(queries,pattern):
    res = []
    for query in queries:
        pointerQ = 0
        firstCheck = True
        for i in range(len(pattern)):
            patternLetter = pattern[i]
            queryLetter   = query[pointerQ]
            check         = True
            while patternLetter!=queryLetter:
                if patternLetter.isupper():
                    if queryLetter.islower():
                        pointerQ+=1
                        if pointerQ== len(query):
                            check = False
                            break
                        else:
                            queryLetter = query[pointerQ]
                    else:
                        check = False
                        break
                else: # pattern is low case
                    if queryLetter.islower():
                        pointerQ+=1
                        if pointerQ== len(query):
                            check = False
                            break
                        else:
                            queryLetter = query[pointerQ]
                    else:
                        check = False
                        break
            if not check:
                firstCheck= False
                break
            else:
                pointerQ+=1
                if pointerQ== len(query):
                    if i == len(pattern)-1:
                        break
                    else:
                        firstCheck = False
                        break
                else:
                    queryLetter = query[pointerQ]
        if firstCheck:
            flag= True
            for letter in query[pointerQ:]:
                if letter.isupper():
                    flag= False
                    break
            if flag:
                res.append(True)
            else:
                res.append(False)
        else:
            res.append(False)
    return res
