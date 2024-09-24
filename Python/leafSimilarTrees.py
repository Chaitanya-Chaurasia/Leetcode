# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 or not root2:
            return False
        
        if not root1 and not root2:
            return True

        return self.LeafSequence([], root1) == self.LeafSequence([], root2)
    
    def LeafSequence(self, s: [], root: Optional[TreeNode]) -> []:
        
        # once you reach a leaf, append to s
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]
        
        return self.LeafSequence(s, root.left) + self.LeafSequence(s, root.right) 
