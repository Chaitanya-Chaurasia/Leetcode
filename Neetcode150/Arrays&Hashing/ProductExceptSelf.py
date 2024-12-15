class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # have two runs
        # one for prefix and one for postfix
        # then iterate and multiply all elements of prefix and postfix

        prefix, postfix, res = 1, 1, [1]*len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
