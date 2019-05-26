# -*- coding: utf-8 -*-
"""

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