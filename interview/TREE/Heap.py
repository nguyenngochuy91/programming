# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 20:21:41 2019

@author: Huy Nguyen
"""
import random
class Heap:
    def __init__(self,arr):
        self.arr =arr 
        self.size = len(arr)
    def heapify(self,index):
#        print (index)
        if index*2+1<self.size:
            left = index*2+1
            if index*2+2 <self.size:
                right = index*2+2
#                print ("left {} right {}".format(left,right))
                if self.arr[index]<max(self.arr[right],self.arr[left]):
                    if self.arr[right]>=self.arr[left]:
                        self.arr[index],self.arr[right]=self.arr[right],self.arr[index]
                        self.heapify(right)
                    else:
                        self.arr[index],self.arr[left]=self.arr[left],self.arr[index]
                        self.heapify(left)
            else:
                if self.arr[index]<self.arr[left]:
                    self.arr[index],self.arr[left]=self.arr[left],self.arr[index]
                    self.heapify(left)
        
    def buildMaxHeap(self):
        # the last parent of non leaf is allaways len(arr)//2
        for i in range(len(self.arr)//2-1,-1,-1):
#            print ("starting index:",i)
            self.heapify(i)
    
    def sort(self):
        for i in range(len(self.arr)-1,-1,-1):
            self.arr[i],self.arr[0]=self.arr[0],self.arr[i]
            self.size-=1
            self.heapify(0)
        

arr = []
for i in range(10):
    arr.append(random.randint(0,10))
#print (arr)
myHeap= Heap(arr)
myHeap.buildMaxHeap()
#print (arr)
myHeap.sort()
#print (arr)
#