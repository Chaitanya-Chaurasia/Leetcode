# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        matrix = defaultdict(list)

        def convertToMap(root):
            if root.left:
                matrix[root.left.val].append(root.val)
                matrix[root.val].append(root.left.val)
                convertToMap(root.left)
            if root.right:
                matrix[root.right.val].append(root.val)
                matrix[root.val].append(root.right.val)
                convertToMap(root.right)
        
        convertToMap(root)
        queue = deque([start])
        visited = set()
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                visited.add(curr)
                for neighbour in matrix[curr]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return time
