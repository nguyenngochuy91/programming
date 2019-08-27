import random
from collections import deque
'''@function: Algorithm for deletion and duplication events
   @input   : tree in nwk format, set of genes
   @output  : tree in nwk format
'''       
def del_dup(rooted_tree,genes):
    # traverse Tree in post-order
    for node in rooted_tree.traverse('postorder'):
#        print (node.name)
        if not node.is_leaf():
            children = node.get_children()
            for gene in genes:
                intersect = (children[0].data[gene]).intersection(children[1].data[gene])
                if len(intersect) == 0:
                    node.data[gene] = (children[0].data[gene]).union(children[1].data[gene])
                else:
                    node.data[gene] = intersect

    # traverse top-down   
    for node in rooted_tree.traverse('levelorder'):
        for gene in genes:
            if node.is_root(): # for the root 
                # if the root has 2 candidate node, randomly choose 1, and get the numeric value
                node.data[gene] = (random.sample(node.data[gene],1))[0] 
            else:
                # for children node, first check the data from the ancestor
                ancestors = node.get_ancestors() # get the list of ancestor
                data = ancestors[0].data[gene] # get the data from the parent
                if data in node.data[gene]:# check if the node.data has value equal to its parent data
                    node.data[gene] = data
                else:
                    node.data[gene] = (random.sample(node.data[gene],1))[0]


    return rooted_tree
    
class TreeNode:
    def __init__(self,val=None,name= None,left=None,right=None):
        self.val   = val
        self.left  = left
        self.right = right
        self.name  = name
    def printLevel(self):
        level = 0
        queue = deque([self])
        while queue:
            size = len(queue)
            myList = []
            for i in range(size):
                node =queue.popleft()
                myList.append([node.name,node.val])
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print("level {} has {}".format(level,myList))
            level+=1
    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            if root.left and root.right:
                leftVal  = root.left.val
                rightVal = root.right.val
                if leftVal==rightVal:
                    root.val = leftVal
                else:
                    intersection = leftVal.intersection(rightVal)
                    if len(intersection)==0:
                        root.val =leftVal.union(rightVal)
                    else:
                        root.val = intersection
            elif root.left:
                root.val = root.left.val
            elif root.right:
                root.val = root.right.val
    def levelOrder(self,root,parent):
        if root:
            if not parent:
                root.val = random.choice(list(root.val))
            else:
                if root.left or root.right:
                    root.val = parent.val
                else:
                    root.val = root.val.pop()
            self.levelOrder(root.left,root)
            self.levelOrder(root.right,root)
#            A
#    B               C
#D(0)       E(0)       F(1)       G(1)

D=TreeNode(set([0]),"D")
E=TreeNode(set([0]),"E")
F=TreeNode(set([1]),"F")
G=TreeNode(set([1]),"G")
B=TreeNode(None,"B",D,E)
C=TreeNode(None,"C",F,G)
A=TreeNode(None,"A",B,C)
A.printLevel()
print ("After traverse Up")
A.postOrder(A)
A.printLevel()
print ("After traverse Down")
A.levelOrder(A,None)
A.printLevel()
        
        
