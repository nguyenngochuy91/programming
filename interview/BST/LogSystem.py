# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:10:23 2019

@author: huyn
"""

#635. Design Log Storage System
#You are given several logs that each log contains a unique id and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.
#
#Design a log storage system to implement the following functions:
#
#void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.
#
#
#int[] Retrieve(String start, String end, String granularity): 
#    Return the id of logs whose timestamps are within the range from start to end. 
#    Start and end all have the same format as timestamp. However, granularity means the time level 
#    for consideration. For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", 
#    granularity = "Day", it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.
class LogSystem:

    def __init__(self):
        self.arr = []
        self.map    = {"Year":1,"Month":2,"Day":3,"Hour":4,"Minute":5,"Second":6}
        self.range  = [[2000,2017],[1,12],[1,31],[0,23],[0,59],[0,59]]
    def put(self, id: int, timestamp: str) -> None:
        time = Time(timestamp,id)
        if not self.arr:
            self.arr.append(time)
        else: # we will do an insert to index 
            start,stop = 0,len(self.arr)-1
            while start+1<stop:
                mid = (start+stop)//2
                if self.arr[mid]<time:
                    start = mid
                else:
                    stop  = mid
            if self.arr[stop]<time:
                self.arr.insert(stop+1,time)
            elif self.arr[start]<time:
                self.arr.insert(start+1,time)
            else:
                self.arr.insert(start,time)
    def retrieve(self, s: str, e: str, gra: str):
        res = []
        if self.arr:
            start = Time(s,None)
            stop  = Time(e,None)
            start.convert(gra,self.map,self.range,True)
            stop.convert(gra,self.map,self.range,False)
            leftMost = self.findLeftMost(start)
            rightMost = self.findRightMost(stop)
    #        print (leftMost,rightMost)
            if leftMost==-1 or rightMost==-1:
                return res
            for index in range(leftMost,rightMost+1):
                res.append(self.arr[index].id)
        return res
    def findLeftMost(self,time):
        start,stop = 0,len(self.arr)-1
        while start+1<stop:
            mid = (start+stop)//2
            if self.arr[mid]>=time:
                stop = mid
            else:
                start = mid
        if self.arr[start]>=time:
            return start
        if self.arr[stop]>=time:
            return stop
        return -1 # if the time is greater than all
    def findRightMost(self,time):
        start,stop = 0,len(self.arr)-1
        while start+1<stop:
            mid = (start+stop)//2
#            print (mid)
            if self.arr[mid]<=time:
#                print (77,mid)
                start = mid
            else:
#                print (79,mid)
                stop = mid
#        print ("stop",stop)
        if self.arr[stop]<=time:
            return stop
        if self.arr[start]<=time:
            return start
        return -1 # if the time is greater than all
# create a class of time
class Time:
    def __init__(self,string,id):
        self.string = [int(item) for item in string.split(":")]
        self.id     = id
    def convert(self,granularity,myMap,myRange,isDown):
        size = myMap[granularity]
        for index in range(size,6):
            if isDown:
                self.string[index]=myRange[index][0]
            else:
                self.string[index]=myRange[index][1]
    def __gt__(self,other):
        for i in range(6):
            val1 = self.string[i]
            val2 = other.string[i]
            if val1>val2:
                return True
            elif val1==val2:
                continue
            else:
                return False
        return False
    def __ge__(self,other):
        for i in range(6):
            val1 = self.string[i]
            val2 = other.string[i]
            if val1>val2:
                return True
            elif val1==val2:
                continue
            else:
                return False
        return True
#    def __le__(self,other):
        
system = LogSystem()
system.put(1,"2017:01:01:23:59:59")
system.put(2,"2017:01:01:22:59:59")
system.put(3,"2016:01:01:00:00:00")
out1 = system.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year")
out2 = system.retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour")