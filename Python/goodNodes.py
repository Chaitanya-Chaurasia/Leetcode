# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        l = [0]

        def check(root, y):
            if root:
                x = max(root.val, y)

                if x <= root.val:
                    l[0] += 1
                
                if root.left:
                    check(root.left, x)
                if root.right:
                    check(root.right, x)

        check(root, -maxsize)
        return l[0]

        
