# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return -1
        
        # do a bfs
        # store sum of each level.
        # sort the array in reverse and return kth value

        queue = deque([root])
        sums = []

        while queue:
            level_sum = 0
            elements_in_level = len(queue)
            for i in range(elements_in_level):
                node = queue.popleft()
                level_sum += node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
            sums.append(level_sum)
        
        if k > len(sums):
            return -1

        sums.sort(reverse=True)
        return sums[k - 1] 
