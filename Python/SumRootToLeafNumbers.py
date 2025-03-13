# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        # Perform a DFS and append the entire path to a list
        # Base Case: Check if root is none, that means a leaf has been encountered
        # Return sum of list
        
        paths = []

        def dfs(node, path):
            if not node:
                return
            
            path += [node.val]

            if not node.left and not node.right:
                paths.append("".join([str(i) for i in path[:]]))

            dfs(node.left, path[:])
            dfs(node.right, path[:])

        dfs(root, [])
        return sum([int(i) for i in paths])
