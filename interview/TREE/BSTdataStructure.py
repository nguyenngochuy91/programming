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
        def dfs(root,val):
            if not root:
                return None
            else:
                if root.val<val:
                    # we will do the delete call on the root.right, and we assign root.right to that
                    root.right = dfs(root.right,val)
                elif root.val > val:
                    # same thign as above, for case like emty, or we only have left or right child of root.left
                    root.left  = dfs(root.left,val)
                else:
                    # root.val == val
                    if not root.left and not root.right : # leaf case, basically return None
                        root = None
                    elif root.left and root.right: # has 2 children
                        # find the minimum value of root.right
                        minRightVal = self.getMinNode(root.right)
                        # swap value to our current root
                        root.val = minRightVal
                        # now we delete the right node and assign
                        root.right = dfs(root.right,val)
                    elif root.left:
                        return root.left # only left child , jsut return left so we can point it to our parent
                    elif root.right:
                        return root.right
        self = dfs(self,val)
    def getMinNode(self):
        root = self
        while root.left:
            root = root.left
        return root.val
    def getMaxNode(self):
        root = self
        while root.right:
            root = root.right
        return root.val
    # invert a binary tree
    def invertTree(self,root):
        if not root:
            return None
        else:
            if root.right and root.left:
                root.right,root.left = self.invertTree(root.left),self.invertTree(root.right)
            elif root.right:
                root.left = self.invertTree(root.right)
                root.right = None
            elif root.left:
                root.right = self.invertTree(root.left)
                root.left = None
            return root    
    def lowestCommonAncestor(self,node1,node2):
        return
class TreeNodeModified:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.countLeft = 0
        self.countRight = 0
    def insert(self,val):
        def add(root,val,parent,isLeft):
            if not root:
                if isLeft:
                    parent.left = TreeNodeModified(val)
                else:
                    parent.right = TreeNodeModified(val)
            else:
                if root.val<val:
                    root.countRight+=1
                    add(root.right,val,root,False)
                elif root.val>val:
                    root.countLeft+=1
                    add(root.left,val,root,True)
                elif root.val==val:
                    leftCount = root.countLeft
                    node = TreeNodeModified(val)
                    node.countLeft=leftCount
                    node.left = root.left
                    root.left = node
        add(self,val,None,True)
                    
    def searchK(self,k):
        root = self
        def dfs(root,size):
            if root:
                countRight = root.countRight
                if countRight+1==size:
                    return root.val
                elif countRight+1<size:
                    val = size - countRight-1
                    return dfs(root.left,val)
                else:
                    return dfs(root.right,size)
        return dfs(root,k)
        
    def print(self,node):
        if node:
            self.print(node.left)
            print ("node.val: {}, leftCount:{}, rightCount:{}".format(node.val,node.countLeft,node.countRight))
            self.print(node.right)
#nums = [4,5,8,2]
#root = TreeNodeModified(4)
#for item in nums[1:]:
#    root.insert(item)
##root.print(root)
#root.insert(3)
#root.insert(5)
#for i in range(1,7):
#    print (root.searchK(i))
#    