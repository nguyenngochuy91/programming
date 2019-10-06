# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 19:51:40 2019

@author: Huy Nguyen
"""

class SpreadSheet:
    def __init__(self,numRow,numCol):
        self.matrix   = [[""]*numCol for i in range(numRow)]
#        self.colSpace = [0]*numCol
    def update(self,row,col,content):
        self.matrix[row][col] = str(content)
    def print(self):
        for row in range(len(self.matrix)):
            string = ""
            for item in self.matrix[row]:
                string+=item+"|"
            print (string[:-1])
    def prettyPrinting(self):
        colSpace = [0]*len(self.matrix[0])
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                item = self.matrix[row][col]
                colSpace[col]=max(colSpace[col],len(item))
        for row in range(len(self.matrix)):
            string = ""
            for col in range(len(self.matrix[0])):
                item = self.matrix[row][col]
#                val  =.. ..
                string+=item+" "*(colSpace[col]-len(item))+"|"
            print (string[:-1])  
    def sumFormula(self,inputString):
        currentSum = 0
        info       = inputString[5:-1]
        first,second = info.split("-")
        row1,col1    = map(int,first.split(":"))
        row2,col2    = map(int,second.split(":"))
        for row in range(row1,row2+1):
            for col in range(col1,col2+1):
                try:
                    val = int(self.matrix[row][col])
                except:
                    val = 0
                currentSum+=val
        return currentSum
# task1
mySpreaSheet = SpreadSheet(4,3)
mySpreaSheet.update(0,0,"bob")
mySpreaSheet.update(0,1,10)
mySpreaSheet.update(0,2,"foo")
mySpreaSheet.update(1,0,"alice")
mySpreaSheet.update(1,1,5)
mySpreaSheet.print()
mySpreaSheet.prettyPrinting()
mySpreaSheet.update(0,2,"")
mySpreaSheet.prettyPrinting()
mySpreaSheet.update(1,2,100)
print (mySpreaSheet.sumFormula("=sum(0:0-1:1)"))
print (mySpreaSheet.sumFormula("=sum(0:1-0:1)"))

