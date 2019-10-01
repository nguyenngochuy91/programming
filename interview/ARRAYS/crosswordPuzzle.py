# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:03:58 2019

@author: huyn
"""

##Crossword Puzzle
def crosswordPuzzle(crossword, words):
    crossword = [list(word) for word in crossword]
    vertical = findVertical(crossword)
    horizontal = findHorizontal(crossword)
    wordDictionary = lengthToWord(words)
    # we solve our crossword based on the horizonal and vertical, and the length of the word
    # we find the word to fit in first but recursive solve for each length
    lengths = list(wordDictionary.keys())
    solveLength(crossword,0,lengths,vertical,horizontal,wordDictionary)
    crossword = ["".join(word) for word in crossword]
    print (crossword)
# for a given length, fill all possible word of that length in to the crossword
def solveLength(crossword,index,lengths,vertical,horizontal,wordDictionary):
    if index == len(lengths):
        return True
    length   = lengths[index]
    wordList = wordDictionary[length]
    perm = permutations(wordList)
    for potential in list(perm):
        canFill = fill(crossword,horizontal,vertical,potential,length)
        if canFill:
            nextStep = solveLength(crossword,index+1,lengths,vertical,horizontal,wordDictionary)
        else:
            nextStep = False
        if nextStep:
            break
    return nextStep
# this try to fill our current length for our crossword,return True if nothing conflicts, else , return False
def fill(crossword,horizontal,vertical,potential,length):
    try:
        toFillHorizontal = horizontal[length]
    except:
        toFillHorizontal = None
    try:
        toFillVertical = vertical[length]
    except:
        toFillVertical = None   
    check = True
    filled = set()
#    print()
#    print (length)
#    print (crossword)
#    print (toFillHorizontal)
#    print (toFillVertical)
    tempH = []
    tempV  = []
    for word in potential:
        if toFillHorizontal:
            r,c = toFillHorizontal.pop()
            tempH.append((r,c))
            for i in range(length):
                if crossword[r][c]!= "-" and crossword[r][c]!=word[i]: 
                # has a letter in it already, then wrong
                    check= False
                    break
                elif crossword[r][c]=="-":
                    crossword[r][c]=word[i]
                    filled.add((r,c))
                c+=1
        else:
            if toFillVertical:
                r,c = toFillVertical.pop()
                tempV.append((r,c))
                for i in range(length):
                    if crossword[r][c]!="-" and crossword[r][c]!=word[i]: 
                    # has a letter in it already, then wrong
                        check= False
                        break
                    elif crossword[r][c]=="-":
                        crossword[r][c]=word[i]
                        filled.add((r,c))
                    r+=1
            else:
                check = False
                break
    if not check:
        # we have to undo any filling
        for r,c in filled:
            crossword[r][c]="-"
        horizontal[length].extend(tempH)
        vertical[length].extend(tempV)
    return check
def findVertical(crossword):
    d ={}
    row = len(crossword)
    col = len(crossword[0])
    for c in range(col):
        r = 0
        found = False
        length = 0
        while r<row:
            if crossword[r][c]=="-":
                if not found:
                    start= (r,c)
                length+=1
                found = True
            else:
                if found: # we are done with 1 segment
                    if length not in d:
                        d[length]= []
                    d[length].append(start)
                    length=0
                found = False
            r+=1
        if found:
            if length not in d:
                d[length]= []
            d[length].append(start)            
    if 1 in d:
        d.pop(1)
    return d
    
def findHorizontal(crossword):
    d ={}
    row = len(crossword)
    col = len(crossword[0])
    for c in range(row):
        r = 0
        found = False
        length = 0
        while r<col:
            if crossword[c][r]=="-":
                if not found:
                    start= (c,r)
                length+=1
                found = True
            else:
                if found: # we are done with 1 segment
                    if length not in d:
                        d[length]= []
                    d[length].append(start)
                    length=0
                found = False
            r+=1
        if found:
            if length not in d:
                d[length]= []
            d[length].append(start)            
    if 1 in d:
        d.pop(1)
    return d

def lengthToWord(words):
    d= {}
    for word in words:
        if len(word) not in d:
            d[len(word)]= []
        d[len(word)].append(word)
    return d
    
#crossword = ['+-++++++++', '+-++++++++', '+-++++++++', '+-----++++', '+-+++-++++', '+-+++-++++', '+++++-++++', '++------++', '+++++-++++', '+++++-++++']
#words = ["LONDON","DELHI","ICELAND","ANKARA"]
#crosswordPuzzle(crossword,words)
#crossword = ['+-++++++++', '+-++++++++', '+-------++', '+-++++++++', '+-++++++++', '+------+++', '+-+++-++++', '+++++-++++', '+++++-++++', '++++++++++']
#words = ["AGRA","NORWAY","ENGLAND","GWALIOR"]
#crosswordPuzzle(crossword,words)
#crossword = ['XXXXXX-XXX', 'XX------XX', 'XXXXXX-XXX', 'XXXXXX-XXX', 'XXX------X', 'XXXXXX-X-X', 'XXXXXX-X-X', 'XXXXXXXX-X', 'XXXXXXXX-X', 'XXXXXXXX-X']
#words = ["ICELAND","MEXICO","PANAMA","ALMATY"]
#crosswordPuzzle(crossword,words)
###############################################################################