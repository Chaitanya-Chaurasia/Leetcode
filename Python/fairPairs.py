class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        # trick: i < j will be maintained after sorting also.
        # this is because nums[i] + nums[j] = nums[j] + nums[i] meaning i != j
        # why we want to use binary search: to search faster instead of linear searching.
        # sort the array to use two pointers.
        # logic
        # for every element i in nums, we want to calculate the number of pairs such it l < nums[i] < u.
        # this gives us our targets u and l, and also our target condition.
        # for every element, we look for the number of pairs in its subarray to the right.
        # we use binary search instead of linear search to accomplish this.
        # we start with two pointers l and r, and keep moving pointers until target cond in met.
        # the index will represent the number of pairs i will have.
        # we do this with upper and lower bounds and subtract to find the intersection.

        res, le = 0, len(nums)
        nums.sort()

        def binarySearch(l, target):
            r = le - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1
            return r
        
        for i in range(le):
            low = lower - nums[i]
            up = upper - nums[i]
            low_pairs = binarySearch(i + 1, low)
            up_pairs = binarySearch(i + 1, up + 1)
            res += up_pairs - low_pairs
        return res  
