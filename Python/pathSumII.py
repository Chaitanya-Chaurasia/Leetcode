# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        if not root:
            return []
    
        def pathSumSolver(root: Optional[TreeNode], target: int, tempRes: List[int]):

            if not root:
                return
            if not root.left and not root.right and target - root.val == 0:
                tempRes.append(root.val)
                res.append(tempRes)
                return

            pathSumSolver(root.left, target - root.val, [*tempRes, root.val]) 
            pathSumSolver(root.right, target - root.val, [*tempRes, root.val])

          
        pathSumSolver(root, targetSum, [])
        return res
