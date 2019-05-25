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
#865. Smallest Subtree with all the Deepest Nodes
#Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.
#
#A node is deepest if it has the largest depth possible among any node in the entire tree.
#
#The subtree of a node is that node, plus the set of all descendants of that node.
#
#Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

def subtreeWithAllDeepest(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    array = []
    def assignDepth(root,depth):
        if root:
            root.depth = depth
            array.append(depth)
            assignDepth(root.left,depth+1)
            assignDepth(root.right,depth+1)
    assignDepth(root,0)
    myMax= max(array)
    def answer(node):
        # Return the answer for the subtree at node.
        if not node or node.depth == myMax:
            return node
        L, R = answer(node.left), answer(node.right)
        return node if L and R else L or R

    return answer(root)

#897. Increasing Order Search Tree
#
#Given a tree, rearrange the tree in in-order so that the leftmost node in the 
#tree is now the root of the tree, and every node has no left child and only 1 right child.

def increasingBST(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    self.array = []
    def dfs(root):
        if root:
            dfs(root.left)
            self.array.append(root.val)
            dfs(root.right)
    dfs(root)
    root = TreeNode(self.array[0])
    head = root
    for item in self.array[1:]:
        newNode = TreeNode(item)
        head.right = newNode
        head = newNode
    return root
    
#429. N-ary Tree Level Order Traversal
#
#Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
def levelOrder(self, root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    level = [root]
    res = []
    while level:
        nextLevel = []
        values    = []
        for node in level:
            children = node.children
            nextLevel.extend(children)
            values.append(node.val)
        res.append(values)
        level = nextLevel
    return res
    
#993. Cousins in Binary Tree
#
#In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
#Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
#We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
#Return true if and only if the nodes corresponding to the values x and y are cousins.
def isCousins(self, root, x, y):
    """
    :type root: TreeNode
    :type x: int
    :type y: int
    :rtype: bool
    """
    self.d={}
    def assignInfo(root,p,x,y,d):
        if root:
            if root.val ==x:
                self.d[x] =[p,d]
            if root.val ==y:
                self.d[y] = [p,d]
            assignInfo(root.left,root,x,y,d+1)
            assignInfo(root.right,root,x,y,d+1)
    
    assignInfo(root,None,x,y,0)
    return self.d[x][0]!=self.d[y][0] and self.d[x][1]== self.d[y][1]
#1022. Sum of Root To Leaf Binary Numbers
#
#Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#
#For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
#
#Return the sum of these numbers.

def sumRootToLeaf(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.arr =[]
    def dfs(root,string):
        if root:
            if root.left:
                dfs(root.left,string+str(root.val))
            if root.right:
                dfs(root.right,string+str(root.val))
            if not root.left and not root.right:
                self.arr.append(string+str(root.val))
    dfs(root,"")
    return sum([int(item,2) for item in self.arr])
    
#988. Smallest String Starting From Leaf
#
#Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z':
#    a value of 0 represents 'a', a value of 1 represents 'b', and so on.
#
#Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
#
#(As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is 
#lexicographically smaller than "aba".  A leaf of a node is a node that has no children.)
    
def smallestFromLeaf(self, root):
    """
    :type root: TreeNode
    :rtype: str
    """
    self.string = None
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    self.d ={}
    for i in range(len(alphabet)):
        self.d[i] = alphabet[i]
    def dfs(root,string):
        if root:
            if root.left and root.right:
      
                dfs(root.left,string+self.d[root.val])
                dfs(root.right,string+self.d[root.val])
            elif root.left:
 
                dfs(root.left,string+self.d[root.val])
            elif root.right:
    
                dfs(root.right,string+self.d[root.val])
            else:

                string = string+self.d[root.val]
                if self.string:
                    self.string = min(self.string,string[::-1])
                else:
                    self.string = string[::-1]
                string = string[:-1]
    dfs(root,"")
    return self.string



#684. Redundant Connection
#
#In this problem, a tree is an undirected graph that is connected and has no cycles.
#
#The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), 
#with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an 
#edge that already existed.
#
#The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, 
#that represents an undirected edge connecting nodes u and v.
#
#Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are 
#multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in 
#the same format, with u < v.

def findRedundantConnection(self, edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    
    return None