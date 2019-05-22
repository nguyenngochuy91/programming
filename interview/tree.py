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

#919. Complete Binary Tree Inserter
#
#A complete binary tree is a binary tree in which every level, except possibly the last, is 
#completely filled, and all nodes are as far left as possible.
#
#Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:
#
#CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
#CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, 
#and returns the value of the parent of the inserted TreeNode;
#CBTInserter.get_root() will return the head node of the tree.
 
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, v: int) -> int:
        root = self
        level = [root]
        while level:
            nextLevel = []
            for node in level:
                if not node.left:
                    newNode = TreeNode(v)
                    node.left= newNode
                    return node.val
                else:
                    if not node.right:
                        newNode = TreeNode(v)
                        node.right= newNode
                        return node.val
                    else:
                        nextLevel.append(node.left)
                        nextLevel.append(node.right)
            level= nextLevel
            

    def get_root(self) -> TreeNode:
        return self.root