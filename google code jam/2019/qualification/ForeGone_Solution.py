# -*- coding: utf-8 -*-
"""
Problem

Someone just won the Code Jam lottery, and we owe them N jamcoins! However, 
when we tried to print out an oversized check, we encountered a problem. 
The value of N, which is an integer, includes at least one digit that is a 4... and 
the 4 key on the keyboard of our oversized check printer is broken.

Fortunately, we have a workaround: we will send our winner two checks for positive 
integer amounts A and B, such that neither A nor B contains any digit that is a 4, and A + B = N. 
Please help us find any pair of values A and B that satisfy these conditions.

Input

The first line of the input gives the number of test cases, T. 
T test cases follow; each consists of one line with an integer N.

Output

For each test case, output one line containing Case #x: A B, 
where x is the test case number (starting from 1), and A and B are positive integers as described above.
"""
import sys
T = int(input().strip())
def solve(number):
    A=[]
    B=[]
    for num in number[::-1]:
        if num=="4":
            A.append("2")
            B.append("2")
        elif num =="5":
            A.append("3")
            B.append("2")
        elif num!="0":
            val = int(num)
            A.append(str(val-1))
            B.append("1")
        else:
            A.append("0")
            B.append("0")
    A = "".join(A[::-1])
    B = "".join(B[::-1])
    return A,B
            
        

                
for i in range(T):
    sys.stdout.flush()
    number = input().strip()
    A,B = solve(number)
    print ("Case #{}: {} {}".format(i+1,A,B))