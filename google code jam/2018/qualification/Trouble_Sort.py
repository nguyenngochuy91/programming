# -*- coding: utf-8 -*-
"""
Deep in Code Jam's secret algorithm labs, we devote countless hours to wrestling with one of the most 
complex problems of our time: efficiently sorting a list of integers into non-decreasing order. 
We have taken a careful look at the classic bubble sort algorithm, and we are pleased to announce a new variant.

The basic operation of the standard bubble sort algorithm is to examine a pair of adjacent numbers, and 
reverse that pair if the left number is larger than the right number. 
But our algorithm examines a group of three adjacent numbers, and if the leftmost number is larger than the 
rightmost number, it reverses that entire group. Because our algorithm is a "triplet bubble sort", 
we have named it Trouble Sort for short.

  TroubleSort(L): // L is a 0-indexed list of integers
    let done := false
    while not done:
      done = true
      for i := 0; i < len(L)-2; i++:
        if L[i] > L[i+2]:
          done = false
          reverse the sublist from L[i] to L[i+2], inclusive
For example, for L = 5 6 6 4 3, Trouble Sort would proceed as follows:

First pass:
inspect 5 6 6, do nothing: 5 6 6 4 3
inspect 6 6 4, see that 6 > 4, reverse the triplet: 5 4 6 6 3
inspect 6 6 3, see that 6 > 3, reverse the triplet: 5 4 3 6 6
Second pass:
inspect 5 4 3, see that 5 > 3, reverse the triplet: 3 4 5 6 6
inspect 4 5 6, do nothing: 3 4 5 6 6
inspect 5 6 6, do nothing: 3 4 5 6 6
Then the third pass inspects the three triplets and does nothing, so the algorithm terminates.
We were looking forward to presenting Trouble Sort at the Special Interest Group in Sorting 
conference in Hawaii, but one of our interns has just pointed out a problem: it is possible that 
Trouble Sort does not correctly sort the list! Consider the list 8 9 7, for example.


We need your help with some further research. Given a list of N integers, determine whether 
Trouble Sort will successfully sort the list into non-decreasing order. If it will not, 
find the index (counting starting from 0) of the first sorting error after the algorithm has finished: 
that is, the first value that is larger than the value that comes directly after it when the algorithm is done.

Input
The first line of the input gives the number of test cases, T. T test cases follow. 
Each test case consists of two lines: one line with an integer N, the number of values in the list, 
and then another line with N integers Vi, the list of values.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) 
and y is OK if Trouble Sort correctly sorts the list, or the index (counting starting from 0) of the first sorting error, 
as described above.
"""


import sys
def solve(array):
    arr1= [array[i] for i in range(0,len(array),2)]
    arr2= [array[i] for i in range(1,len(array),2)]
    arr1.sort()
    arr2.sort()
    newArray = []
    for i in range(min(len(arr1),len(arr2))):
        newArray.append(arr1[i])
        newArray.append(arr2[i])
    newArray.extend(arr1[i+1:])
    newArray.extend(arr2[i+1:])
    for i in range(len(array)-1):
        if newArray[i]>newArray[i+1]:
            return i
    return "OK"
T = int(input())
for i in range(T):
    N = int(input())
    array = map(int,input().split())
    result = solve(list(array))
    print ("Case #{}: {}".format(i+1,result))