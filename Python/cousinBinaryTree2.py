# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # logic: 2-pass bfs
        # first pass: calculate sum of each level
        # second pass: for each level, get sibling sum and subtract it with level_sum. 
        # if 0 that means all nodes in same level are siblings.
        # if not 0, at least one cousin exists.

        queue = deque([root])
        sums = []
        while queue:
            level_sum = 0
            no_of_nodes = len(queue)
            for _ in range(no_of_nodes):
                curr_node = queue.popleft()
                level_sum += curr_node.val

                # push children to queue
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            sums.append(level_sum)
        
        queue = deque([root])
        idx = 1
        root.val = 0

        while queue:
            no_of_nodes = len(queue)
            for _ in range(no_of_nodes):
                curr_node = queue.popleft()
                sibling_sum = 0
                if curr_node.left:
                    sibling_sum += curr_node.left.val
                    queue.append(curr_node.left)
                if curr_node.right:
                    sibling_sum += curr_node.right.val
                    queue.append(curr_node.right)

                
                if curr_node.left:
                    curr_node.left.val = sums[idx] - sibling_sum
                if curr_node.right:
                    curr_node.right.val = sums[idx] - sibling_sum
            idx += 1
        
        return root
