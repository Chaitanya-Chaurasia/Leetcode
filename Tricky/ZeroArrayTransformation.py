class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        # Trick: Difference Arrays + Prefix Sums
        # Step A) For every l,r in queries, apply range updates using DA 
        # To do this, at every start interval, we increment one and 
        # at every end interval + 1, we decrement one.
        # + 1 because while calculating prefix sum, our effect would end at index + 1.
        # Step B) Then, use prefix sum to apply the decrements
        # Step C) If prefix sum < nums[i], that means, it is not 0.
        # If prefix sum > nums[i], we proceed 
        n = len(nums)
        prefix = 0
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            if r + 1 < n:
                diff[r + 1] -= 1
        
        for i in range(n):
            prefix += diff[i]
            if nums[i] > prefix:
                return False
        return True
