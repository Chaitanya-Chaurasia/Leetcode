# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: 

        # Our approach: Use BFS to return the rightmost element in every level
        if not root:
            return []
        queue = deque([root])
        view = [root.val]
        while queue:
            nodes = []
            levelSize = len(queue)
            for _ in range(levelSize):
                parent = queue.popleft()
                if parent.left:
                    queue.append(parent.left)
                if parent.right:
                    queue.append(parent.right)
            if queue:
                view.append(queue[-1].val)
        return view
