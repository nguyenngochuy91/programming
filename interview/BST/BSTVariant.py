# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:37:52 2019

@author: huyn
"""
import math
# second version of binarySearch that has l<r, and r = mid, l = mid , 
# this helps our l and r never goes out of bound, and they dont flip
def binarySearch(arr,num):
    start,stop = 0,len(arr)-1
    while start +1< stop:
        mid = (start+stop)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            stop = mid
        else:
            start = mid
    if arr[start]== num: 
        return start
    if arr[stop] == num: 
        return stop
    return -1
# given an array and target number, find the range of index that is equal to the target, 
# if target not in arrays, return [-1,-1]
def searchRange(nums, target):
    # Write your code here
    def searchLeft(nums,target):
        start,stop = 0 , len(nums)-1
        while start+1<stop:
            mid = (start+stop)//2
            if nums[mid]>=target: 
                stop = mid 
            else:
                start = mid
        if nums[start]==target:
            return start
        if nums[stop]== target:
            return stop 
        return -1 
    left = searchLeft(nums,target)
    if left ==-1:
        return [-1,-1]
    def searchRight(nums,target):
        start,stop = 0 , len(nums)-1
        while start+1<stop:
            mid = (start+stop)//2
            if nums[mid]<=target: 
                start = mid 
            else:
                stop = mid
        if nums[stop]==target:
            return stop
        if nums[start]== target:
            return start 
    right = searchRight(nums,target)
    return [left,right] 
# find peak in an array, could have multiple mid
def getPeak(nums):
    # Write your code here
    start ,stop =0,len(nums)-1 
    while start+1<stop:
        mid = (start+stop)//2
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid
        elif nums[mid]<nums[mid-1]:
            stop = mid
        elif nums[mid]<nums[mid+1]: 
            start = mid
    if nums[start]>=nums[stop]:
        return start
    return stop

# def find minimum element in rotated sorted array
def getMin(nums):
    # Write your code here
    start,stop = 0,len(nums)-1 
    while start+1<stop: 
        mid = (start+stop)//2
        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return nums[mid+1]
        elif nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]:
            return nums[mid]
        elif nums[mid]<nums[mid+1] and nums[mid]>nums[mid-1]: # mid-1,mid,mid+1 increase 
            if nums[mid]<nums[len(nums)-1]: # means that our min is to the left 
                stop = mid
            else: # min is to the right 
                start = mid
    if start ==stop: 
        return nums[start]
    return min(nums[start],nums[stop])
#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
######### great one
def climbingLeaderboard(scores, alice):
    d= {}
    value = set()
    i = 1
    for s in scores:
        if s not in value:
            d[i]=s
            value.add(s)
            i+=1
    res = []
    for score in alice:
        start,stop = 1,len(d)
        check = False
        while start+1<stop:
            mid = (start+stop)//2
          
            if d[mid]==score:
                res.append(mid)
                check = True
                break
            if d[mid]<score:
                stop = mid
            else:
                start = mid
        if not check:
            if d[stop]>score:
                res.append(stop+1)
            else:
                if d[start]>score:
                    res.append(stop)
                else:
                    res.append(start)
    return res

#875. Koko Eating Bananas
#Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  
#The guards have gone and will come back in H hours.
#
#Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, 
#and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, 
#and won't eat any more bananas during this hour.
#
#Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
#
#Return the minimum integer K such that she can eat all the bananas within H hours.
def minEatingSpeed(piles, H):
    def check(piles,K,H):
        hour = 0
        for p in piles:
            hour+=p//K
            if p%K:
                hour+=1
        return hour<=H
    start,stop = 0, max(piles)
    while start+1<stop:
        mid = (start+stop)//2
        if check(piles,mid,H):
            stop = mid
        else:
            start = mid
    if check(piles,stop,H):
        return stop
    return start
    
#1146. Snapshot Array
class SnapshotArray:
######### great one
    def __init__(self, length: int):
        self.arr = {index:[[0,0]] for index in range(length)}
        self.snapNum = -1
    def set(self, index: int, val: int) -> None:
        nextSnap = self.snapNum+1
        # check if this is overide the currentSNap
        if self.arr[index][-1][0]==nextSnap:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([nextSnap,val])

    def snap(self) -> int:
        self.snapNum+=1
        return self.snapNum

    def get(self, index: int, snap_id: int) -> int:
        arr =self.arr[index]
        # do a binary Search
        start = 0
        stop = len(arr)-1
        while start+1<stop:
            mid = (start+stop)//2
            item = arr[mid]
            currentSnap,value = item
            if currentSnap==snap_id:
                return value
            elif currentSnap>snap_id:
                stop = mid
            else:
                start = mid
        if arr[stop][0]<=snap_id:
            return arr[stop][1]
        elif arr[start][0]<=snap_id:
            return arr[start][1]
            
#https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
######### great one
def repeatedString(s, n):
    d= {}
    current = None
    for i in range(len(s)):
        if s[i]=="a":
            if not d:
                d[i]=1
                current = i
            else:
                d[i]=d[current]+1
                current = i
    bigCount = n//len(s)*(len(d))
#    print ("bigCount",bigCount)
    extraLength = n%len(s)
#    print ("extraLength",extraLength)
    if extraLength and d:
        array = list(d.keys())
        start = 0
        stop = len(array)-1
        while start+1<stop:
            mid = (start+stop)//2
            if array[mid] == extraLength-1:
                return bigCount+d[array[mid]]
            elif array[mid]<extraLength-1:
                start=mid
            else:
                stop = mid
#        print (array,start,stop)
        if array[stop]<=extraLength-1:
            return bigCount+d[array[stop]]
        elif array[start]<=extraLength-1:
            return bigCount+d[array[start]]
    return bigCount
    
#1201. Ugly Number III
#Write a program to find the n-th ugly number.
#
#Ugly numbers are positive integers which are divisible by a or b or c.
def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
    start = min([a,b,c])
    stop  = max([a,b,c])*n
    lcmABC = lcm([a,b,c])
    lcmAB  = lcm([a,b])
    lcmBC  = lcm([c,b])
    lcmAC  = lcm([a,c])    
    while start+1<stop:
        mid   = (start+stop)//2
        index = getIndex(mid,lcmAB,lcmBC,lcmAC,lcmABC,a,b,c)
        if index<n:
            start = mid
        else:
            stop = mid
    return stop
def lcm(array):
    array = list(set(array))
    if len(array)==1:
        return array[0]
    a= array[0]
    multiple = a
    for num in array[1:]:
        a= math.gcd(a,num)
        multiple*=num
    return multiple/a
def getIndex(mid,lcmAB,lcmBC,lcmAC,lcmABC,a,b,c):
    numDivisibleC   = mid//c
    numDivisibleA   = mid//a
    numDivisibleB   = mid//b
    numDivisibleAB  = mid// lcmAB
    numDivisibleBC  = mid// lcmBC
    numDivisibleAC  = mid // lcmAC
    numDivisibleABC = mid //lcmABC
    if len(set([a,b,c]))==3:
        return numDivisibleA+numDivisibleB+numDivisibleC-numDivisibleAB-numDivisibleBC-numDivisibleAC+numDivisibleABC
    elif len(set([a,b,c]))==2:
        return sum(set([numDivisibleC,numDivisibleA,numDivisibleB]))-numDivisibleABC
    else:
        return numDivisibleA
