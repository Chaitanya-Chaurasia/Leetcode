class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        # Trick: DA (from Zero Array I) + Binary Search
        # We need to find the minimum no of queries (k) that can make the array 0
        # We can do this linearly, but it is inefficient.
        # To make the search quicker, we use binary search

        left, right, n = 0, len(queries), len(nums)

        def canTransform(k):

            diff = [0] * (n + 1)

            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r + 1] -= val
            
            prefix = 0
            for i in range(n):
                prefix += diff[i]
                if prefix < nums[i]:
                    return False
            return True

        if not canTransform(right):
            return -1

        while left < right:
            mid = (left + right) // 2
            if canTransform(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
