class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort() 
        ops = 0
        l,r = 0, len(nums) - 1

        while l < r:
            sum = nums[l] + nums[r]

            if sum == k:
                ops += 1
                l += 1
                r -= 1

            elif sum < k:
                l = bisect.bisect_left(nums, k - nums[r], lo = l + 1, hi = r )
            else:
                r = bisect.bisect_right(nums, k - nums[l], lo = l, hi = r ) - 1

        return ops
