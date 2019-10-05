# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 00:37:01 2019

@author: huyn
"""
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.min = None
        self.max = None
        def dfs(root):
            if root:
                dfs(root.left)
                if not self.max:
                    self.min = root
                else:
                    self.max.right = root
                    root.left = self.max
                self.max = root
                dfs(root.right)
        dfs(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            self.min = self.min.right
            return self.min.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.min.right!=None
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15,TreeNode(9),TreeNode(20))
iterator   = BSTIterator(root)
#print (iterator.next())
#print (iterator.next())
#print (iterator.hasNext())
#print (iterator.next())
#
#print (iterator.hasNext())
#print (iterator.next())
#
#print (iterator.hasNext())
#print (iterator.next())
#
#print (iterator.hasNext())