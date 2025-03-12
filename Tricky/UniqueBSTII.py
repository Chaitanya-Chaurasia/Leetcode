# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        # Similar to generating all phone numbers given n
        # Start with 1, and generate all possible subtrees using backtracking
        # Recursive DFS?
        # How do we make a BST?
        # We need two things: left and right subtree
        # Left subtree needs to be smaller than root, and right subtree needs to be greater.
        # So we can modify our range accordingly. 
        # If no such number exists, we append None.

        def generateTrees(start, end):
            if start > end:
                return [None,]
            trees = []
            for i in range(start, end + 1):
                leftSubtree = generateTrees(start, i - 1)
                rightSubtree = generateTrees(i + 1, end)

                for l in leftSubtree:
                    for r in rightSubtree:
                        newTree = TreeNode(i)
                        newTree.left = l
                        newTree.right = r
                        trees.append(newTree)
            return trees
        return generateTrees(1, n) if n else []
