# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:05:06 2019

@author: huyn
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
         
#951. Flip Equivalent Binary Trees
         
#For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
#
#A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
#
#Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

def flipEquiv(root1,root2):   
    if root1.val==root2.val:
        return True
    else:
        return False