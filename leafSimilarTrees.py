# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def leafSearch(root: Optional[TreeNode], leaves: List[int]):

            if root is None:
                return
            
            if not root.left and not root.right:
                leaves.append(root.val)
                print(leaves) 
                return
            
            if root.left:
                leafSearch(root.left, leaves)
            if root.right:
                leafSearch(root.right, leaves)

        leafA = []
        leafB = []
        leafSearch(root1, leafA)
        leafSearch(root2, leafB)
        
        if leafA == leafB:
            return True
        
        return False
        
