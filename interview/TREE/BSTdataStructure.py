# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 01:45:40 2019

@author: huyn
"""

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def searchRecursively(self,val):
        root = self
        def dfs(root):
            if not root:
                return None
            if root.val==val:
                return root
            elif root.val<val:
                return dfs(root.right)
            else:
                return dfs(root.left)
        return dfs(root)
    def searchIterative(self,val):
        root = self
        while root:
            if root.val==val:
                return True
            elif root.val<val:
                root = root.right
            else:
                root = root.left
        return False
    def insertRecursive(self,val):
        root  = self
        def dfs(root,parent,isLeft,val):
            if not root:
                if isLeft:
                    parent.left = TreeNode(val)
                else:
                    parent.right = TreeNode(val)
            else:
                if root.val>val:
                    dfs(root.left,root,True,val)
                else:
                    dfs(root.right,root,False,val)
        dfs(root,None,True,val)
    def insertIterative(self,val):
        root,parent = self,None
        while root:
            parent = root
            if root.val<val:
                root = root.right
            else:
                root = root.left
        newNode = TreeNode(val)
        if parent.val>val:
            parent.left = newNode
        else:
            parent.right = newNode
    def deleteRecursive(self,val):
        return