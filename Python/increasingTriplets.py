class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        temp = nums

        if (temp.sort(reverse = True) == nums)

        while (l < r):
            if nums[r] > nums[l]:
                for i in range(r + 1, l):
                    if nums[l] < i < nums[r]:
                        return True
            else:
                l += 1
                r -= 1
        # the trick is to check if each element falls between the lowest and highest values.
        # starting from left, store min values uptil nums[i] at i.
        # starting from right, store max values from nums[i] to nums[-1].
        # iterate over nums, and check if nums[i] between left and right array values.

        # first = float('inf')
        # second = float('inf')

        # for i in nums:
        #     if i <= first:
        #         first = i
        #     elif i <= second:
        #         second = i
        #     else:
        #         return True
        
        # return False
        # return False
    
