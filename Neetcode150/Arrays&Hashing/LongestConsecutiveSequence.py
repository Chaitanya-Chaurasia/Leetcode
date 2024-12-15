class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for i in nums:
            lcs = 0
            if i - 1 not in nums:
                lcs = 1
                while i + lcs in nums:
                    lcs += 1
                ans = max(ans, lcs)
        return ans
