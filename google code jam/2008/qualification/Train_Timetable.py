# -*- coding: utf-8 -*-
"""
Problem

A train line has two stations on it, A and B. Trains can take trips from A to B 
or from B to A multiple times during a day. When a train arrives at B from A (or arrives at A from B), 
it needs a certain amount of time before it is ready to take the return journey - 
this is the turnaround time. For example, if a train arrives at 12:00 
and the turnaround time is 0 minutes, it can leave immediately, at 12:00.

A train timetable specifies departure and arrival time of all trips between A and B. 
The train company needs to know how many trains have to start the day at A and B in 
order to make the timetable work: whenever a train is supposed to leave A or B, 
there must actually be one there ready to go. There are passing sections on the track,
so trains don't necessarily arrive in the same order that they leave. 
Trains may not travel on trips that do not appear on the schedule.

Input

The first line of input gives the number of cases, N. N test cases follow.
Each case contains a number of lines. The first line is the turnaround time, T,
 in minutes. The next line has two numbers on it, NA and NB. 
 NA is the number of trips from A to B, and NB is the number of trips from B to A. 
 Then there are NA lines giving the details of the trips from A to B.

Each line contains two fields, giving the HH:MM departure and arrival time for that trip. 
The departure time for each trip will be earlier than the arrival time. 
All arrivals and departures occur on the same day. 
The trips may appear in any order - they are not necessarily sorted by time. 
The hour and minute values are both two digits, zero-padded, and are on a 24-hour clock (00:00 through 23:59).
After these NA lines, there are NB lines giving the departure and arrival times for the trips from B to A.

Output

For each test case, output one line containing "Case #x: " 
followed by the number of trains that must start at A and the number of trains that must start at B.
"""
from heapq import heappop,heappush
def findMinNumTrain(trips,T):
    start = [0, 0]
    trains = [[], []]
    for trip in trips:
        station = trip[2]
        # check if there is a train at the station
        if trains[station] and trains[station][0]<=trip[0]:
            heappop(trains[station])
        else:
            # no train available, adding one
            start[station]+=1
        # add an available train at the other station, adding the turnover time
        heappush(trains[1-station],trip[1]+T)
    return start
def convertToMinute(time):
    hour,minute= time.split(":")
    return int(hour)*60+int(minute)
def solve(infile,outfile):
    handle     = open(infile,"r")
    N          = int(handle.readline().strip())
    outfile    = open(outfile,"w")
    for testCase in range(1,N+1):
        turnAroundTime = int(handle.readline().strip())
        NA,NB  = [int(item) for item in handle.readline().strip().split()]
        trips = []
        for i in range(NA):
            departure,arrival =  handle.readline().strip().split()
            trips.append([convertToMinute(departure),convertToMinute(arrival),0])
        for i in range(NB):
            departure,arrival = handle.readline().strip().split()
            trips.append([convertToMinute(departure),convertToMinute(arrival),1])
        trips.sort()
        A,B = findMinNumTrain(trips,turnAroundTime)
        outfile.write("Case #{}: {} {}\n".format(testCase,A,B))
    outfile.close()