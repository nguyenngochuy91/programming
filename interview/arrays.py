# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:43:28 2019

@author: Huy Nguyen
"""
import heapq
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

# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0
# with 01, and each occurrence of 1 with 10.
#
#Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).
def kthGrammar(n, k):
    """
    :type N: int
    :type K: int
    :rtype: int
    """
    k-=1
    flip = 0
    while n>1:
        if k%2:
            flip+=1
        k=k//2
        n-=1
    if k%2:
        flip+=1
    if flip%2:
        return 1
    return 0
# merge sort iterative
def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1
    
    # append what is remained in either of the lists
    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])
    
    return ret
def mergeSortIterative(nums):
    array = [[num] for num in nums]
    while len(array)>1:
        temp = []
        for i in range(0,len(array),2):
            if i+1<len(array):
                ret = merge(array[i],array[i+1])
            else:
                ret = array[i]
            temp.append(ret)
        array = temp
    return array[0]


#Search a 2D Matrix II
#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#Integers in each row are sorted in ascending from left to right.
#Integers in each column are sorted in ascending from top to bottom.
# O(m+n)
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    row = len(matrix)
    col = len(matrix[0])
    i = 0
    j = col-1
    while  i<row and j>=0:
        val = matrix[i][j]
        if target== val:
            return True
        elif target>val: # this means increase the number of row:
            i+=1
        else:
            j-=1
    return False
    
#1091. Shortest Path in Binary Matrix
#In an N by N square grid, each cell is either empty (0) or blocked (1).
#
#A clear path from top-left to bottom-right has length k if and only if it is composed of cells 
#C_1, C_2, ..., C_k such that:
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
#Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1
def shortestPathBinaryMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    k=0
    n = len(grid)-1
    if grid[0][0]==1 or grid[n][n]==1:
        return -1
    visited = set([(0,0)])
    current = set([(0,0)])
    while current:
        nextL = set()
        k+=1
        for node in current:
            x,y = node
            visited.add(node)
            if (x,y)==(n,n):
                return k
            temp = [(x-1,y-1),(x-1,y),(x-1,y+1),
                   (x,y-1),(x,y+1),
                   (x+1,y-1),(x+1,y),(x+1,y+1)]
            for t in temp:
                if t[0]>=0 and t[1]>=0 and t[0]<=n and t[1]<=n and t not in visited and grid[t[0]][t[1]]==0:
                    nextL.add(t)
        current = nextL
    return -1
    
#1090. Largest Values From Labels
#We have a set of items: the i-th item has value values[i] and label labels[i].
#
#Then, we choose a subset S of these items, such that:
#
#|S| <= num_wanted
#For every label L, the number of items in S with label L is <= use_limit.
#Return the largest possible sum of the subset S.
def largestValsFromLabels(values, labels, num_wanted, use_limit):
    """
    :type values: List[int]
    :type labels: List[int]
    :type num_wanted: int
    :type use_limit: int
    :rtype: int
    """
    d = {}
    res = 0
    labelUse = {}
    for i in range(len(values)):
        label = labels[i]
        value = values[i]
        if value not in d:
            d[value] = {label:1}
        else:
            if label not in d[value]:
                d[value][label]=0
            d[value][label]+=1
    myList = sorted(d)


    while num_wanted:
        if myList:
            value = myList.pop(-1)
            # get the labels that have this value
            labels = d[value]
            for label in labels:
                labelCount = labels[label] # will have to check whether this label count cant be used and used how many times
                # get the number of this label already used
                if label not in labelUse:
                    labelUse[label]=0
                used = labelUse[label] 
                if used==use_limit:
                    pass # passed if already used to limit
                # else, add to the minimum of (use_limit-used,num_wanted)
                for i in range(min(use_limit-used,num_wanted,labelCount)):
                    res+=value
                    num_wanted-=1
                    labelUse[label]+=1

        else:
            break

    return res    

# qsort
def quicksort(lst):
    n = len(lst)
    qsort(lst,0,n-1)
def qsort(lst,low,high):
    if low<high:
        p = partition(lst, low, high)
        qsort(lst,0,p-1)
        qsort(lst,p+1,high)
def partition(lst, lo, hi):
    pivot = lst[hi]
    i = lo
    for j in range(lo,hi):
        if lst[j]<pivot:
            lst[i],lst[j]= lst[j],lst[i]
            i+=1
    lst[i], lst[hi] = lst[hi], lst[i]
    return i
    
#You are given two strings s and t of the same length, consisting of uppercase English letters. 
#Your task is to find the minimum number of "replacement operations" needed to get some anagram of the 
#string t from the string s. A replacement operation is performed by picking exactly one character from the string s and replacing it by some other character.
def createAnagram(s, t):
    ds = {}
    dt = {}
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in l:
        ds[letter]=0
        dt[letter]=0
    for item in s:
        ds[item]+=1
    for item in t:
        dt[item]+=1        
    swap = 0 # swapping
    leftOver = 0
    for letter in l:
        vs = ds[letter]
        vt = dt[letter]
        if vs==vt:
            continue
        elif vs<vt:
            extra = vs-vt
            if leftOver>=0:
                swap+=min(leftOver,-extra)
            leftOver+=extra
        else:
            extra= vs-vt 
            if leftOver<=0: 
                swap +=min(-leftOver,extra)
            leftOver+=extra 
    return swap

#Given a string consisting of lowercase English letters, find the largest square number which 
#can be obtained by reordering the string's characters and replacing them with any digits you need 
#(leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.
#
#If there is no solution, return -1.
def constructSquare(s):
    v = len(s)
    ds = {}
    dv = {}
    for l in s:
        if l not in ds:
            ds[l]=0
        ds[l]+=1
    for key in ds:
        val = ds[key]
        if val not in dv:
            dv[val]=[]
        dv[val].append(key)
    if len(ds)>10:
        return -1
    if v ==1:
        return 9
    start = int((10**(v-1))**.5)
    stop  = int((10**v)**.5)

    for i in range(stop,start,-1):
        i = i**2

        # check if there is a valid mapping
        num = str(i)
        ds = {}
        dn= {}
        check = True
        for l in num:
            if l not in ds:
                ds[l]=0
            ds[l]+=1
        for key in ds:
            v = ds[key]
            if v not in dn:
                dn[v]=[]
            dn[v].append(key)  
        if len(dn)!=len(dv):
            continue
        for key in dn:
            if key not in dv:
                check = False
                break
            else:
                if len(dv[key])!=len(dn[key]):
                    check = False 
                    break 
        if check:
            return i
            
    return -1

## #1129 Shortest Path with Alternating Colors
#Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, 
#each edge is either red or blue, and there could be self-edges or parallel edges.
#
#Each [i, j] in red_edges denotes a red directed edge from node i to node j.  
#Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.
#
#Return an array answer of length n, where each answer[X] is the length of the 
#shortest path from node 0 to node X such that the edge colors alternate along 
#the path (or -1 if such a path doesn't exist).
def shortestAlternatingPaths(n, red_edges, blue_edges):
    graph = {}
    answer = {}
    for i in range(n):
        answer[i]={}
        answer[i][0]=float("inf")
        answer[i][1] = float("inf")
    for edge in red_edges:
        start,stop = edge
        if start in graph:
            if 1 not in graph[start]:
                graph[start][1] = []

        else:
            graph[start]={}
            if 1 not in graph[start]:
                graph[start][1] = []    
        graph[start][1].append(stop)     
    for edge in blue_edges:
        start,stop = edge
        if start in graph:
            if 0 not in graph[start]:
                graph[start][0] = []

        else:
            graph[start]={}
            if 0 not in graph[start]:
                graph[start][0] = []    
        graph[start][0].append(stop)  
    answer[0]={0: 0, 1: 0}
    pq = []
    if 0 in graph:
        if 1 in graph[0]:
            for neighbor in graph[0][1]:
                heapq.heappush(pq,(1,neighbor,1))
        if 0 in graph[0]:
            for neighbor in graph[0][0]:
                heapq.heappush(pq,(1,neighbor,0))
#    print (graph,pq)
    while pq:
#        print (33,pq)
#        print (34,answer)
        distance,currentNode,currentColor  = heapq.heappop(pq)
        if distance <answer[currentNode][currentColor]:
            answer[currentNode][currentColor] = distance
        if currentNode not in graph:
            continue
        else:
            if (1-currentColor) not in graph[currentNode]:
                continue
            else:
                for neighbor in graph[currentNode][1-currentColor]:
                    neighborDistance = 1 + answer[currentNode][currentColor]
                    #print (neighbor,answer)
                    # check if the distance to this neighbor through currentNode is less than current Distance
                    if answer[neighbor][1-currentColor]>neighborDistance: # update and insert to our hp
                        answer[neighbor][1-currentColor] = neighborDistance
                        heapq.heappush(pq,(neighborDistance,neighbor,1-currentColor))
#        print (50,pq)
#        print (51,answer)
    output = [0]
#    print (pq,answer)
    for i in range(1,n):
        val= min(answer[i][0],answer[i][1])
        if val==float("inf"):
            output.append(-1)
        else:
            output.append(val)
    return output

# countIsland
#You are given a binary matrix as an input. 
#You want to return the number of islands in the binary matrix.  
#You can think of the 0's as the ocean and the 1's as land.  
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
#
# 
#
#Examples:
#
# 
#
## There are 6 islands in this matrix
#{1, 1, 0, 0, 0},
#{0, 1, 0, 0, 1},
#{1, 0, 0, 1, 1},
#{0, 0, 0, 0, 0},
#{1, 0, 1, 0, 1}
#
# 
#
## There is 1 island in this matrix
#{1, 1, 1, 1, 1},
#{1, 1, 1, 1, 1},
#{1, 1, 1, 1, 1}
# allow modifing mattrix, runtime O(nm), space O(1)
def countIslands(mat):
    numIsland = 0
    row       = len(mat)
    col       = len(mat[0])
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                queue = [(i,j)]
                
                mat[i][j] =0
                numIsland+=1
                while queue:
                    currentNode            = queue.pop()
                    currentRow,currentCol  = currentNode 
                    potentialNeighbor = [(currentRow+1,currentCol),(currentRow,currentCol+1),(currentRow-1,currentCol),(currentRow,currentCol-1)]
                    for potential in potentialNeighbor:
                        x,y = potential
                        if x>=0 and x<row and y>=0 and y<col:
                            if  mat[x][y]==1:
                                mat[x][y]=0
                                queue.append((x,y))
    return numIsland   
# not allowing modifying matrix, runtime O(nm),space O(nm)
def countIsLandHashMap(mat):
    numIsland = 0
    row       = len(mat)
    col       = len(mat[0])
    visited   = set()
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1 and (i,j) not in visited:
                queue = [(i,j)]
                visited.add((i,j))
                mat[i][j] =0
                numIsland+=1
                while queue:
                    currentNode            = queue.pop()
                    currentRow,currentCol  = currentNode 
                    potentialNeighbor = [(currentRow+1,currentCol),(currentRow,currentCol+1),(currentRow-1,currentCol),(currentRow,currentCol-1)]
                    for potential in potentialNeighbor:
                        x,y = potential
                        if x>=0 and x<row and y>=0 and y<col:
                            if  mat[x][y]==1 and (x,y) not in visited:
                                mat[x][y]=0
                                queue.append((x,y))
    return numIsland   
# not allowing modifying matrix, runtime O(n^2m),space O(n)
def countIsLandVariant(mat):
    row             = len(mat)
    col             = len(mat[0])
    lastRow         = []
    numIsland       = 0
    for i in range(row):
        currentRow = []
        count      = 0
        for j in range(col):
            if mat[i][j] ==1:
                if count ==0:
                    start = j
                count+=1
            else:
                if count>0:
                    stop = j-1
                    currentRow.append((start,stop))
                    count = 0
        if count>0:
            currentRow.append((start,col-1))
#        print (mat[i])
        intersectedIsland = findIntersect(lastRow,currentRow)
        numIsland +=intersectedIsland
        lastRow = currentRow
#        print ("numIsland",numIsland)
    return numIsland       
# helper function, given lastRow, and currentRow,determin how many island should we add
# time O(n)
def findIntersect(lastRow,currentRow):
#    print ("lastRow",lastRow)
#    print ("currentRow",currentRow)
    if not lastRow:
        return len(currentRow)
    if not currentRow:
        return 0
    output = []
    i,j = 0,0
    # set currentInterval as empty
    currentInterval = []
    countNewInterval = 0
    output = []
    while i<len(lastRow) and j <len(currentRow):
        lastRowInterval = lastRow[i]
        currentRowInterval = currentRow[j]
#        print ("lastRowInterval:",lastRowInterval)
#        print ("currentRowInterval",currentRowInterval)
#        print ("currentInterval",currentInterval)
#        print ("output",output)
        # check if they intersec
        if lastRowInterval[0]>currentRowInterval[1] or lastRowInterval[1]<currentRowInterval[0]:
            # this means those 2 dont intersect, we only need to check if our currentInterval intersect any of them
            # and we know that our currentInterval can only intersect at most 1 of those 2 intervals
            if currentInterval: # if our currentInterval is not empty, basically only if the previous are merged
                if currentInterval[0]>lastRowInterval[1] or currentInterval[1]<lastRowInterval[0]: # means current and lastRow not itnersect
                    if currentInterval[0]>currentRowInterval[1] or currentInterval[1]<currentRowInterval[0]:
                        # it means we can count of currentInterval as a non intersecting to the rest
                        output.append(currentInterval)
                        # we also append the interval that is smaller of the lastRowInterval and currentRowInterval
                        if lastRowInterval[0]<currentRowInterval[0]:
                            output.append(lastRowInterval)
                            # set our currentInterval equal to currentRowInterval
                            currentInterval = []
                            i+=1
                        else:
                            output.append(currentRowInterval)
                            currentInterval = []
                            j+=1
                        countNewInterval+=2
                    else:
                        # we merge currentInterval with currentRowInterval
                        currentInterval = (min(currentInterval[0],currentRowInterval[0]),max(currentInterval[1],currentRowInterval[1]))
                        countNewInterval+=1
                        output.append(currentInterval)
                        currentInterval = []
                        j+=1
                else:
                    # we merge currentInterval with lastRowInterval
                    currentInterval = (min(currentInterval[0],lastRowInterval[0]),max(currentInterval[1],lastRowInterval[1]))
                    countNewInterval+=1
                    output.append(currentInterval)
                    currentInterval = []
                    i+=1
            # if our currentInterval is empty
            else:
                if lastRowInterval[0]<currentRowInterval[0]:
                    output.append(lastRowInterval)
                    # set our currentInterval equal to currentRowInterval
                    currentInterval = []
                    i+=1
                    countNewInterval+=1
                else:
                    output.append(currentRowInterval)
                    currentInterval = []   
                    j+=1
                    countNewInterval+=1
        else: # they intersect, create a merge interval
            mergeInterval = (min(currentRowInterval[0],lastRowInterval[0]),max(currentRowInterval[1],lastRowInterval[1]))
            
            # check if this merge intersect with out currentInterval
            if not currentInterval:
                currentInterval = mergeInterval
            else:
                if currentInterval[0]>mergeInterval[1] or currentInterval[1]<mergeInterval[0]:
                    # they dont intersect
                    countNewInterval+=1
                    output.append(currentInterval)
                    currentInterval = mergeInterval
                    
                else:
                    # merge all of them
                    currentInterval = (min(currentInterval[0],mergeInterval[0]),max(currentInterval[1],mergeInterval[1]))
            i+=1
            j+=1
        print ()
#        print ("currentInterval after loop",currentInterval)
    # if we iterate through one of our list but not both
    if i <len(lastRow):
        if not currentInterval:
            output.extend(lastRow[i:])
            countNewInterval+=len(lastRow)-i
        else:
            for interval in lastRow[i:]:
                
                if interval[1]<currentInterval[0]:
                    output.append(interval)
                    countNewInterval+=1
                elif interval[0]>currentInterval[1]:
                    output.append(currentInterval)
                    countNewInterval+=1
                    currentInterval = interval
                else: # they intersect
                    currentInterval = (min(currentInterval[0],interval[0]),max(currentInterval[1],interval[1]))
            output.append(currentInterval)
            countNewInterval+=1
    elif j <len(currentRow):
        if not currentInterval:
            output.extend(currentRow[j:])
            countNewInterval+=len(currentRow)-j
        else:
            for interval in currentRow[j:]:
                if interval[1]<currentInterval[0]:
                    output.append(interval)
                    countNewInterval+=1
                elif interval[0]>currentInterval[1]:
                    output.append(currentInterval)
                    countNewInterval+=1
                    currentInterval = interval
                else: # they intersect
                    currentInterval =  (min(currentInterval[0],interval[0]),max(currentInterval[1],interval[1]))
            output.append(currentInterval)
            countNewInterval+=1
    else:
        if currentInterval:
            output.append(currentInterval)
            countNewInterval+=1
#    print ("final result:",output)
    return countNewInterval    - len(lastRow)      
                
#def test():
#    inp = [[1, 1, 0, 0, 0],              
#           [0, 1, 1, 1, 1],
#           [1, 0, 0, 1, 1],
#           [0, 0, 0, 0, 0],
#           [1, 0, 1, 0, 1]]
#    print ("Should have 5")
#    print ("Actually have "+str(countIsLandVariant(inp)))
##    lastRow= [(1, 1), (4, 4)]
##    currentRow= [(0, 0), (3, 4)]
##
##    print(findIntersect(lastRow,currentRow))
#test()
                
#221. Maximal Square
#Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    arr = []
    output = 0
    for i in range(row-1,-1,-1):
        for j in range(col-1,-1,-1):
            if i == row-1:

            if matrix[i][j]=="1":
                val= min(arr[i][j+1],arr[i+1][j],arr[i+1][j+1])+1
                arr[i][j]=val
                output   = max(val,output)
    return output**2
