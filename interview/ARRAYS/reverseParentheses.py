# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:05:20 2019

@author: huyn
"""

def reverseParentheses(s: str) -> str:
    stack = []
    output = []
    string = ""
    res = ""
    for item in s:
        if item=="(":
            stack.append("(")
            if string:
                output.append(string)
                string = ""
        elif item== ")":
#            print ("2547, stack {}, output {}, string {}, res {}".format(stack,output,string,res))
            stack.pop()
            if string:
                output.append(string)
            if not stack:
                myString = "".join(output)
                res+=myString[::-1]
            else:
                myString = output.pop()
                if output:
                    output[-1]+=myString[::-1]
                else:
                    output.append(myString[::-1])
            string = ""
#            print ("2557, stack {}, output {}, string {}, res {}".format(stack,output,string,res))
        else:
            if not stack:         
                res+=item
            else:
                string+=item
    if string:
        res+=string
#    print (stack,output)
    return res