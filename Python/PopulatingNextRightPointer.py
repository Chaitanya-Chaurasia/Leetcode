"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        # Our approach: BFS
        # Maintain a result array, and at the end of every level traversal, append a "#" to the result

        if not root:
            return None

        queue = [root]
        res = []

        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.pop(0)
                if not queue:
                    node.next = None
                if i != levelSize - 1:
                    node.next = queue[0]
                if node.left:
                    queue += [node.left]
                if node.right:
                    queue += [node.right]    
        return root    
