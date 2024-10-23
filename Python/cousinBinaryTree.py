# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        # logic: do dfs to find first element occurence
        # store its parent and level.
        # now start searching for second variable.
        # keep updating level, parents and check for cousin condition.
        
        if root is None:
            return None

        def dfs(curr, parent, depth, val):
            if not curr:
                return 0
            if curr.val == val:
                return depth

            parent[0] = curr.val
            left = dfs(curr.left, parent, depth + 1, val)
            if left:
                return left
            
            parent[0] = curr.val
            right = dfs(curr.right, parent, depth + 1, val)
            return right

        # store in list because TreeNode is a list
        parent_x, parent_y = [-1], [-1]
        d_x = dfs(root, parent_x, 0, x)
        d_y = dfs(root, parent_y, 0, y)

        return d_x == d_y and parent_x != parent_y
