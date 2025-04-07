class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1: Using extra space 
        # Use modulus to get new index of elements
        # Then copy rotated to nums, as we need to modify in place

        n = len(nums)
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i] 

        for i in range(n):
            nums[i] = rotated[i]

        # Approach 2: 3 Reverses
        # First reverse- entire array
        # Second reverse- 0 to k - 1
        # Third Reverse- k to end
