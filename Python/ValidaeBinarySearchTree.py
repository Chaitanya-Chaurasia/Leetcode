# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Method 1: Use Inorder traversal.
        # In a BST, Inorder Traversal is stricly increasing array.

        inorderT = []

        def inorder(root):
            if not root:
                return True
            
            if not inorder(root.left):
                return False

            if inorderT and root.val <= inorderT[-1]:
                return False

            inorderT.append(root.val)
            
            return inorder(root.right)
                    
        return inorder(root)
