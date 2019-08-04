# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:57:10 2019

@author: huyn
"""

# normal binary search, given a sorted array, and a number, find the index of the number in the array or return -1
def binarySearch(arr,num):
    start,stop = 0,len(arr)-1
    while start<=stop: # has to <= else it wont find all
        mid = (start+stop)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            start = mid+1
        else:
            stop = mid-1
    # if not found, then basically, start points to the smallest index that is bigger
    # stop points to the largest index that is smaller
    return -1  

# normal binary search, given a sorted array, and a number, find the index of the number or the smallest index that is 
# larger than the number or the index that is equal to the number
def binarySearchSmallestLarger(arr,num):
    start,stop = 0,len(arr)-1
    while start<=stop: # has to <= else it wont find all
        mid = (start+stop)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            start = mid+1
        else:
            stop = mid-1
    return start
# normal binary search, given a sorted array, and a number, find the index of the number or the smallest index that is 
# larger than the number or return -1 if not founded
def binarySearchSmallestLarger1(arr,num):
    start,stop = 0 , len(arr)-1
    while start<=stop:
        mid = (start+stop)//2
        if arr[mid] ==num:
            stop = mid-1
        elif arr[mid]>num:
            stop = mid-1
        else:
            start = mid+1
    if arr[start]==num:
        return -1
    return start
arr1= [1,3,5,7,9,11]
#print (binarySearchSmallestLarger1(arr1,2),1)
#print (binarySearchSmallestLarger1(arr1,3),2)
#print (binarySearchSmallestLarger1(arr1,9),5)
#print (binarySearchSmallestLarger1(arr1,10),5)
#print (binarySearchSmallestLarger1(arr1,11),-1)
    
# normal binary search, given a sorted array, and a number, find the index of the number or the largest index that is 
# smaller than the number or the index that is equal to the number
def binarySearchLargestSmaller(arr,num):
    start,stop = 0,len(arr)-1
    while start<=stop: # has to <= else it wont find all
        mid = (start+stop)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            start = mid+1
        else:
            stop = mid-1
    return stop    


#print (arr)
#for n in nums:
#    v1 = binarySearch(arr,n)
#    v2 = binarySearchSmallestLarger(arr,n)
#    print ("num {}, index using original {}, index using binarySearchSmallestLarger {}".format(n,v1,v2))

# given an sorted arr with duplication, return the smallest index of a given number of -1
def binarySearchDupLeft(arr,num):
    start,stop = 0,len(arr)-1

    while start<=stop: # has to <= else it wont find all
        mid = (start+stop)//2
        print (start,mid,stop)
        if arr[mid]==num:
            start = mid
            stop = mid-1
        elif arr[mid]<num:
            start = mid+1
        else:
            stop = mid-1
    # if not found, then basically, start points to the smallest index that is bigger
    # stop points to the largest index that is smaller
    return -1  
#arr = [6,6,6,6,6,6,6,6,6,6]
#print (binarySearchDupLeft(arr,6))
    
#1146. Snapshot Array
class SnapshotArray:

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
    