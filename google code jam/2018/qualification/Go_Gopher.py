import sys

def solve(D,string):
    if string.count("S")>D:
        return "IMPOSSIBLE"

    currentTotal = 0
    gunValue =[]
    initial = 1
    totals  = []
    for letter in string:
        if letter=="C":
            initial+=initial
        else:
            currentTotal+=initial
        totals.append(currentTotal)
        gunValue.append(initial)
    if currentTotal <=D:
        return 0
    count = 0
    while True: # while there are still CS available
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
            currentTotal = totals[indexOfC-1]
            initial = gunValue[indexOfC-1]
            # we swap CS into SC
            string[indexOfC]= "S"
            string[indexOfC+1]= "C"
            for i in range(indexOfC,len(string)):
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
                
T = int(input())
for i in range(1, T + 1):
    D, string = input().split()
    result = solve(int(D),list(string))
    print("Case #{}: {}".format(T, result))
    sys.stdout.flush()