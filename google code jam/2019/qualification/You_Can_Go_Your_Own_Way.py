# -*- coding: utf-8 -*-
"""
Problem

You have just entered the world's easiest maze. You start in the northwest cell of an N by N grid of unit cells, 
and you must reach the southeast cell. You have only two types of moves available: a unit move to the east, 
and a unit move to the south. 
You can move into any cell, but you may not make a move that would cause you to leave the grid.

You are excited to be the first in the world to solve the maze, but then you see footprints. 
Your rival, Labyrinth Lydia, has already solved the maze before you, using the same rules described above!

As an original thinker, you do not want to reuse any of Lydia's moves. 
Specifically, if her path includes a unit move from some cell A to some adjacent cell B, 
your path cannot also include a move from A to B. 
(However, in that case, it is OK for your path to visit A or visit B, as long as you do not go from A to B.) 
Please find such a path.

Input

The first line of the input gives the number of test cases, T. T test cases follow; each case consists of two lines. 
The first line contains one integer N, giving the dimensions of the maze, as described above. 
The second line contains a string P of 2N - 2 characters, 
each of which is either uppercase E (for east) or uppercase S (for south), representing Lydia's valid path through the maze.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) 
and y is a string of 2N - 2 characters each of which is either uppercase E (for east) or uppercase S (for south), 
representing your valid path 
through the maze that does not conflict with Lydia's path, as described above. 
It is guaranteed that at least one answer exists.
"""
import sys
T = int(input().strip())
def solve(N,path):
    myPath = [(0,0)]
    current  = (0,0)
    for p in path:
        nextR = current[0]
        nextC = current[1]
        if p =="E":
            nextC+=1
        else:
            nextR+=1
        nextCurrent = (nextR,nextC)
        flip  = (nextC,nextR)
        myPath.append(flip)
        current = nextCurrent
    result = ""
    for i in range(len(myPath)-1):
        current = myPath[i]
        nextC   = myPath[i+1]
        if current[0]==nextC[0]:
            result+="E"
        else:
            result+="S"
    return result
            
        

                
for i in range(T):
    sys.stdout.flush()
    N = int(input().strip())
    path = input().strip()
    result = solve(N,path)
    print ("Case #{}: {}".format(i+1,result))