# -*- coding: utf-8 -*-
"""

"""
import sys
T = int(input().strip())
def solve(instructions,R,C,SR,SC):
    d = {"R":{},"C":{}}
    d["R"][SC]=[[SR,SR]]
    d["C"][SR] = [[SC,SC]]
    visited = set()
    visited.add((SR,SC))
    for instruction in instructions:
        if instruction=="N":
            SR-=1
            if (SR,SC) in visited:
                # look at the array of interval of SR
                rowIntervals = insertInterval(d["R"][SC],SR,-1)
                d["R"][SC] = rowIntervals
        elif instruction == "S":
            SR+=1
            if (SR,SC) in visited:
                # look at the array of interval of SR
                rowIntervals = insertInterval(d["R"][SC],SR,1)
                d["R"][SC] = rowIntervals
        elif instruction =="E":
            SC+=1
            if (SR,SC) in visited:
                # look at the array of interval of SR
                colIntervals = insertInterval(d["C"][SR],SC,1)
                d["C"][SR] = rowIntervals
        else:
            SC-=1  
            if (SR,SC) in visited:
                # look at the array of interval of SR
                colIntervals = insertInterval(d["C"][SR],SC,-1)
                d["C"][SR] = rowIntervals
        # now we update our d and visited
        visited.add((SR,SC))
        print (instruction,SR,SC)
    return SR,SC
            
def insertInterval(intervals,SR,toAdd):
    output = []
    i = 0
    while i <len(intervals):
        interval = intervals[i]
        if SR>=interval[0] and SR<=interval[1]:
            if toAdd==1:
                highestR=interval+1
                # check if we will have to merge
                if i+1<len(intervals):
                    newInterval = intervals[i+1]
                    if highestR>=newInterval[0] and highestR<=newInterval[1]: # merge
                        interval[1] = newInterval[1]
                        i= i+1
                    else:
                        interval[1]+=1
            else:
                lowestR = interval-1
                if i-1 >=0:
                    lastInterval = intervals[i-1]
                    if lowestR>=lastInterval[0] and lowestR<=lastInterval[1]:
                        interval[0]=lastInterval[0]
                        # we have to pop last item in output
                        output.pop()
                    else:
                        interval[0]-=1
  
        i+=1
        output.append(interval)
    output.append(newInterval)     
    return output
for i in range(T):
    N, R, C, SR , SC = [int(item) for item in input().split()]
    instructions = input()
    FR,FC = solve(instructions,R,C,SR,SC)
    print ("Case #{}: {} {}".format(i+1,FR,FC))