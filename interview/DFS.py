# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:39:06 2019

@author: huyn
"""
from os import walk
# finding a file in a directory
def findFile(directory,name):
    r =[]
    for (dirpath, dirnames, filenames) in walk(directory): 
        # exhast each dirnames
        for eachDir in dirnames:
            more = findFile(dirpath+"/"+eachDir,name)
            r.extend(more)
        for file in filenames:
            if name in file:
                r.append(file)
    return r
# find all valid parentheses
def findValidPermutationParentheses(n):
    r=[]
    left = right = n
    addParenthese(left,right,2*n,r,[])
    return r
def addParenthese(left,right,size,r,temp):
    if len(temp)==size:
        r.append("".join(temp))
    if left>0:
        temp.append("(")
        addParenthese(left-1,right,size,r,temp)
        temp.pop()
    if right>left: # important 
        temp.append(")")
        addParenthese(left,right-1,size,r,temp)
        temp.pop()
        
# medium problem


def calcEquation(equations, values, queries):
    # Write your code here
    d = {}
    for i in range(len(equations)):
        x,y = equations[i]
        k = values[i]
        if x not in d:
            d[x]={}
        if y not in d:
            d[y]={}
        d[x][y]=k 
        d[y][x] = 1/k 
    def dfs(a,b,currentValue,visited):
        if a not in d or b not in d:
            return  
        else:
            res = None
            for neighbor in d[a]:
                value = d[a][neighbor]
                if neighbor==b:
                    return currentValue*value 
                elif neighbor not in visited:
                    res = dfs(neighbor,b,currentValue*value,visited+neighbor) 
            return res
    res = []
    for query in queries:
        x,y = query 
        v = dfs(x,y,1.0,"")
        if v==None:
            res.append(-1.0)
        else:
            res.append(v)
    return res
#equations = [["a","b"],["b","c"]]
#values    = [2.0,3.0]
#queries = [["a","c"],["b","a"],["a","e"]]
#print (calcEquation(equations,values,queries))
    
# restore ip addresses
# given a string containing only digits, restore it by returning all possible valid IP address combinations
def restoreIpAddresses(s):
    # Write your code here
    res = []
    def dfs(s,index,current):
        if len(current)==4 and index==len(s):
            res.append(".".join(current))
        elif len(current)<4:
            for i in range(1,4):
                if index+i<=len(s):
                    item = int(s[index:index+i])
                    if item>=0 and item<256:
                        current.append(s[index:index+i])
                        dfs(s,index+i,current)
                        current.pop()
                    else:
                        break
                
  
    dfs(s,0,[])
    return res
#s = "25525511135"
#print(restoreIpAddresses(s))
    
#letter combinations of a phone number, given a string "2-9", return all possible letter combinations that the number could present
def letterCombinations(digits):
    # Write your code here
    res =[]
    d= {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

    def dfs(digits,current,index):
        if index ==len(digits):
            res.append(current)
        elif index<len(digits):
            digit = int(digits[index])
            for letter in d[digit]:
                dfs(digits,current+letter,index+1) 
    dfs(digits,"",0)
    return res
    
# boggle game
def exist(board, word):
    # Write your code here
    row = len(board)
    col = len(board[0])
    def dfs(currentX,currentY,index,visited):
        if index==len(word):
            return True
        elif index<len(word):
            temp = [(0,1),(1,0),(-1,0),(0,-1)]
            check = False
            for x,y in temp:
                a,b= currentX+x,currentY+y
                if a>=0 and a<row and b>=0 and b<col and (a,b) not in visited:
                    if word[index]==board[a][b]:
                        visited.append((a,b))
                        check = dfs(a,b,index+1,visited)
                        visited.pop()
                if check:
                    break 
            return check
    for i in range(row):
        for j in range(col):
            if dfs(i,j,0,[]):
                return True
    return False
#1079. Letter Tile Possibilities
#        You have a set of tiles, where each tile has one letter tiles[i] printed on it.  
#        Return the number of possible non-empty sequences of letters you can make.
def numTilePossibilities(tiles):
    res = []
    def dfs(tiles,index,current):
        if index==len(tiles):
            if current not in res:
                res.append(current)
        if index<len(tiles):
            dfs(tiles,index+1,current+tiles[index])
            dfs(tiles,index+1,current)
    dfs(tiles,0,"")
    return res
#print (numTilePossibilities("AAB"))
#print (numTilePossibilities("AAABBC"))

# remove the least amount of parenthese to make valid
#301. Remove Invalid Parentheses
def removeInvalidParentheses(s):
    
    return