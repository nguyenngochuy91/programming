# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:01:51 2019

@author: huyn
"""

#https://www.hackerrank.com/challenges/queens-attack-2/problem
def queensAttack(n, k, r_q, c_q, obstacles):
    r_q=n-r_q
    c_q-=1
#    print (r_q,c_q)
    dictionary= {} # store info of the range of the 4 lines goes through the queen is allow to travel
    dictionary["H"]= [-1,n]
    dictionary["V"]= [-1,n]
    # we basically use the row for indication
    # left diagonal
    decrease = min(r_q,c_q)
    increase = min(n-r_q,n-c_q-1)
#    print (decrease,increase)
    dictionary["LD"]=[max(r_q-decrease-1,-1),min(r_q+increase+1,n)]
    # right diagonal
    decrease = min(r_q,n-c_q-1)
    increase = min (c_q,n-r_q-1)
    dictionary["RD"]=[max(r_q-decrease-1,-1),min(r_q+increase+1,n)]
    for key in dictionary:
        print (key,dictionary[key])
    for obstacle in obstacles:
        x,y = obstacle
        x=n-x
        y-=1
#        print (x,y)
        if x== r_q:
            if y>c_q:
                dictionary["V"][1] = min( dictionary["V"][1] ,y)
            else:
                dictionary["V"][0] = max( dictionary["V"][0] ,y)
        elif y ==c_q:
            if x>r_q:
                dictionary["H"][1] = min( dictionary["H"][1] ,x)
            else:
                dictionary["H"][0] = max( dictionary["H"][0] ,x)
        else:
            if (x-r_q)/(y-c_q)==1:
                if x>r_q:
                    dictionary["LD"][1]= min(dictionary["LD"][1],x)
                else:
                    dictionary["LD"][0]= max(dictionary["LD"][0],x)
            elif (x-r_q)/(y-c_q)==-1:
                if x>r_q:
                    dictionary["RD"][1]= min(dictionary["RD"][1],x)
                else:
                    dictionary["RD"][0]= max(dictionary["RD"][0],x)
    c = 0
    for key in dictionary:
        start,stop = dictionary[key]
        print (key,start,stop)
        if start<stop:
            c+=stop-start-2
        print (c)
#    print ("final c:",c)
    return c