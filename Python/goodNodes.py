# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        return self.countGoodNodes(root, root.val)

    def countGoodNodes(self, root: Optional[TreeNode], parentNodeVal: int) -> int:

        if root:
            goodNodes = self.countGoodNodes(root.left, max(parentNodeVal, root.val)) + self.countGoodNodes(root.right, max(parentNodeVal, root.val))
            if root.val >= parentNodeVal:
                goodNodes += 1
            return goodNodes
        
        return 0
