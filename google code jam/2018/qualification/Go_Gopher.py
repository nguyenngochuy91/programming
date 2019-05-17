"""
Problem
The Code Jam team has just purchased an orchard that is a two-dimensional matrix of cells of unprepared soil, 
with 1000 rows and 1000 columns. We plan to use this orchard to grow a variety of trees — AVL, 
binary, red-black, splay, and so on — so we need to prepare some of the cells by digging holes:

In order to have enough trees to use for each year's tree problems, we need there to be at least A prepared cells.
In order to care for our trees properly, the set of all prepared cells must form a single grid-aligned 
rectangle in which every cell within the rectangle is prepared.
Note that the above also implies that none of the cells outside of that rectangle can be prepared. 
We want the orchard to look tidy!

For example, when A=11, although the eleven prepared cells in the left figure 
below form a 3x4 rectangle (that is, with 3 rows and 4 columns), the cell in the center of the rectangle is not prepared. 
As a result, we have not yet completed preparing our orchard, since not every cell of the 3x4 rectangle is prepared. 
However, after just preparing the center cell, the rectangle of size at least 11 is fully filled, and the orchard is ready.

Input
T test Case
A : minimum required prepared rectangular area
process up to 1000 exchanges
Sending I,J: row, column to deploy gopher 2<=i,j<=999

after 1000
I=0 ,J=0 : Correct
I'=J'=-1: Incorrect
"""
import sys

def solve(A):
    
    return result
            

                
T = int(input())
for i in range(1, T + 1):
    A = int(input())
    print("Case #{}: {}".format(T, result))
    sys.stdout.flush()