class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        # our approach- use prefix and suffix arrays
        # store all max elements until index i in prefix array
        # store all min elements until index i in suffix array
        # iterate through both of them, and find an index where prefix[i] < suffix[i + 1]
        # we use i + 1 because we need to find a partition and hence need to be one index ahead.
        # wherever this is encountered is where we have to make the partition

        prefix, suffix = [0]*len(nums), [0]*len(nums)
        prefix[0], suffix[-1] = nums[0], nums[-1] 
        for i in range(1, len(nums)):
            prefix[i] = max(prefix[i - 1], nums[i])
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])
        for i in range(len(prefix) - 1):
            if prefix[i] <= suffix[i + 1]:
                return i + 1
        return -1
