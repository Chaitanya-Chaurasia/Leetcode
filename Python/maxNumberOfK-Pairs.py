class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # SORT THE LIST
        # START BY FINDING INDEX >= k
        # NOW USE TWO POINTERS AND CHECK SUM. IF SUM EXISTS, MOVE POINTERS AND INCREMENT ops.
        # IF SUM IS GREATER, DECREMENT, ELSE INCREMENT.

        ops = 0
        i = 0
        j = len(nums) - 1

        nums.sort()

        while (i < j):
            if nums[i] + nums[j] == k:
                ops += 1
                i += 1
                j -= 1
            
            elif nums[i] + nums[j] > k:
                j -= 1
            
            else:
                i += 1

        return ops
