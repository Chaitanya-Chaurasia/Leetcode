# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        queue = [root]
        res = []

        while queue:
            levelSize = len(queue)
            nodes = []
            for _ in range(levelSize):
                parent = queue.pop(0)
                nodes.append(parent.val)
                if parent.left:
                    queue += [parent.left]
                if parent.right:
                    queue += [parent.right]
            res.append(nodes)
        return res
