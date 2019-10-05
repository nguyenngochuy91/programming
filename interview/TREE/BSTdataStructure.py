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
    def search(self,val):
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
        
    def insert(self,val):
        return