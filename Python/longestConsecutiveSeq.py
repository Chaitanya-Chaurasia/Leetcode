class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # so the entire question falls on how we know what element is our starting element in our LCS
        # to do this, we check if n-1 exists or not. 
        # we iterate through the array to check if n-1 exists or not.
        # if it doesn't, we have found our starting element and assign length as 1.
        # for every potential starting element, we iterate the array to calculate consecutive length and update the length 
        # as we go
        # me keep the max of lcs

        nums = set(nums)
        ans = 0
        for i in nums:
            length = 0
            if i - 1 not in nums:
                length = 1
                while i + length in nums:
                    length += 1
                ans = max(ans, length)
        return ans
