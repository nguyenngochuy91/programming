# -*- coding: utf-8 -*-
"""
Created on Sun May 26 05:24:49 2019

@author: Huy Nguyen
"""
def solve(R,C,K,matrix):
    nums = set()
    for item in matrix:
        for number in item:
            nums.add(number)
    currentMax = 0
    for number in nums:
        res, histRow = 0, ([0 for _ in matrix[0]]) if matrix else None
        for rowNums in matrix:
            stk = []
            for c, num in enumerate(rowNums):
                histRow[c] = (histRow[c]+1) if num == number else 0
            for i, n in enumerate(histRow+[0]):
                while stk and histRow[stk[-1]] > n:
                    h = histRow[stk.pop()]
                    res = max(res, h * ((i - stk[-1] - 1) if stk else i))
                    currentMax = max(currentMax,res)
                stk.append(i)
    return currentMax
T = int(input())
for i in range(T):
    R,C,K = [int(item) for item in input().split()]
    matrix = []
    for j in range(R):
        row = [int(item) for item in input().split()]
        matrix.append(row)
    res = solve(R,C,K,matrix)
    print ("Case #{}: {}".format(i+1,res))