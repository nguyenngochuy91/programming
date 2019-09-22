# -*- coding: utf-8 -*-
"""
Problem

An alien robot is threatening the universe, using a beam that will destroy all algorithms knowledge. We have to stop it!

Fortunately, we understand how the robot works. It starts off with a beam with a strength of 1, and 
it will run a program that is a series of instructions, which will be executed one at a time, in left to right order. 
Each instruction is of one of the following two types:

C (for "charge"): Double the beam's strength.
S (for "shoot"): Shoot the beam, doing damage equal to the beam's current strength.
For example, if the robot's program is SCCSSC, the robot will do the following when the program runs:

Shoot the beam, doing 1 damage.
Charge the beam, doubling the beam's strength to 2.
Charge the beam, doubling the beam's strength to 4.
Shoot the beam, doing 4 damage.
Shoot the beam, doing 4 damage.
Charge the beam, increasing the beam's strength to 8.

In that case, the program would do a total of 9 damage.

The universe's top algorithmists have developed a shield that can withstand a maximum total of D damage. 
But the robot's current program might do more damage than that when it runs.

The President of the Universe has volunteered to fly into space to hack the robot's program before the robot runs it. 
The only way the President can hack (without the robot noticing) is by swapping two adjacent instructions. 
For example, the President could hack the above program once by swapping the third and fourth instructions to make it SCSCSC. 
This would reduce the total damage to 7. Then, for example, the president could hack the program again to make it SCSSCC, 
reducing the damage to 5, and so on.

To prevent the robot from getting too suspicious, the President does not want to hack too many times. 
What is this smallest possible number of hacks which will ensure that the program does no more than D total damage, 
if it is possible to do so?

Input

The first line of the input gives the number of test cases, T. T test cases follow. 
Each consists of one line containing an integer D and a string P: the maximum total damage our shield can withstand, 
and the robot's program.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y 
is either the minimum number of hacks needed to accomplish the goal, or IMPOSSIBLE if it is not possible.
"""
import sys,random
from itertools import product
def solve(D,string):
    string = list(string)
    if string.count("S")>D:
        return "IMPOSSIBLE"

    currentTotal = 0
    gunValue =[]
    initial = 1
    for letter in string:
        if letter=="C":
            initial+=initial
        else:
            currentTotal+=initial
        gunValue.append(initial)
    if currentTotal <=D:
        return 0
    count = 0
    indexOfC = findSCReverse(string)
    while indexOfC!=-1: # while there are still CS available
        indexOfC = findSCReverse(string)
        count +=1
        if indexOfC==0:
            # this means we substract 1 out of the total
            currentTotal-=1
            # we swap CS into SC
            string[indexOfC]= "S"
            string[indexOfC+1]= "C"
        else:
            # we wll recalculate our current Total
            # set up current Total, and current initial
            currentTotal = 0
            initial      = 1
            # we swap CS into SC
            string[indexOfC]= "S"
            string[indexOfC+1]= "C"

            for letter in string:
                if letter=="C":
                    initial+=initial
                else:
                    currentTotal+=initial
                        
        if currentTotal<=D:
            return count
            
def findSCReverse(string):
    for i in range(len(string)-1,0,-1):
        if string[i] == "S" and string[i-1]=="C":
            return i-1
    return -1
                
#T = int(input())
#for i in range(1, T + 1):
#    D, string = input().split()
#    result = solve(int(D),list(string))
#    print("Case #{}: {}".format(T, result))
#    sys.stdout.flush()
    
def solve1(D,comp):
    count = 0
    comp = list(comp)
    D= int(D)
    init = []
    current = 1
    total = 0
    for l in comp:
        if l =="C":
            current*=2
        else:
            total+=current
            count+=1
        init.append(current)
    if total<=D:
        return 0
    if count >D:
        return "IMPOSSIBLE"
    r = 0
    size = len(comp)
#    print (init)
#    print (comp)
    index = findSC1(comp,size)
    while index!=-1:
        if index==0:
            total-=1
        else:
            total-=init[index-1]
        r+=1
        if total<=D:
            return r
        comp[index]="S"
        comp[index+1]="C"
        for i in range(index,size):
            if comp[i]=="S":
                init[i]=init[i-1]
            else:
                init[i]=init[i-1]*2
#        print (init)
#        print (comp)  
        index = findSC1(comp,size)


def findSC1 (comp,size):
    for i in range(size-1,0,-1):
        if comp[i]=="S" and comp[i-1]=="C":
            return i-1
    return -1
for p in product("SC",repeat=8):
    D = random.randint(1,10^2)
    p = "".join(list(p))
    r = solve(D,list(p))
    try:
        r1 = solve1(D,list(p))
    except TypeError:
        print (TypeError,D,p)
        break
    if r!=r1:
        print (D,p,r,r1)
