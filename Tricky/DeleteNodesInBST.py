# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSuccessor(self, root):
        # two ways, either min of right subtree or max of left subtree 
        while root.left:
            root = root.left        
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # three cases
        # case a: node has both left and right children (replace with inorder successor)
        # case b: node is a leaf (simply delete it then)
        # case c: node has one child (replace by its child)
        # use recursion to search

        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # node with val key is found
        else:
            # case b
            if not root.right and not root.left:
                return None 
            # case c
            if not root.left:
                return root.right
            if not root.right :
                return root.left
           
            # case a
            # if both children, find successor
            root.val = self.findSuccessor(root.right)
            # remove duplicate successor
            root.right = self.deleteNode(root.right, root.val)

        return root
