# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # https://www.youtube.com/watch?v=13m9ZCB8gjw

        # Naive Approach: We store the path of root->p and root-q.
        # We start comparing the paths, and the first mismatch is where the LCA occurs.
        # This requires extra space and hence not optimal.

        # Optimized approach: DFS
        # We recursively search for either p or q.
        # Once we find p or q, we return that node's val to its parent.
        # For example, if 6 -> 2, and q = 2, we find 2 and return 2 back to 6.
        # At every root, we make a comparison as follows: 
        # If we get at least one non-null value (i.e we find one of p or q), we return that.
        # If a parent gets both non-null values, that parent is the LCA.

        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left or right
