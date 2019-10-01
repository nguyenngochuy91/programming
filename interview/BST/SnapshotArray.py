# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:08:43 2019

@author: huyn
"""

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