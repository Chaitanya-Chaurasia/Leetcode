# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        return self.DFS(root) != -1

    def DFS(self, root: Optional[TreeNode]) -> int:

        # on every right and left node of root, calculate height and if equal, two scenarios:
        # if both have children, continue to compute,
        # if only one has children, make that node as parent, and assign new left and right nodes.
        # to accomplish both at the same time, we start by iterating the deepest subtree, and coming all the way up. 

        if not root:
            return 0
        
        left_height = self.DFS(root.left)
        right_height = self.DFS(root.right)

        if (abs(left_height - right_height) > 1):
            return -1
        if (left_height == -1 or right_height == -1):
            return -1
        return max(left_height, right_height) + 1
