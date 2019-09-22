# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:28:15 2018

@author: huynguyen
"""

class linkList(object):
    def __init__(self,val=None,next= None):
        self.val = val
        self.next = next
    def insertHead(self,val):
        head = linkList(val=val,next= self)
        self = head
    def insertAfter(self,val,prev):
        head = self
        while head:
            if head == prev:
                next = prev.next
                current = linkList(val,next)
                prev.next = current
                return True
        return False
    def deleteOne(self,node):
        if node == self:
            self = self.next
            return True
        head= self
        while head.next:
            if head.next == node:
                next = head.next.next
                self.next = next
                return True
        return False
        return False            
    def getLenthIter(self):
        c = 0
        head =self
        while head:
            c+=1
            head = head.next
            
        return c
    def getLengthRecur(self,head):
        c = 0
        if head:
            c+=self.getLengthRecur(head.next)
        return c

    def searchElementInter(self,node):
        head = self
        while head:
            if head == node:
                return True
        return False
    def searchElementRecur(self,node,head):
        if head:
            if head == node:
                return True
            else:
                return self.searchElementRecur(node,head.next)
                
    def getNthNodeIter(self,k):
        head  = self
        c= 0
        while head:
            c+=1
            if k ==c:
                return head.val
            head= head.next
        return -1
        
    def getNthNodeRecur(self,k,head):
        if head and k ==0:
            return head.val
        elif not head:
            return -1
        else:
            return self.getNthNodeRecur(k-1,head.next)
    def getMiddle(self):
        head1,head2= self,self
        while head2 and head2.next:
            head1,head2= head1.next,head2.next.next
        return head1
    
    def reverse(self):
        prev,current = None,self
        while current:
            next= current.next
            current.next= prev
            prev=current
            current = next
        return prev
    

        
            
            
    
    
array =[i for i in range(0,10)]
linkLists =[linkList(item) for item in array]
for i in range(9):
    linkLists[i].next = linkLists[i+1]
root = linkLists[0]           