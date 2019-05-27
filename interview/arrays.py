# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:43:28 2019

@author: Huy Nguyen
"""
# finding the maximum sum of the contiguous sub-array of a given array
def findContiguousMaxSum(array):
    output = 0
    localMax = 0
    for number in array:
        localMax = max(0,localMax+number)
        output = max(output,localMax)
    return output

#array = [10,-1,2,4,10,-11,5,-20,4,10,25,-100,5,5,4,1,2,3]
#print (findContiguousMaxSum(array))

# finding the contiguous sub-array that has the maximum sum of a given array
def findContiguousArrayMaxSum(array):
    output = 0
    localMax = 0
    start = 0
    localStart = 0
    stop = 0
    for i in range(len(array)):
        number = array[i]
        if localMax<=0:
            localStart = i
        localMax = max(0,localMax+number)
        if output<localMax:
            start = localStart
            stop = i
        output = max(output,localMax)
    return array[start:stop+1] if stop!=0 else []
#array=[-1,-2,-3,-5]
#print (findContiguousArrayMaxSum(array))

# find missing number in linear runtime and constant extra space
def findMissingNumber(array):
    n = len(array)
    return n*(n+1)//2-sum(array)
    
# given an array, find contiguous sub-array that adds up to a given number n, all numbers are positive
def findContiguousArrayWithSum(array,n):
    start = 0
    stop  = 0
    currentSum = array[0]
    size = len(array)
    # have 2 pointers moving to the right
    while start<=stop and stop<=size-1:
#        print (start,stop,currentSum)
        if currentSum == n:
            return start,stop
        else:
            if currentSum<n:
                # increase stop
                stop+=1
                currentSum+=array[stop]
            else:
                currentSum-=array[start]
                start+=1
                stop = max(stop,start)
    return -1
#array = [10,0,2,4,10,5,4,0,25,5,5,4,1,2,3]
#print (findContiguousArrayWithSum(array,34))

# array contains only 0,1,2, sort the array
def sort012Dict(array):
    output = []
    d = {0:0,1:0,2:0}
    for item in array:
        d[item]+=1
    output.extend([1]*d[1])
    output.extend([2]*d[2])
    output.extend([0]*d[0])
    return output                
    
#  array contains only 0,1,2, sort the array in place from left
def sort012Left(array):
    zero = 0
    one  = 0
    two  = len(array)-1
    while one <=two:
        if array[one]==0:
            array[zero],array[one] = array[one],array[zero]
            zero+=1
            one+=1
        elif array[one]==1:
            one+=1
        else:
            array[one],array[two]= array[two],array[one]
            two-=1
    
    return array
#array = [1, 0, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
#print (sort012Left(array))

#  array contains only 0,1,2, sort the array in place from left
def sort012Right(array):
    zero = 0
    one  = len(array)-1
    two  = len(array)-1
    while zero <=one:
        if array[one]==0:
            array[zero],array[one] = array[one],array[zero]
            zero+=1
        elif array[one]==1:
            one-=1
        else:
            array[one],array[two]= array[two],array[one]
            two-=1
            one-=1
    
    return array
#array = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
#print (sort012Right(array))
    
def equilibirum(array):
    mySum = sum(array)
    if mySum%2:
        return -1
    current = 0
    for index in range(len(array)):
        current+=array[index]
        if current*2 == mySum:
            return index
    return -1

# longest increase subsequence O(n)
def longestIncreasingSubsequence(array):
    L = [[array[0]]]
    for i in range(1,len(array)):
        number = array[i]
        local  = 0
        new_array = None
        for j in range(len(L)):
            local_array = []
            arr       = L[j]
            local_array.extend(arr)
            if local_array[-1]<number:
                local_array.append(number)
            else:
                local_array = [number]
            if len(local_array)>local:
                local = len(local_array)
                new_array = local_array
        L.append(new_array)
    return L[-1]
#array = [10,22,9,33,21,50,41,60,80, 3, 10, 7, 40, 80]
#print (longestIncreasingSubsequence(array))
# given a sorted array, find a given key
def binarySearch(array,key):
    start = 0
    stop = len(array)-1
    while start<=stop:
        mid = (start+stop)//2        
        if array[mid] == key:
            return mid
        elif array[mid]<key:
            start = mid+1
        else:
            stop = mid-1
    return -1
# given an array, find the index so that array[index]<=key and array[index+1]>key, return -1 if key is the smallest, and
# length array-1 if key is the largest
def findCeiling(array,key):
    start = 0
    stop  = len(array)-1
    while start <=stop:
        mid = (start+stop)//2
        if array[mid]<=key:
            start = mid+1
        else:
            stop = mid-1
    return stop

def findFloor(stop,key):
    start = 0
    while start <=stop:
        mid = (start+stop)//2
        if mid<=key:
            start = mid+1
        else:
            stop = mid-1
    return start
# longest increase subsequence O(n)
#    1. If A[i] is smallest among all end 
#   candidates of active lists, we will start 
#   new active list of length 1.
#2. If A[i] is largest among all end candidates of 
#  active lists, we will clone the largest active 
#  list, and extend it by A[i].
#
#3. If A[i] is in between, we will find a list with 
#  largest end element that is smaller than A[i]. 
#  Clone and extend this list by A[i]. We will discard all
#  other lists of same length as that of this modified list.
def longestIncreasingSubsequenceFast(array):
    activeLists= [[array[0]]]
    for i in range(1,len(array)):
        item = array[i]
        index = findCeiling([activeList[-1] for activeList in activeLists],item)
        if array[index]==item: # equal then we just continue
            continue
        else:
            if index ==-1: # it is the smallest,case 1
                activeLists.insert(0,[item])
            elif index == len(array)-1: # it is the largest, case 2
                temp =[]
                for num in activeLists[-1]:
                    temp.append(num)
                temp.append(item)
                activeLists.append(temp)
            else: # case 3, we can actually merge with the above, but for the sake of clarity
                temp = []
                for num in activeLists[index]:
                    temp.append(num)
                temp.append(item)
                # we need to remove all the have same length as this temp
                length = len(temp)
                new = []
                for activeList in activeLists:
                    if len(activeList)==length:
                        continue
                    else:
                        new.append(activeList)
                # insert temp at the correct index
                new.insert(index+1,temp)
                activeLists = new

    return activeLists[-1]
                
#array = [10,22,9,33,21,50,41,41,60,60,80]
#print (longestIncreasingSubsequenceFast(array))    
# find the sum of maximum Sum increasing subsequence
# same idea, however, return the max sum out of all sum
def maxSumIncreasingSubsequence(array):
    activeLists= [[array[0]]]
    for i in range(1,len(array)):
        item = array[i]
        index = findCeiling([activeList[-1] for activeList in activeLists],item)
        if array[index]==item: # equal then we just continue
            continue
        else:
            if index ==-1: # it is the smallest,case 1
                activeLists.insert(0,[item])
            elif index == len(array)-1: # it is the largest, case 2
                temp =[]
                for num in activeLists[-1]:
                    temp.append(num)
                temp.append(item)
                activeLists.append(temp)
            else: # case 3, we can actually merge with the above, but for the sake of clarity
                temp = []
                for num in activeLists[index]:
                    temp.append(num)
                temp.append(item)
                # we need to remove all the have same length as this temp
                length = len(temp)
                new = []
                for activeList in activeLists:
                    if len(activeList)==length:
                        continue
                    else:
                        new.append(activeList)
                # insert temp at the correct index
                new.insert(index+1,temp)
                activeLists = new    
    return max([sum(activeList) for activeList in activeLists])
#array = [10,22,9,33,21,50,41,41,60,60,80]
#print (maxSumIncreasingSubsequence(array))      
# find the leaders in an array, leader is greater or equal to all the element ot its right side
def leaderInArray(array):
    output= [array[-1]]
    for item in array[::-1][1:]:
        if item>=output[-1]:
            output.append(item)
    return output[::-1]
#array = [16 ,17 ,4 ,3, 5, 2]
#print (leaderInArray(array))

# given 2 interval, if they overlap, return 1 union, else, return 2 intervals
def overlap(interval1,interval2):
    if interval1[1]>=interval2[0]:
        return [interval1[0],max(interval2[1],interval1[1])],True
    else:
        return interval2,False
        
# minimal of platforms so that trains leaves safely, array of tuple of deapture and arrival time 
# example: array = [(900,910),(940,1200), (950,1120)  ,(1100,1130) ,(1500,1900) ,(1800,2000)]
def minimumPlatforms(array):
    output = 1
    currentInterval = array[0]
    local =1
    for interval in array[1:]:
        currentInterval,isOverlapped = overlap(currentInterval,interval)
        if isOverlapped:
            local+=1
        else:
            output = max(output,local)
            local = 1
    return output
#array = [(900,910),(940,1200), (950,1120)  ,(1100,1130) ,(1500,1900) ,(1800,2000)]
#print (minimumPlatforms(array))

# maximum of all subarrays of size k
def maximumOfAllSubArrayK(array,k):
    output = [max(array[:k])]
    for item in array[k:]:
        currentMax = output[-1]
        output.append(max(currentMax,item))
    return output
#array=[1 ,2, 3, 1, 4, 5, 2, 3, 6]
#print (maximumOfAllSubArrayK(array,3))
    
# trapping rain water 
#Given an array A of N non-negative integers representing height of blocks at 
#index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
# slow version, for each index, find max left, max right, and the amount of water holding is minimum of those 2 minus the height
def trapRainWaterSlow(array):
    total = 0
    for index,item in enumerate(array):
        maxRight = max(array[index+1:])
        maxLeft  = max(array[:index-1])
        total = min(maxRight+maxLeft)-item
    return total

# fast version
def trapRainWaterFast(array):
    total = 0
    left = 0
    right = len(array)-1
    leftWall,rightWall = 0
    while left<right:
        if array[left]<array[right]:
            if array[left]>leftWall:
                leftWall = array[left]
            else:
                total+=leftWall-array[left]
            left+=1
        else:
            if array[right]>rightWall:
                rightWall = array[right]
            else:
                total+=rightWall-array[right]
            right-=1
    return total
    
#849. Maximize Distance to Closest Person
#In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 
#
#There is at least one empty seat, and at least one person sitting.
#
#Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
#
#Return that maximum distance to closest person.
def maxDistToClosest(seats):
    check = False
    currentLength = 0
    start = 0
    stop = 0
    localLength = 0
    position = None
    for index,item in enumerate(seats):
        if item:
            if check: # this means end of our vacancy
                stop = index-1
                if start ==0: # means that we are from the left
                    localLength= stop-start
                    if (localLength>currentLength):
                        position= 0
                        currentLength = localLength
                else:
                    localLength = (stop-start)//2
                    if (localLength>currentLength):
                        position= (stop+start)//2
                        currentLength = localLength
                check = False
        else:
            if not check:
                check = True
                start = index
    if check:
        stop = index
        localLength = (stop-start)
        if localLength>currentLength:
            position = index
            currentLength = localLength
    return currentLength+1
    
#    605. Can Place Flowers
#Suppose you have a long flowerbed in which some of the plots are planted and some 
#are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
#
#Given a flowerbed (represented as an array containing 0 and 1, where 0 means 
#empty and 1 means not empty), and a number n, return if n new flowers can be planted 
#in it without violating the no-adjacent-flowers rule.    
def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    if len(flowerbed)==1 and flowerbed[0]==0 and n<=1:
        return True
    check = False
    start = 0
    stop = 0
    localLength = 0
    position = None
    for index,item in enumerate(flowerbed):
        if item:
            if check: # this means end of our vacancy
                stop = index-1
                if start ==0: # means that we are from the left
                    localLength= stop-start+1                        
                else:
                    localLength = (stop-start)
                n-= (localLength)//2
                check = False
        else:
            if not check:
                check = True
                start = index
        if n<=0:
            return True
    if check:
        stop = index
        if start:
            localLength = (stop-start)+1
        else:
            localLength = (stop-start)+2
        n-= (localLength)//2
    return n<=0
    
#    581. Shortest Unsorted Continuous Subarray
#Given an integer array, you need to find one continuous subarray that if you only 
#sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
#You need to find the shortest such subarray and output its length.
# using sort is easy, consider not using sort
    
#It turns out that the two boundary indices i and j can be found in linear time, 
#if we take advantage of the following three properties:
#
#nums[0, i - 1] and nums[j + 1, n - 1] are both sorted.
#
#nums[i] != nums_sorted[i] and nums[j] != nums_sorted[j].
#
#nums[i - 1] <= min and max <= nums[j + 1], where min and max are the minimum and maximum values of subarray nums[i, j].
#
#The first and third properties guarantee that the subarray nums[0, i - 1] will 
#be exactly the same as subarray nums_sorted[0, i - 1], and the subarray nums[j + 1, n - 1] 
#exactly the same as nums_sorted[j + 1, n - 1], while the second property ensures that i will 
#be the first index at which the two elements of nums and nums_sorted are different and j be the last such index.
#
#Since we aim at the shortest subarrays, from the first property alone, we need to 
#find the two longest sorted subarrays starting at index 0 and ending at index n - 1, respectively. 
#Assume the two subarrays are nums[0, l] and nums[r, n - 1]. 
#If there is overlapping between these two subarrays, i.e.l >= r, 
#then the whole array is sorted so 0 will be returned. Otherwise, the input array is not sorted. 
#However, we cannot say sorting nums[l, r] will leave the whole array sorted, 
#because at this moment the third property may not be satisfied.
#
#To guarantee the third property, assume min and max are the minimum and maximum 
#values of subarray nums[l, r], then we need to decrease l as long as nums[l] > min, 
#and increase r as long as nums[r] < max. After this is done, it can be shown that the second property will be 
#met automatically, and nums[l + 1, r - 1] will be the shortest subarray we are looking for (that is, i = l + 1 and j = r - 1).
#
#Finding the longest subarrays and the maximum and minimum values of the middle 
#subarray takes one-pass. Ensuring the third property requires a second pass. 
#Therefore we have this two-pass solution:
def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # define left, and right for the sorted left, and right
    l, r = 0,len(nums)-1
    while l<r and nums[l]<=nums[l+1]:
        l+=1
    if l>=r: 
        return 0 # the array is sorted
    while r>l and nums[r]>=nums[r-1]:
        r-=1
    # find the min, max of the middle part from l to r
    midMin,midMax= float("inf"),-float("inf")
    for i in range(l,r+1):
        midMin = min(midMin,nums[i])
        midMax=  max(midMax,nums[i])
    while l>=0 and nums[l]>midMin:
        l-=1
    while nums[r]<midMax and r<len(nums):
        r+=1
    return r-l-1
    
# given an array, find array triplets (or number of possible triangle endge)
def arrayTriangleSlow(arr):
    if len(arr)<3:
        return 0
    arr= sorted(arr)
    output = set()
    print (arr)
    for first in range(len(arr)-2):
        second = first+1
        third  = first+2
        while second<third and third<=len(arr)-1:
            if arr[first]+arr[second]>arr[third]:
                output.add((first,second,third))
                third+=1
            else:
                second+=1 
                third  = second+1
            if second >=len(arr)-2:
                break
            if third>len(arr)-1:
                second+=1
                third = second+1
    return output
# fast
def arrayTriangleFast(arr):
    if len(arr)<3:
        return 0
    arr= sorted(arr)
    output = set()
    print (arr)
    for first in range(len(arr)-2):
        second = first+1
        third  = first+2
        while second<third and third<=len(arr)-1:
            if arr[first]+arr[second]>arr[third]:
                output.add((first,second,third))
                third+=1
            else:
                second+=1 
                third  = second+1
            if second >=len(arr)-2:
                break
            if third>len(arr)-1:
                second+=1
                third = second+1
    return output
## Google Code Jam 2019 round 1B   
    
#Along one wall of the fencing arena, there is a rack with N different types of swords; 
#the swords are numbered by type, from 1 to N. As the head judge, you will pick a pair of integers (L, R)
# (with 1 ≤ L ≤ R ≤ N), and only the L-th through R-th types of swords (inclusive) will be available for the fight.
#
#Different types of sword are used in different ways, and being good with one type of sword does not 
#necessarily mean you are good with another! Charles and Delila have skill levels of Ci and Di, respectively,
# with the i-th type of sword. Each of them will look at the types of sword you have made available for this fight, 
# and then each will choose a type with which they are most skilled. If there are multiple available types with which a
# fighter is equally skilled, and that skill level exceeds the fighter's skill level in all other available types,
# then the fighter will make one of those equally good choices at random. Notice that it is possible for Charles and 
# Delila to choose the same type of sword, which is fine — there are multiple copies of each type of sword available.

#The fight is fair if the absolute difference between Charles's skill level with his chosen sword type and Delila's 
#skill level with her chosen sword type is at most K. To keep the fight exciting, you'd like to know how many different
# pairs (L, R) you can choose that will result in a fair fight.
    
def findPPairLR(charles,delilah,K,N):
    result = 0
    return result
#763. Partition Labels
# A string S of lowercase letters is given. We want to partition this string into 
#    as many parts as possible so that each letter appears in at most one part, 
#    and return a list of integers representing the size of these parts.
def partitionLabel(label):
    d= {}
    result = []
    for index in range(len(label)):
        letter= label[index]
#        print (index,letter)
        if letter not in d:
            result.append(1)
            d[letter] = len(result)
        else:
            currentIndex= d[letter]
#            print (580,letter,index,currentIndex)
            if currentIndex!= len(result):
                for i in range(len(result)-1,currentIndex-1,-1):
                    currentS = result.pop()
                    for key in d:
                        if d[key]==i+1:
                            d[key] = currentIndex
                    result[currentIndex-1]+=currentS
            d[letter]= len(result)
            result[-1]+=1     
    return result
    
#986. Interval List Intersections
#
#Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
#Return the intersection of these two interval lists.
#
#(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x 
#with a <= x <= b.  The intersection of two closed intervals is a set of real numbers 
#that is either empty, or can be represented as a closed interval.  For example, the intersection of 
#[1, 3] and [2, 4] is [2, 3].)
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
def intervalIntersection(A,B):
    i = 0
    j = 0
    result = []
    while i<len(A) and j<len(B):
        intervalA = A[i]
        intervalB = B[j]
        # check if those 2 interval intersect
        if (intervalA[0]>=intervalB[0] and intervalA[0]<=intervalB[1]): # means that B[0], A[0],min(B[1],A[1]),max(B[1],A[1])
            # intersection is equal to A[0],min(B[1],A[1])
            intersection = [intervalA[0],min(intervalB[1],intervalA[1])]
            # if A[1] greater than B[1], we keep i, increase j
            if intervalA[1]>intervalB[1]:
                j+=1
            elif intervalA[1]<intervalB[1]:
                i+=1
            # if equal, increase both
            else:
                i+=1
                j+=1
            result.append(intersection)
        elif (intervalB[0]>=intervalA[0] and intervalB[0]<=intervalA[1]): # means that A[0], B[0],min(B[1],A[1]),max(B[1],A[1])
            intersection = [intervalB[0],min(intervalB[1],intervalA[1])]
            if intervalA[1]>intervalB[1]:
                j+=1
            elif intervalA[1]<intervalB[1]:
                i+=1
            # if equal, increase both
            else:
                i+=1
                j+=1
            result.append(intersection)
        else: # no intersection, we keep the one with higher interval
            if intervalA[0]>intervalB[1]:
                j+=1
            elif intervalB[0]>intervalA[1]:
                i+=1
    return result

#931. Minimum Falling Path Sum
#
#Given a square array of integers A, we want the minimum sum of a falling path through A.
#
#A falling path starts at any element in the first row, and chooses one element from each row.  
#The next row's choice must be in a column that is different from the previous row's column by at most one.
    
def minFallingPathSum(A):
    r = len(A)
    c = len(A[0])
    for i in range(1,r):
        for j in range(c):
            if j==0:
                A[i][j] = A[i][j]+min(A[i-1][j],A[i-1][j+1])
            elif j==c-1:
                A[i][j] = A[i][j]+min(A[i-1][j-1],A[i-1][j])
            else:
                A[i][j] = A[i][j]+min(A[i-1][j],A[i-1][j+1],A[i-1][j-1])
    return min(A[r-1])

#1023. Camelcase Matching
#A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. 
#(We may insert each character at any position, and may insert 0 characters.)
#
#Given a list of queries, and a pattern, return an answer list of booleans, where 
#answer[i] is true if and only if queries[i] matches the pattern.
    
def camelMatch(queries,pattern):
    res = []
    for query in queries:
        pointerQ = 0
        firstCheck = True
        for i in range(len(pattern)):
            patternLetter = pattern[i]
            queryLetter   = query[pointerQ]
            check         = True
            while patternLetter!=queryLetter:
                if patternLetter.isupper():
                    if queryLetter.islower():
                        pointerQ+=1
                        if pointerQ== len(query):
                            check = False
                            break
                        else:
                            queryLetter = query[pointerQ]
                    else:
                        check = False
                        break
                else: # pattern is low case
                    if queryLetter.islower():
                        pointerQ+=1
                        if pointerQ== len(query):
                            check = False
                            break
                        else:
                            queryLetter = query[pointerQ]
                    else:
                        check = False
                        break
            if not check:
                firstCheck= False
                break
            else:
                pointerQ+=1
                if pointerQ== len(query):
                    if i == len(pattern)-1:
                        break
                    else:
                        firstCheck = False
                        break
                else:
                    queryLetter = query[pointerQ]
        if firstCheck:
            flag= True
            for letter in query[pointerQ:]:
                if letter.isupper():
                    flag= False
                    break
            if flag:
                res.append(True)
            else:
                res.append(False)
        else:
            res.append(False)
    return res

#712. Minimum ASCII Delete Sum for Two Strings
#
#Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
def minimumDeleteSum(s1,s2):
    dp =[]
    for i in range(len(s1)+1):
        temp =[]
        for j in range(len(s2)+1):
            temp.append(None)
        dp.append(temp)
    dp[0][0]=0
    for i in range(1,len(s1)+1):
        dp[i][0]= dp[i-1][0]+ord(s1[i-1])
    for j in range(1,len(s2)+1):
        dp[0][j] = dp[0][j-1]+ord(s2[j-1])
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]),dp[i][j-1]+ord(s2[j-1]))
    return dp[-1][-1]

#932. Beautiful Array
#For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
#
#For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
#
#Given N, return any beautiful array A.  (It is guaranteed that one exists.)

def beautifulArray(N):
    return None
#
#Write a function that reverses a string. The input string is given as an array of characters char[].
#
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
#You may assume all the characters consist of printable ascii characters.
def reverseString(s):
    def reverse(s,i,j):
        if i<j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            reverse(s,i+1,j-1)
    reverse(s,0,len(s)-1)
        
# pascal triangle
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1],[1,1]]
    for i in range(2,numRows):
        temp=[1]
        for j in range(i-1):
            temp.append(res[-1][j]+res[-1][j+1])
        temp.append(1)
        res.append(temp)
    return res[:numRows]