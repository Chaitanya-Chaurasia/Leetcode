# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        # simple bfs approach

        if not root:
            return None

        sums = []
        queue = deque([root])
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.popleft()
                level_sum += curr_node.val
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            sums.append(level_sum)

        return sums.index(max(sums)) + 1
