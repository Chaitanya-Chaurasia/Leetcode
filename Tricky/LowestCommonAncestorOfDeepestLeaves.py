# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Similar to LCA but instead of p and q, we need to find the LCA of deepest leaves.
        # Recall Postorder traversal - left, right, root.
        # This kicks an intuition.
        # TRICK: Postorder traversal + Maintain Depth of Tree
        # After every traversal, i.e after checking left and right subtrees, 
        # we check if height of left and right is same and equal to maxDepth.
        # If it is, they are the deepest leaves, and return root.
        
        depth, answer = -1, None

        def postOrder(root, level):
            nonlocal depth, answer

            if not root:
                return level - 1
            
            if level > depth:
                depth = level
            
            l, r = postOrder(root.left, level + 1), postOrder(root.right, level + 1)
            
            # Since we are doing post order traversal, we will be checking the leaves first.
            # In this process, the maxDepth is calculated in the first iteration itself.
            # Depending on the length of other deeper paths, we update it in line 26.
            if l == r == depth:
                answer = root
            
            return max(l, r)
            
        postOrder(root, 0)
        return answer
