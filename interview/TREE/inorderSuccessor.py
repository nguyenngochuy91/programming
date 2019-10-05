# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 19:45:59 2019

@author: huyn
"""
class TreeNode(object):
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right
def inorderSuccessorIterative(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    parents = []
    while root:
        if p.val==root.val:
            if p.right:
                return getMinRight(root.right)
            else:
                # we will traverse up the parent until we hit thte very first node greater
                while parents:
                    parent = parents.pop()
                    if parent.val>root.val:
                        return parent
                return None
        elif p.val<root.val:
            parents.append(root)
            root = root.left
        else:
            parents.append(root)
            root= root.right
        
                    
def getMinRight(node):
    while node.left:
        node = node.left
    return node

def inorderSuccessorRecursive(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    parents = []
    while root:
        if p.val==root.val:
            if p.right:
                return getMinRight(root.right)
            else:
                # we will traverse up the parent until we hit thte very first node greater
                while parents:
                    parent = parents.pop()
                    if parent.val>root.val:
                        return parent
                return None
        elif p.val<root.val:
            parents.append(root)
            root = root.left
        else:
            parents.append(root)
            root= root.right