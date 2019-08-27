# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:39:06 2019

@author: huyn
"""
from os import walk
from typing import *
from math import log2
import random
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
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
    temp = set()
    def dfs(tiles,index,current):
        if index==len(tiles):
            if current not in temp:
                temp.add(current)
        if index<len(tiles):
            dfs(tiles,index+1,current+tiles[index])
            dfs(tiles,index+1,current)
    dfs(tiles,0,"")
    # for each item in res, we permute
    res =set()
    def permute(string,current):
        if not string and current not in res:
            res.add(current)
        for i in range(len(string)):
            item = string.pop(i)
            permute(string,current+item)
            string.insert(i,item)
    for string in temp:
        permute(list(string),"")
    return len(res)-1
#print (numTilePossibilities("AAB"))
#print (numTilePossibilities("TBAKNLM"))

        
#979. Distribute Coins in Binary Tree
#Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
#
#In one move, we may choose two adjacent nodes and move one coin from one node to another.  
#        (The move may be from parent to child, or from child to parent.)
#
#Return the number of moves required to make every node have exactly one coin.
def distributeCoins(root: TreeNode) -> int:  
    def dfs(root,parent):
        if root:
            root.extra =0 
            step = 0
            # set up the root.need right here
            # if it is a leaf node, any extra has to be pushed up, if it is 0, it needs 1 more from top down
            if not root.left and not root.right:
                root.extra = root.val-1
            elif root.left and root.right:
                step+= dfs(root.left,root)
                step+= dfs(root.right,root)
                root.extra+=root.val-1+root.left.extra+root.right.extra
            elif root.left:
                step+=dfs(root.left,root)
                root.extra+=root.val-1+root.left.extra
            elif root.right:
                step+=dfs(root.right,root)
                root.extra+=root.val-1+root.right.extra                
            return step

    return dfs(root,None)
#89. Gray Code
#The gray code is a binary numeral system where two successive values differ in only one bit.
#
#Given a non-negative integer n representing the total number of bits in the code, 
#print the sequence of gray code. A gray code sequence must begin with 0.
# 2 number different by 1 bit has difference is a 2 of power
def grayCode(n):
    mySet = [item for item in range(1,n+1)]
    res   = [0]
    def isValid(num1,num2):
        c = 0
        while num1 and num2:
            if num1%2 !=num2%2:
                if c==1:
                    return False
                else:
                    c+=1
            num1//=2
            num2//=2
        m = max(num1,num2)
        m = bin(m)[2:]
        for item in m:
            if m=="1":
                c+=1
        return c<=1
        
    def dfs(currentNum,mySet):
        if not mySet:
            return True
        else:
            check = False
            for i in range(len(mySet)):
                num = mySet.pop(i)
                if isValid(num,currentNum): # num is valid
#                    print (currentNum,num)
                    res.append(num)
#                    print (res,mySet)
                    check = dfs(num,mySet)
                    if not check:
                        res.pop()
                mySet.insert(i,num)
                if check:
                    break
            return check
    found = dfs(0,mySet)
    return res
#res= grayCode(30)
#1020. Number of Enclaves
#Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)
#
#A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.
#
#Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.
def numEnclaves( A) :
    row = len(A)
    col = len(A[0])
    count = 0
    global smallCount
    smallCount =0 
    def dfs(r,c):
        # set A[r][c]=0
#        print ("start {}",(r,c))
        global smallCount
        smallCount+=1
        A[r][c]=0
        t= [(0,1),(1,0),(0,-1),(-1,0)]
        overal = False
        for x,y in t:
            a,b = r+x,y+c
            if a>=0 and a<row and b>=0 and b<col and A[a][b]==1:
                check = dfs(a,b)
                if check:
                    overal=True
        if r==0 or c==0 or r== row-1 or c == col-1:
            return True
        return overal
    for r in range(row):
        for c in range(col):
            if A[r][c]:
                goodPath = dfs(r,c)
                print (r,c,goodPath,smallCount)
                if not goodPath:
                    count+=smallCount
                smallCount= 0 
    return count
#A=[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
#print (numEnclaves( A) )
#A=[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
#print (numEnclaves( A) )
def generate(n):
    arr= []
    for i in range(n):
        t= []
        for j in range(n):
            t.append(random.randint(0,1))
        arr.append(t)
    return arr
#947. Most Stones Removed with Same Row or Column
#On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
#
#Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
#
#What is the largest possible number of moves we can make?
def removeStones(stones):
    cc = []
    for stone in stones:
        
    return
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
stones = [[0,0]]
        