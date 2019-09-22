# -*- coding: utf-8 -*-
"""
Problem:
The diners at the Infinite House of Pancakes have gotten tired of circular pancakes, 
so the chefs are about to offer a new menu option: waffles! As a publicity stunt, 
they have made one large waffle that is a grid of square cells with R rows and C columns. 
Each cell of the waffle is either empty, or contains a single chocolate chip.

Now it is time for the chefs to divide up the waffle among their hungry diners. 
A horizontal cut runs along the entire gridline between two of the rows; a vertical 
cut runs along the entire gridline between two of the columns. For efficiency's sake, 
one chef will make exactly H different horizontal cuts and another chef will make exactly 
V different vertical cuts. This will conveniently create one piece for each of the (H + 1) × (V + 1) diners. 
The pieces will not necessarily all be of equal sizes, but that is fine; market research has shown 
that the diners do not care about that.

What the diners do care about is the number of chocolate chips they get, so each piece 
must have exactly the same number of chocolate chips. Can you determine whether the chefs can accomplish 
this goal using the given numbers of horizontal and vertical cuts?


Input
The first line of the input gives the number of test cases, T; T test cases follow. 
Each begins with one line containing four integers R, C, H, and V: the number of rows and 
columns in the waffle, and the exact numbers of horizontal and vertical cuts that the chefs must make. 
Then, there are R more lines of C characters each; the j-th character in the i-th of these lines represents 
the cell in the i-th row and the j-th column of the waffle. Each character is either @, 
which means the cell has a chocolate chip, or ., which means the cell is empty.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is 
POSSIBLE if the chefs can accomplish the goal as described above, or IMPOSSIBLE if they cannot.
"""

import sys
def solve(array,R,C,H,V):
    col1 = {}
    row1 = {}
    total1= 0
    for i in range(R):
        for j in range(C):
            if array[i][j]:
                total1+=1
                if i not in row1:
                    row1[i] = []
                if j not in col1:
                    col1[j] = []
                row1[i].append(j)
                col1[j].append(i)
    if total1== 0:
        return "POSSIBLE"
    if total1% (H+1)*(V+1):
        return "IMPOSSIBLE"
    count =0 
    for i in range(R):
        count +=len(row1[i])
        if count ==total1//2:
            break
        elif count >total1//2:
            return "IMPOSSBILE"
    count =0 
    for i in range(C):
        count +=len(col1[i])
        if count ==total1//2:
            break
        elif count >total1//2:
            return "IMPOSSBILE"    
    return "POSSIBLE"
def main():
    T = int(input())
    for i in range(1,T+1):
        R,C,H,V = [int(item) for item in input().split()]
        array   = []
        for r in range(R):
            row = [0 if item =="." else 1 for item in input()]
            array.append(row)
        result = solve(array,R,C,H,V)
        print ("Case #{}: {}".format(i,result))
main()