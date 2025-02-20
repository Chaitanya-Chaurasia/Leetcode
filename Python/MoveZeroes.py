class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # have two pointers
        # first pointer finds a zero 
        # second pointer starts from first pointer, and iterates until non-zero occurs.
        # swap pointers

        if len(nums) == 1:
            return nums

        left = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums
