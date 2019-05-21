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
         
#998. Maximum Binary Tree II998. Maximum Binary Tree II
#
#We are given the root node of a maximum tree: a tree where every node has a value greater than any other value in its subtree.
#
#Just as in the previous problem, the given tree was constructed from an list A (root = Construct(A)) recursively with the following
# Construct(A) routine:
#
#If A is empty, return null.
#Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
#The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
#The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
#Return root.
#Note that we were not given A directly, only a root node root = Construct(A).
#
#Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.
#
#Return Construct(B).

def insertIntoMaxTree(root,val):
    if val>root.val:
        node = TreeNode(val)
        node.left = root
    else:
        # our val is lest than the root, we check if our root was all the way to the right
        if not root.right:
            node = TreeNode(val)
            root.right = node
            node = root
        else:
            # this means we have some number to the right, we check of val with this
            rightNode = insertIntoMaxTree(root.right,val)
            root.right = rightNode
            node = root
    return node

#979. Distribute Coins in Binary Tree
#
#Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
#
#In one move, we may choose two adjacent nodes and move one coin from one node to another. 
# (The move may be from parent to child, or from child to parent.)
#
#Return the number of moves requi
red to make every node have exactly one coin.
def distributeCoins(root):
    return root