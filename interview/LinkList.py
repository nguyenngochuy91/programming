# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:21:06 2019

@author: Huy Nguyen
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    # revere the link list
    def reverse(self):
        prev,head  = None,self
        while head.next:
            temp = head.next
            head.next= prev
            prev= head
            head = temp
        head.next = prev
        return head
    # convert into an array
    def toArray(self):
        array =[]
        head =self
        while head:
            array.append(head.val)
            head= head.next
        return array
        
#1019. Next Greater Node In Linked List
#
#We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
#
#Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val 
#such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  
#If such a j does not exist, the next larger value is 0.
#
#Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
#
#Note that in the example inputs (not outputs) below, arrays such as [2,1,5] 
#represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.
#Input: [2,1,5]
#Output: [5,5,0]
def nextLargerNodes(head):
    head = head.reverse()
    array = head.toArray()
    stack = []
    res   = []
    for item in array[::-1]:
        if not stack:
            res.append(0)
            stack.append(item)
        else:
            while stack:
                last = stack[-1]
                if last<=item:
                    stack.pop()
                else:
                    res.append(last)
                    stack.append(item)
                    break
            if not stack:
                res.append(0)
                stack.append(item)
    return res[::-1]

def convertArrayToLinkList(array):
    head = ListNode(array[0])
    node = head
    for item in array[1:]:
        newNode = ListNode(item)
        node.next = newNode
        node = newNode
    return head

#817. Linked List Components
#We are given head, the head node of a linked list containing unique integer values.
#
#We are also given the list G, a subset of the values in the linked list.
#
#Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

def numComponents(head,G):
    mySet = set(G)
    root = head
    res  = 0 
    while root:
        if root.val in mySet:
            if root.next:
                if root.next.val not in mySet:
                    res+=1
            else:
                res+=1
        root = root.next
    return res
    return None
