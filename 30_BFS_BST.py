import sys
from collections import defaultdict

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        if root == None:
            return 
        
        queue = []
        queue.append(root)
        
        while queue:
            print(queue[0].data, end=" ") 
            node = queue.pop(0)
            if node.left != None:
                queue.append(node.left)
            
            if node.right != None:
                queue.append(node.right)
                
    def inOrder(self, root):
        if root.left:
            self.inOrder(root.left)

        print(root.data, end=" ")

        if root.right:
            self.inOrder(root.right)

T=int(input("Enter the number of nodes in the BST: "))
myTree=Solution()
root=None
for i in range(T):
    data=int(input(f"Enter Node {i+1}: "))
    root=myTree.insert(root,data)

print("The Level-Order-Traversal of the BST is:")
myTree.levelOrder(root)

print()

print("The In-Order-Traversal of the BST is:")
myTree.inOrder(root)