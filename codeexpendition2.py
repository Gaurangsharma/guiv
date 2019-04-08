class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        root=Node(data)
        return root
    else:
        if root.val>data:
            root.left=insert(root.left,data)
        else:
            root.right=insert(root.right,data)
        return root
def inorder(root): 
    if root:  
        inorder(root.left)  
        inorder(root.right) 
        print(root.val)
n=int(input())
l=list(map(int,input().split()))
root=None
for i in range(n):
    root=insert(root,l[i]) 
inorder(root)