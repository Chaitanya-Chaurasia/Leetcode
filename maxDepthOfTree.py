# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDepth(root: Optional[TreeNode], count: int) -> int:

            if root is None:
                return count

            count += 1
            return max(maxDepth(root.left, count), maxDepth(root.right, count))
        
        count = 0
        return maxDepth(root, count) 




            



        
